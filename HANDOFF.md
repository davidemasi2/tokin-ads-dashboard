# Tokin Ads Dashboard — Handoff (2026-04-22, 12:42 MDT)

## Live URLs
- **Dashboard**: https://tokin-ads-dashboard-production.up.railway.app
- **Creative Breakdown** (same as root): https://tokin-ads-dashboard-production.up.railway.app/creative_breakdown.html
- **GitHub repo** (now public): https://github.com/davidemasi2/tokin-ads-dashboard
- **Skill tarball** (145 KB, bundled data + query helper): https://github.com/davidemasi2/tokin-ads-dashboard/raw/main/tokin-ads-advisor.tar.gz
- **Railway project**: 1d4aee66-d932-4f16-b934-83eaf581043e

## Dataset (unchanged since last handoff)
- **721 ads** across TC1 (571) · TC2 (122) · TC3 (28) · TC4 (empty)
- **$356,556 spend · $794,193 revenue · 2.23× ROAS · 10,675 purchases**
- **97 clusters** covering 635 ads (88%) · **312 unique visual assets** (pHash deduped)
- **501/721 ads with LPs populated** · **166 compliance-flagged ads**

## Dashboard tabs (8)
1. **Summary** (default) — auto insights + SCALE/KILL/TEST/FIX action list + leaderboards
2. **Clusters** — asset ranking (pHash deduped) · signal ranking table (26 dims) · per-variant table with targeting/CTA/LP/copy
3. **Tiers** — flagship/scalers/winners/marginal/losers/money pits/untested
4. **Patterns** — 14 ROAS-ranked tables, sortable
5. **Targeting** — strategy + audience-tag, sortable
6. **Compliance** — FDA/Health/THC-CBD/Superlative/Time-urgency flagged
7. **Reproduce** — live recommendations: Optimize for ROAS/CPP/CTR/Compliance-safe · min spend · show 10-100
8. **All ads** — flat sortable

All views filter-aware (Year · Account · Format · Tier · Offer · min-spend slider · full-text search) + sort by CPP everywhere.

## Skills shipped this session
- **tokin-ads-advisor** — installed at `~/.claude/skills/tokin-ads-advisor/` globally + packaged as standalone tarball
  - Auto-invokes on Tokin ads questions
  - `query.py` helper with top/find/ad/cluster/group/compare/list-clusters commands
  - 721 ads of data bundled — zero dependencies
  - One-line install: `curl -fsSL https://github.com/davidemasi2/tokin-ads-dashboard/raw/main/tokin-ads-advisor.tar.gz | tar -xzf - -C /tmp && bash /tmp/tokin-ads-advisor/install.sh`
  - Cross-references `tokin-jew-db` skill for live Shopify/Klaviyo queries
- **tokin-jew-db** — existing skill that this one chains to for commerce questions

## Notion pages updated
- **Internal Tools Guide** (`34a26136-b372-8187-b7eb-c53325bf1630`) — 4 tools: Command Center · Claude DB Skill · **Claude Ads Advisor (new section 3)** · Ads Dashboard

## Thumbnail strategy (unchanged)
- Local (`file://`/localhost): `fullres/` → `thumbnails_med/` → `thumbnails/`
- Remote (Railway): `thumbnails_med/` (500×500) → `thumbnails/` fallback
- Videos: local = `videos/`, remote = GitHub raw URLs
- Sizes: ad-card 100px · member-grid 72px · Reproduce hero 220px · asset-rank card 180px · variant-table 48px

## Data pipeline
```
raw/ads_{acc}.json + raw/insights_{acc}.json
  └─ merge_all.py           → data/merged.json (721 rows)
  └─ analyze.py             → data/analysis.json
  └─ dedup_assets.py        → data/asset_groups.json (pHash/dHash, Hamming ≤6)
  └─ enrich_creative.py     → data/creative_enriched.json
  └─ make_medium_thumbs.py  → thumbnails_med/ (500×500 q85)
  └─ build_breakdown.py     → public/creative_breakdown.html + public/index.html
```

