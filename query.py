#!/usr/bin/env python3
"""Tokin Ads Advisor query helper. Loads data/creative_enriched.json and answers
common questions without dumping the whole dataset to the caller.

Commands:
  top <metric> [N] [--min-spend X] [--asc]
  find <keyword> [--min-spend X] [-n N]
  ad <ad_id>
  cluster <cluster_id>
  group --by <dim> --metric <metric> [--min-spend X] [--asc] [-n N]
  compare <metric> <valueA> <valueB> [--by <dim>]
  list-clusters [--min-spend X] [-n N]

Metrics: roas, spend, revenue, purchases, ctr, cpm, cpp, cvr, impressions, clicks, flags
Dimensions for `group --by`:
  hook, title, cta, audience, strategy, account, year, season, fmt, body_len, tone, offer,
  month, dow, objective, opt_goal, compliance

Examples:
  python3 query.py top roas 10 --min-spend 500
  python3 query.py top cpp 10 --min-spend 500 --asc
  python3 query.py find "passover"
  python3 query.py cluster C003
  python3 query.py ad 120240817371500484
  python3 query.py group --by audience --metric roas --min-spend 500
  python3 query.py compare roas video image
"""
import json, os, sys, argparse, re
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = f"{ROOT}/data/creative_enriched.json"

def load():
    with open(DATA) as f:
        d = json.load(f)
    return d["ads"]

# ============================================================
# Formatters
# ============================================================
def fmt_money(v): return f"${v:,.0f}" if isinstance(v,(int,float)) and v==v else "—"
def fmt_pct(v): return f"{v:.2f}%" if v else "—"
def fmt_roas(v): return f"{v:.2f}x" if v else "—"
def fmt_num(v): return f"{v:,.0f}" if v else "0"
def fmt_cpp(v): return f"${v:,.2f}" if v and v<1e9 else "—"

def get_metric(a, metric):
    if metric == "cpp":
        return a["spend"]/a["purchases"] if a["purchases"] else float("inf")
    if metric == "flags":
        return len(a.get("compliance") or [])
    return a.get(metric, 0)

METRIC_HIGHER_BETTER = {
    "roas": True, "spend": True, "revenue": True, "purchases": True,
    "ctr": True, "cvr": True, "clicks": True, "impressions": True,
    "cpp": False, "cpm": False, "flags": False,
}

def metric_label(m):
    return {"roas":"ROAS","cpp":"CPP","ctr":"CTR","cpm":"CPM","cvr":"CVR",
            "spend":"Spend","revenue":"Revenue","purchases":"Purchases",
            "impressions":"Impressions","clicks":"Clicks","flags":"# flags"}.get(m,m)

def fmt_metric_val(m, v):
    if m == "roas": return fmt_roas(v)
    if m == "cpp":  return fmt_cpp(v)
    if m in ("ctr","cvr"): return fmt_pct(v)
    if m in ("cpm","spend","revenue"): return fmt_money(v)
    return fmt_num(v)

# ============================================================
# Commands
# ============================================================
def cmd_top(args):
    ads = load()
    if args.min_spend:
        ads = [a for a in ads if a["spend"] >= args.min_spend]
    higher = METRIC_HIGHER_BETTER.get(args.metric, True)
    asc = args.asc if args.asc is not None else not higher
    key = lambda a: get_metric(a, args.metric)
    ads.sort(key=key, reverse=not asc)
    # Filter infinities for cpp asc
    if args.metric == "cpp":
        ads = [a for a in ads if get_metric(a, "cpp") != float("inf")] + [a for a in ads if get_metric(a, "cpp") == float("inf")]
    n = args.n or 10
    print(f"# Top {n} ads by {metric_label(args.metric)} {'ASC' if asc else 'DESC'}" + (f" · min spend ${args.min_spend:,.0f}" if args.min_spend else ""))
    print(f"{'#':>3} {'ad_id':<22} {'acct':<4} {'date':<10} {'fmt':<5} {'spend':>9} {'roas':>6} {'purch':>6} {'cpp':>9} {'ctr':>7} · name")
    for i, a in enumerate(ads[:n], 1):
        acct = a["account"].replace("Tokin Chews ", "TC")
        cpp = get_metric(a, "cpp")
        cpp_s = fmt_cpp(cpp) if cpp != float("inf") else "   —"
        print(f"{i:>3} {a['id']:<22} {acct:<4} {a['created']:<10} {a['fmt']:<5} {fmt_money(a['spend']):>9} {fmt_roas(a['roas']):>6} {fmt_num(a['purchases']):>6} {cpp_s:>9} {fmt_pct(a['ctr']):>7} · {a['name'][:60]}")

