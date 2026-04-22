# Tokin Ads Dashboard — Handoff (2026-04-22, 10:47 MDT)

## Live URLs
- **Dashboard**: https://tokin-ads-dashboard-production.up.railway.app
- **Creative Breakdown** (now the same as root): https://tokin-ads-dashboard-production.up.railway.app/creative_breakdown.html
- **GitHub**: https://github.com/davidemasi2/tokin-ads-dashboard
- **Railway project**: 1d4aee66-d932-4f16-b934-83eaf581043e

## Dataset
- **721 ads** across TC1, TC2, TC3 (TC4 empty)
  - TC1 · 571 ads · 456 insight rows
  - TC2 · 122 ads · 68 rows
  - TC3 · 28 ads · 24 rows
- **Portfolio totals**: $356,556 spend · $794,193 revenue · **2.23× ROAS** · 10,675 purchases
- **97 creative clusters** covering **635 ads (88%)** — union-find across asset / title / hook / body-text Jaccard
- **312 unique visual assets** (perceptual-hash dedup) — 138 are shared across >1 ad
- **501 / 721** ads carry landing-page URLs (clickable on every card)
- **166** compliance-flagged ads across 7 flag types
- **77 MP4s** on disk · 66 with native video thumbs · 87 source URLs expired on Meta's CDN
- **989 medium thumbnails** (500×500, 39.5 MB) for Railway · **989 fullres** (318 MB, local-only)

## Dashboard tabs

1. **Summary** (default) — filter-aware insights + SCALE / KILL / TEST / FIX action list · leaderboards grid with *Rank by* selector (ROAS / Spend / Purchases / CTR / CPP / CPM / Ads)
2. **Clusters** — every cluster card shows:
   - Aggregate + per-variant metrics (spend, ROAS, CPP, CTR, purchases)
   - Cluster-sort dropdown: 10 aggregate options + 8 winner-only options (all include CPP ↑↓)
   - **Winner by** selector: ROAS / CPP / CTR / CPM / Purchases / Spend → drives winner selection + signal analysis
   - **🖼 Asset-level ranking**: grid of unique visual assets in the cluster (perceptual-hash deduped) with per-asset metrics and delta-vs-median
   - **🧪 Signal ranking table**: 26 creative+targeting dimensions analyzed for causal impact, ranked by effect size with strength bars (🎨 creative vs 🎯 targeting split)
   - **📋 Per-variant ranking table**: every variant's tag, thumb, name, CTA, targeting, landing-page link, copy snippet, and metric — winner highlighted green, loser red
   - Expandable full ad cards
3. **Tiers** — flagship / scalers / winners / marginal / losers / money pits / untested, each with a sort dropdown covering CPP + all metrics in both directions
4. **Patterns** — 14 ROAS-ranked tables (hook, CTA, offer, body length, tone, format, objective, opt goal, question vs statement, emoji, hashtag, year, season, day of week). Every column header sortable (CPP included).
5. **Targeting** — strategy + audience-tag tables; every column sortable incl. CPP
6. **Compliance** — FDA / Health / THC-CBD / Superlative / Time-urgency / Guarantee / Kids flagged ads. Flag summary table has CPP. Flagged-ads grid has full sort dropdown incl. CPP
7. **Reproduce** — reactive recommendations:
   - **Optimize for**: ROAS / CPP / CTR / Compliance-safe + profitable
   - **Min spend** $50–$5K · **Show** 10–100 cards
   - Spans clusters AND solo ads (every ad is eligible)
   - Each card: 220 px hero of the top asset · "why picked" explanation · Top-3 variant summary · full creative recipe · asset-level ranking · per-variant ranking table · one-shot copy-paste prompt
8. **All ads** — flat sortable list

## Filters (compose across all tabs)
Year · Account · Format · Tier · Offer (or none) · **Min-spend slider** ($0–$25K log-stop) · full-text search (name / body / adset / campaign)

## Thumbnail strategy
- **Local** (`file://` or `localhost`): prefers `fullres/` (1080 px, 318 MB) → `thumbnails_med/` (500 px) → `thumbnails/` (Meta small)
- **Remote** (Railway): `thumbnails_med/` (500 px) → `thumbnails/` fallback
- **Videos**: local plays from `videos/`; remote plays via GitHub raw URLs (`raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/videos/vid_X.mp4`) to keep Railway payload at 52 MB
- Sizes normalized: ad-card 100 px · member-grid 72 px · Reproduce hero 220 px · variant-table 48 px · asset-rank card 180 px
- Auto-detects environment via `location.protocol` + hostname