## Commands
```bash
# Full rebuild
python3 merge_all.py && python3 analyze.py && python3 dedup_assets.py && python3 enrich_creative.py && python3 build_breakdown.py
cp public/creative_breakdown.html public/index.html public-lite/creative_breakdown.html public-lite/index.html

# Skill refresh (after data re-enrichment)
cp data/creative_enriched.json data/asset_groups.json ~/.claude/skills/tokin-ads-advisor/data/
cd ~/.claude/skills && tar -czf /tmp/tokin-ads-advisor.tar.gz --exclude='*.tar.gz' tokin-ads-advisor/
cp /tmp/tokin-ads-advisor.tar.gz ~/.claude/skills/tokin-ads-advisor/
cp /tmp/tokin-ads-advisor.tar.gz "{WORKING_DIR}/public/"
cd {WORKING_DIR}/public && git add -A && git commit -m "refresh skill data" && git push

# Deploy
(cd public && git add -A && git commit -m "..." && git push)  # GitHub (public) — videos served from raw URLs
(cd public-lite && mv videos /tmp/v_$$ && railway up --detach && mv /tmp/v_$$ videos)

# Query helper (works anywhere)
python3 ~/.claude/skills/tokin-ads-advisor/query.py top roas 10 --min-spend 500
python3 ~/.claude/skills/tokin-ads-advisor/query.py cluster C003
python3 ~/.claude/skills/tokin-ads-advisor/query.py group --by audience --metric cpp --asc
```

## Paid Media Plan analysis — PENDING NOTION PAGE
*This session's big deliverable — full 3-campaign strategy for new media buyer onboarding.*

**Plan summary (3 campaigns across risk spectrum):**

### Campaign #1 — "Kosher Closet" 🟢 LOW RISK
Apparel ToFu → 12.5% crossover to chews. $100K historical data at 2.28× ROAS, 0 compliance flags. Hero: Ad `120235840343690484` guiltypleasure.2 video (4.80× ROAS, $17 CPP). Backup: Ad `120236100453450484` Kiddush Cup V5 (6.04× ROAS). Main BM, LAL 1%, $150/day start. Expected LTV-ROAS ~3.5×.

### Campaign #2 — "Gifting Funnel" 🟢 LOW-MEDIUM RISK
Gelt + cookies + bundles. 2.40× ROAS on $67K gelt + 2.38× on $77K cookies (only 8 flagged of 88). **Chocolate gelt is #1 crossover product** (167 post-merch orders on chews brand). Hero: Ad `120235839731570484` "Gelt that gets you chai DC V1" ($27K · 2.92× ROAS). Season lift: Spring runs 2.52× vs Fall 2.10× — time Feb-May. Expected LTV-ROAS ~4.0×.

### Campaign #3 — "Which Tokin' Jew Are You?" 🟡 HIGHER RISK
Interactive quiz ToFu. Proof point: Ad `120239611228270484` "Mix, Match, & Get Chai" compliance-clean at 3.64× ROAS. Quiz archetypes: Rabbi/Bubbe/Mensch/Schlimazel → flavor recommendation. Requires **new Business Manager + jump page** (`tokinjewquiz.com`) to isolate risk. $50/day for 14 days, scale if CAC < $30.

**Key data cited:**
- LTV by first-brand: chews-first $116 vs merch-first $82 (40% higher)
- Merch → chews crossover rate: apparel 12.5% · paraphernalia 12.5% · papers 10.5% · judaica 6.8%
- Top crossover products: Chocolate Gelt ($11.8K), Watermelon High Dose, flavor variety
- Compliance flag rate by bucket: gummy 28%, papers 20%, clothing 0%
- Character video CTR 5.19% (portfolio-leading, only 13 clean ads — under-explored)