def cmd_find(args):
    ads = load()
    q = args.keyword.lower()
    matches = []
    for a in ads:
        hay = (a["name"] + " " + a.get("body","") + " " + a.get("title","") + " " + a.get("adset","") + " " + a.get("campaign","")).lower()
        if q in hay:
            if args.min_spend and a["spend"] < args.min_spend: continue
            matches.append(a)
    matches.sort(key=lambda a: -a["spend"])
    n = args.n or 25
    print(f"# Found {len(matches)} ads matching '{args.keyword}'" + (f" · showing top {n} by spend" if len(matches)>n else ""))
    print(f"{'ad_id':<22} {'acct':<4} {'date':<10} {'fmt':<5} {'spend':>9} {'roas':>6} {'purch':>6} · name")
    for a in matches[:n]:
        acct = a["account"].replace("Tokin Chews ", "TC")
        print(f"{a['id']:<22} {acct:<4} {a['created']:<10} {a['fmt']:<5} {fmt_money(a['spend']):>9} {fmt_roas(a['roas']):>6} {fmt_num(a['purchases']):>6} · {a['name'][:70]}")

def cmd_ad(args):
    ads = load()
    a = next((x for x in ads if x["id"] == args.ad_id), None)
    if not a:
        print(f"Ad {args.ad_id} not found"); sys.exit(1)
    print(f"# Ad {a['id']} · {a['name']}")
    print(f"Account:   {a['account']}")
    print(f"Created:   {a['created']} ({a['season']} · {a['dow']})")
    print(f"Campaign:  {a['campaign']}  · {a['objective']}")
    print(f"Adset:     {a['adset']}  · opt {a['opt_goal']}")
    print(f"Format:    {a['fmt']}  · CTA: {a['cta']}")
    print(f"Title:     {a['title']!r}")
    print(f"Body:      {a.get('body','')!r}")
    print(f"LP:        {a.get('lp','')}")
    print(f"Cluster:   {a.get('cluster_id','—')}  · asset_uid {a.get('asset_uid','—')}")
    print()
    print(f"METRICS:   spend {fmt_money(a['spend'])} · ROAS {fmt_roas(a['roas'])} · {fmt_num(a['purchases'])} purch")
    cpp = get_metric(a,'cpp')
    print(f"           CTR {fmt_pct(a['ctr'])} · CPM {fmt_money(a['cpm'])} · CPP {fmt_cpp(cpp) if cpp!=float('inf') else '—'} · CVR {fmt_pct(a['cvr'])}")
    print()
    print(f"TARGETING: {a['targeting']['strategy']}")
    for aud in a['targeting'].get('audiences', [])[:5]: print(f"           · {aud}")
    print()
    print(f"OFFERS:    {', '.join(a.get('offers') or []) or '—'}")
    print(f"TONE:      {', '.join(a['patterns']['tone']) or '—'}")
    print(f"HOOK:      {a['patterns']['hook']!r}")
    print(f"BODY LEN:  {a['patterns']['body_len']} · {a['patterns']['word_count']} words")
    flags = a.get('compliance') or []
    if flags: print(f"⚠ FLAGS:   {', '.join(flags)}")
    thumb = a.get('thumb_med') or a.get('thumb') or ''
    if thumb: print(f"\nTHUMB:     {thumb}")
    if a.get('video_path'): print(f"VIDEO:     {a['video_path']}")