## Data pipeline
```
raw/ads_{acc}.json + raw/insights_{acc}.json
  └─ merge_all.py           → data/merged.json (721 rows)
  └─ analyze.py             → data/analysis.json + data/ads.csv
  └─ dedup_assets.py        → data/asset_groups.json (pHash/dHash dedup, Hamming ≤6)
  └─ enrich_creative.py     → data/creative_enriched.json
       • thumb / thumb_med / thumb_full / video_path / video_thumb_path / asset_uid
       • cluster_id (union-find: asset ∪ title ∪ hook ∪ body-Jaccard ≥0.50)
       • offer detection · compliance flags (7 rules)
       • pattern tags · targeting classification
       • landing-page URL
  └─ make_medium_thumbs.py  → thumbnails_med/ (500×500 q85)
  └─ build_breakdown.py     → public/creative_breakdown.html + public/index.html
```

## Commands
```bash
# Full rebuild from raw data
python3 merge_all.py && python3 analyze.py && python3 dedup_assets.py && python3 enrich_creative.py && python3 build_breakdown.py
cp public/creative_breakdown.html public/index.html
cp public/creative_breakdown.html public-lite/creative_breakdown.html && cp public/creative_breakdown.html public-lite/index.html

# Sync assets to public-lite (remote)
rsync -a thumbnails/ public-lite/thumbnails/
rsync -a thumbnails_med/ public-lite/thumbnails_med/

# Deploy
(cd public && git add -A && git commit -m "..." && git push)          # GitHub (videos served from here via raw URLs)
(cd public-lite && mv videos /tmp/v_$$ && railway up --detach && mv /tmp/v_$$ videos)   # Railway (move videos out — deploys > 60 MB time out)

# Video re-pull (needs fresh Meta token)
python3 pull_videos_missing.py  # idempotent — only fetches missing MP4s
```

## Meta token
Stored in `~/.claude/projects/.../memory/reference_meta_token.md`. Ad account IDs:
- TC1: `1449383908993328`  · TC2: `24992731496994614`  · TC3: `745810064600142`  · TC4: `1407910603745588`

## Known gaps / next steps
- **Railway CLI uploads time out** on payloads >80 MB — current workflow moves `videos/` to /tmp before `railway up`, since videos are served from GitHub raw URLs anyway. Consider connecting Railway to the GitHub repo for Git-based deploys.
- **87 Meta video source URLs expired** on CDN — re-running `pull_videos_missing.py` with a fresh token may recover some.
- **1 silent MP4** (video only, no audio).
- **fullres/ is local-only** (318 MB too big for Railway free tier).

## Recent commits (top 12)
```
6ab67b5  CPP + full metric sort coverage on Tiers/Clusters/Compliance/All-ads
8e4e9d3  Variant ranking table in Clusters+Reproduce · LP populated (501/721)
5012742  Reproduce rework: 220 px hero · top-3 variants table · asset ranking inline
3b0e503  Cluster sort: add Winner-only sort options (ROAS/CPP/CTR/CPM/purchases/spend)
9e510e0  Perceptual-hash asset dedup: 721 ads → 312 unique visuals
05f6812  Per-asset ranking inside cluster cards with delta-vs-median
5e1677f  Cluster signals: 26 creative+targeting dims, ranked table with strength bars
046d142  Clusters union-find: 511 → 635 clustered, variant labels, why-winner analysis
d673a81  Remote video playback via GitHub raw URLs (Railway payload 52 MB)
d1afd01  Make creative_breakdown the default dashboard (replaced old index.html)
e27b843  Video playback: fetched 153 missing MP4s, inline player on video ads
699f7bc  Reproduce: include solo ads (unclustered), show count selector, $50 min
```

## Files in working dir
- **Dashboards**: `public/index.html`, `public/creative_breakdown.html` (identical), same in `public-lite/`
- **Builders**: `build_breakdown.py` · `enrich_creative.py` · `dedup_assets.py` · `merge_all.py` · `analyze.py` · `make_medium_thumbs.py`
- **Pullers**: `pull.py` · `pull_tc1_tc4.py` · `pull_tc1_assets.py` · `pull_videos_missing.py` · `pull_ads_retry.py`
- **Data**: `data/merged.json` · `data/analysis.json` · `data/creative_enriched.json` · `data/asset_groups.json`
- **Assets**: `thumbnails/` (6.6 MB) · `thumbnails_med/` (42 MB) · `fullres/` (318 MB, local) · `videos/` (113 MB, 77 files)