**Creative hero ad IDs + thumbnails** (for the Notion page):
| Ad ID | Fmt | Name | Thumb path |
|---|---|---|---|
| 120235840343690484 | video | guiltypleasure.2 | thumbnails/120235840343690484_20bc4d3065.jpg |
| 120235839927630484 | image | Gelt that gets you chai DC V2 | thumbnails_med/adimg_1449383908993328_7e754b6be9c1.jpg |
| 120236100453450484 | image | Kiddush Cup (sqr) V5 | thumbnails_med/adimg_1449383908993328_e2ec163176c5.jpg |
| 120235839731570484 | image | Gelt that gets you chai DC V1 | thumbnails_med/adimg_1449383908993328_f45b3b26320f.jpg |
| 120219109515800484 | image | Hamantaschen - Header | thumbnails_med/adimg_1449383908993328_bc03ec5ddf3e.jpg |
| 120239611228270484 | image | TC x Variety Pack (sqr) V1 (COMPLIANT) | thumbnails_med/adimg_1449383908993328_aa235400dc5a.jpg |
| 120234591667130484 | image | Kiddush Cup (sqr) V2 | thumbnails_med/adimg_1449383908993328_fb1766ba75e1.jpg |
| 120237189249690484 | image | THE CHAI HOLIDAYS Hanukkah Bundle | thumbnails_med/adimg_1449383908993328_4fcf84854af6.jpg |
| 120235840055520484 | image | Gelty Pleasure (sqr) V1 | thumbnails_med/adimg_1449383908993328_0fd1cd3a8fc7.jpg |
| 120220249726550484 | image | K4P - image - cirtus | thumbnails_med/adimg_1449383908993328_ee2ab9fb5028.jpg |
| 120240805947640484 | video | TokinChew Brand Awareness V2 | thumbnails/120240805947640484_3d0ba2c8eb.jpg |

**Remote URL prefix for thumbnails**: `https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/`

## NEXT SESSION — TO BUILD
1. **Create Notion page "Paid Media Plan"** under "Tokin' Home" (parent: `06b26136-b372-83ae-b247-81e3464c837a`)
   - Top of page: Links to 4 tools (Command Center, Claude DB Skill, Claude Ads Advisor, Ads Dashboard)
   - Section 1: Evidence tables (performance by bucket, crossover rates, LTV)
   - Section 2: Campaign #1 Kosher Closet — full brief + hero creative thumbnails
   - Section 3: Campaign #2 Gifting Funnel — full brief + hero creative thumbnails
   - Section 4: Campaign #3 Tokin Jew Quiz — full brief + jump page spec
   - Section 5: Deployment calendar (W1-W7+)
   - Section 6: 90-day projected economics table
   - Section 7: Non-negotiables for new media buyer
2. Use GitHub raw URLs for all thumbnails so they render inline in Notion
3. Optional follow-ups user may request: ad-copy drafts, quiz spec, nano-banana hero generation, media plan doc

## Known gaps / next refresh
- Data snapshot is 2026-04-21 · re-pull Meta if campaigns launch
- 87 Meta video source URLs have expired — rerun `pull_videos_missing.py` with fresh token if needed
- fullres/ is local-only (318 MB too big for Railway)

## Recent commits (top 10)
```
a881c3c  Ship tokin-ads-advisor skill tarball (standalone, 145KB, bundled data)
4d62d23  Add query.py helper for tokin-ads-advisor skill
e044bee  Update HANDOFF: clusters · asset dedup · variant tables · CPP sort
6ab67b5  CPP + full metric sort coverage on Tiers/Clusters/Compliance/All-ads
8e4e9d3  Variant ranking table in Clusters+Reproduce · LP populated (501/721)
5012742  Reproduce rework: 220px hero · top-3 variants table · asset ranking
3b0e503  Cluster sort: Winner-only options (ROAS/CPP/CTR/CPM/purchases/spend)
9e510e0  Perceptual-hash asset dedup: 721 ads → 312 unique visuals
05f6812  Per-asset ranking inside cluster cards with delta-vs-median
5e1677f  Cluster signals: 26 creative+targeting dims ranked with strength bars
```