def cmd_cluster(args):
    ads = load()
    members = [a for a in ads if a.get("cluster_id") == args.cluster_id]
    if not members:
        print(f"Cluster {args.cluster_id} not found"); sys.exit(1)
    members.sort(key=lambda a: -a["roas"])
    total_spend = sum(a["spend"] for a in members)
    total_rev = sum(a["revenue"] for a in members)
    total_purch = sum(a["purchases"] for a in members)
    total_imps = sum(a["impressions"] for a in members)
    total_clicks = sum(a["clicks"] for a in members)
    print(f"# Cluster {args.cluster_id} · {len(members)} variants")
    print(f"Spend {fmt_money(total_spend)} · ROAS {fmt_roas(total_rev/total_spend if total_spend else 0)} · {fmt_num(total_purch)} purch · CPP {fmt_cpp(total_spend/total_purch if total_purch else 0)} · CTR {fmt_pct(total_clicks/total_imps*100 if total_imps else 0)}")
    dates = sorted([a["created"] for a in members if a["created"]])
    if dates: print(f"Ran: {dates[0]} → {dates[-1]}")
    # Unique assets within cluster
    asset_groups = defaultdict(list)
    for m in members:
        key = m.get("asset_uid") or m.get("video_id") or m.get("image_hash") or m["id"]
        asset_groups[key].append(m)
    print(f"Unique visual assets: {len(asset_groups)}")
    # Dominant CTA / audience / tone
    from collections import Counter
    cta = Counter(m["cta"] for m in members if m["cta"]).most_common(3)
    aud = Counter(a for m in members for a in m["targeting"].get("audiences",[])).most_common(3)
    tone = Counter(t for m in members for t in m["patterns"].get("tone",[])).most_common(3)
    print(f"Top CTAs:      {', '.join(f'{k} ({v})' for k,v in cta) or '—'}")
    print(f"Top audiences: {', '.join(f'{k[:50]} ({v})' for k,v in aud) or '—'}")
    print(f"Top tones:     {', '.join(f'{k} ({v})' for k,v in tone) or '—'}")
    print()
    print("VARIANTS (ranked by ROAS):")
    print(f"{'#':>3} {'ad_id':<22} {'acct':<4} {'fmt':<5} {'spend':>9} {'roas':>6} {'purch':>6} {'cpp':>9} · name")
    for i, a in enumerate(members, 1):
        acct = a["account"].replace("Tokin Chews ", "TC")
        cpp = get_metric(a, "cpp")
        cpp_s = fmt_cpp(cpp) if cpp != float("inf") else "   —"
        print(f"{i:>3} {a['id']:<22} {acct:<4} {a['fmt']:<5} {fmt_money(a['spend']):>9} {fmt_roas(a['roas']):>6} {fmt_num(a['purchases']):>6} {cpp_s:>9} · {a['name'][:60]}")
    # Winner + loser detail
    winner = members[0]; loser = members[-1] if len(members)>1 else None
    print()
    print(f"WINNER:  {winner['id']} · ROAS {fmt_roas(winner['roas'])} · {fmt_money(winner['spend'])}")
    print(f"  Hook:  {winner['patterns']['hook']!r}")
    print(f"  Title: {winner['title']!r}")
    print(f"  CTA:   {winner['cta']} · Targeting: {winner['targeting']['strategy']}")
    if winner.get('thumb_med'): print(f"  Thumb: {winner['thumb_med']}")
    if loser and loser['id'] != winner['id']:
        print(f"LOSER:   {loser['id']} · ROAS {fmt_roas(loser['roas'])} · {fmt_money(loser['spend'])}")
        if winner['cta'] != loser['cta']:   print(f"  ↳ different CTA (winner={winner['cta']} vs loser={loser['cta']})")
        ws, ls = winner['targeting']['strategy'], loser['targeting']['strategy']
        if ws != ls: print(f"  ↳ different targeting (winner={ws} vs loser={ls})")

def extract_dim(a, dim):
    if dim == "hook":     return a["patterns"]["hook"]
    if dim == "title":    return a["title"]
    if dim == "cta":      return a["cta"]
    if dim == "audience": return (a["targeting"].get("audiences") or [""])[0]
    if dim == "strategy": return a["targeting"].get("strategy","")
    if dim == "account":  return a["account"]
    if dim == "year":     return a["year"]
    if dim == "month":    return a["month"]
    if dim == "season":   return a["season"]
    if dim == "dow":      return a["dow"]
    if dim == "fmt":      return a["fmt"]
    if dim == "body_len": return a["patterns"]["body_len"]
    if dim == "tone":     return a["patterns"].get("tone", [])  # list
    if dim == "offer":    return a.get("offers", [])            # list
    if dim == "objective":return a.get("objective","")
    if dim == "opt_goal": return a.get("opt_goal","")
    if dim == "compliance": return a.get("compliance", [])       # list
    return a.get(dim, "")

def cmd_group(args):
    ads = load()
    if args.min_spend:
        ads = [a for a in ads if a["spend"] >= args.min_spend]
    buckets = defaultdict(lambda: {"ads":0, "spend":0, "revenue":0, "purchases":0, "imps":0, "clicks":0, "example_ids":[]})
    for a in ads:
        val = extract_dim(a, args.by)
        keys = val if isinstance(val, list) else [val]
        for k in keys:
            if not k: continue
            b = buckets[k]
            b["ads"] += 1
            b["spend"] += a["spend"]; b["revenue"] += a["revenue"]
            b["purchases"] += a["purchases"]
            b["imps"] += a["impressions"]; b["clicks"] += a["clicks"]
            if len(b["example_ids"]) < 3: b["example_ids"].append(a["id"])
    rows = []
    for k, b in buckets.items():
        if b["spend"] == 0: continue
        rows.append({
            "key": k, "ads": b["ads"], "spend": b["spend"], "revenue": b["revenue"],
            "purchases": b["purchases"],
            "roas": b["revenue"]/b["spend"] if b["spend"] else 0,
            "ctr":  b["clicks"]/b["imps"]*100 if b["imps"] else 0,
            "cpm":  b["spend"]/b["imps"]*1000 if b["imps"] else 0,
            "cpp":  b["spend"]/b["purchases"] if b["purchases"] else float("inf"),
            "examples": b["example_ids"],
        })
    higher = METRIC_HIGHER_BETTER.get(args.metric, True)
    asc = args.asc if args.asc is not None else not higher
    rows.sort(key=lambda r: (r[args.metric] if r[args.metric]!=float("inf") else (float("inf") if asc else float("-inf"))), reverse=not asc)
    n = args.n or 15
    print(f"# Group by {args.by} · ranked by {metric_label(args.metric)} {'ASC' if asc else 'DESC'}" + (f" · min spend ${args.min_spend:,.0f}" if args.min_spend else ""))
    print(f"{'#':>3} {'metric':>10} {'ads':>4} {'spend':>10} {'roas':>6} {'cpp':>9} {'ctr':>7} · value · example_ids")
    for i, r in enumerate(rows[:n], 1):
        cpp_s = fmt_cpp(r["cpp"]) if r["cpp"] != float("inf") else "   —"
        key_short = (str(r["key"])[:70] + "…") if len(str(r["key"]))>72 else str(r["key"])
        mv = r[args.metric]
        mv_s = fmt_metric_val(args.metric, mv) if mv != float("inf") else "—"
        print(f"{i:>3} {mv_s:>10} {r['ads']:>4} {fmt_money(r['spend']):>10} {fmt_roas(r['roas']):>6} {cpp_s:>9} {fmt_pct(r['ctr']):>7} · {key_short} · {', '.join(r['examples'])}")

def cmd_compare(args):
    ads = load()
    def bucket(a):
        v = extract_dim(a, args.by) if args.by else a["fmt"]
        if isinstance(v, list): return v
        return [v]
    def agg(subset, label):
        spend = sum(a["spend"] for a in subset)
        rev = sum(a["revenue"] for a in subset)
        purch = sum(a["purchases"] for a in subset)
        imps = sum(a["impressions"] for a in subset)
        clicks = sum(a["clicks"] for a in subset)
        return {
            "label": label, "n": len(subset),
            "spend": spend, "revenue": rev, "purchases": purch,
            "roas": rev/spend if spend else 0,
            "ctr": clicks/imps*100 if imps else 0,
            "cpm": spend/imps*1000 if imps else 0,
            "cpp": spend/purch if purch else float("inf"),
        }
    def match(a, val):
        b = bucket(a)
        return val.lower() in [str(x).lower() for x in b] or any(val.lower() in str(x).lower() for x in b)
    A = [a for a in ads if match(a, args.valueA)]
    B = [a for a in ads if match(a, args.valueB)]
    ra = agg(A, args.valueA); rb = agg(B, args.valueB)
    print(f"# Compare on {args.metric}: {args.valueA!r} vs {args.valueB!r}" + (f" (by {args.by})" if args.by else ""))
    print()
    for r in (ra, rb):
        cpp = fmt_cpp(r['cpp']) if r['cpp']!=float('inf') else '—'
        print(f"  {r['label']:<30} · {r['n']:>4} ads · {fmt_money(r['spend']):>9} spend · ROAS {fmt_roas(r['roas'])} · {fmt_num(r['purchases'])} purch · CTR {fmt_pct(r['ctr'])} · CPP {cpp}")
    # Diff on target metric
    def gv(r, m):
        if m == "cpp": return r["cpp"]
        return r[m]
    va, vb = gv(ra, args.metric), gv(rb, args.metric)
    if isinstance(va, float) and isinstance(vb, float) and va and vb and va!=float('inf') and vb!=float('inf'):
        higher = METRIC_HIGHER_BETTER.get(args.metric, True)
        winner = args.valueA if (va>vb)==higher else args.valueB
        delta = abs(va-vb)/min(va,vb)*100 if min(va,vb) else 0
        print(f"\n→ {winner} wins on {metric_label(args.metric)} by {delta:.0f}%")

def cmd_list_clusters(args):
    ads = load()
    groups = defaultdict(list)
    for a in ads:
        if a.get("cluster_id"): groups[a["cluster_id"]].append(a)
    rows = []
    for cid, members in groups.items():
        spend = sum(m["spend"] for m in members)
        if args.min_spend and spend < args.min_spend: continue
        rev = sum(m["revenue"] for m in members)
        purch = sum(m["purchases"] for m in members)
        winner = max(members, key=lambda m: m["roas"])
        rows.append({
            "cid": cid, "size": len(members),
            "spend": spend, "revenue": rev, "purchases": purch,
            "roas": rev/spend if spend else 0,
            "winner_roas": winner["roas"], "winner_id": winner["id"],
            "hook": winner["patterns"]["hook"][:60],
        })
    rows.sort(key=lambda r: -r["spend"])
    n = args.n or 30
    print(f"# Clusters" + (f" · min spend ${args.min_spend:,.0f}" if args.min_spend else "") + f" · {len(rows)} total, showing top {min(n,len(rows))}")
    print(f"{'cid':<6} {'size':>4} {'spend':>10} {'roas':>6} {'win-roas':>9} {'winner':<22} · hook")
    for r in rows[:n]:
        print(f"{r['cid']:<6} {r['size']:>4} {fmt_money(r['spend']):>10} {fmt_roas(r['roas']):>6} {fmt_roas(r['winner_roas']):>9} {r['winner_id']:<22} · {r['hook']!r}")

# ============================================================
# CLI
# ============================================================
def main():
    p = argparse.ArgumentParser(description="Tokin Ads Advisor query helper")
    sp = p.add_subparsers(dest="cmd", required=True)

    pt = sp.add_parser("top", help="Top N ads by metric")
    pt.add_argument("metric", choices=list(METRIC_HIGHER_BETTER.keys()))
    pt.add_argument("n", type=int, nargs="?", default=10)
    pt.add_argument("--min-spend", type=float, default=0)
    pt.add_argument("--asc", action="store_true", default=None)

    pf = sp.add_parser("find", help="Text search name/body/title/adset/campaign")
    pf.add_argument("keyword")
    pf.add_argument("--min-spend", type=float, default=0)
    pf.add_argument("-n", type=int, default=25)

    pa = sp.add_parser("ad", help="Full ad profile by ID")
    pa.add_argument("ad_id")

    pc = sp.add_parser("cluster", help="Full cluster profile")
    pc.add_argument("cluster_id")

    pg = sp.add_parser("group", help="Aggregate by dimension, rank by metric")
    pg.add_argument("--by", required=True, choices=["hook","title","cta","audience","strategy","account","year","month","season","dow","fmt","body_len","tone","offer","objective","opt_goal","compliance"])
    pg.add_argument("--metric", required=True, choices=list(METRIC_HIGHER_BETTER.keys()))
    pg.add_argument("--min-spend", type=float, default=0)
    pg.add_argument("--asc", action="store_true", default=None)
    pg.add_argument("-n", type=int, default=15)

    pcmp = sp.add_parser("compare", help="Compare two values on a metric")
    pcmp.add_argument("metric", choices=list(METRIC_HIGHER_BETTER.keys()))
    pcmp.add_argument("valueA")
    pcmp.add_argument("valueB")
    pcmp.add_argument("--by", choices=["hook","title","cta","audience","strategy","account","year","season","fmt","body_len","tone","offer"], default="fmt")

    plc = sp.add_parser("list-clusters", help="List all clusters by spend")
    plc.add_argument("--min-spend", type=float, default=0)
    plc.add_argument("-n", type=int, default=30)

    args = p.parse_args()
    cmds = {"top": cmd_top, "find": cmd_find, "ad": cmd_ad, "cluster": cmd_cluster,
            "group": cmd_group, "compare": cmd_compare, "list-clusters": cmd_list_clusters}
    cmds[args.cmd](args)

if __name__ == "__main__":
    main()
