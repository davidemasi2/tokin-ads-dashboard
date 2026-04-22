# Tokin Ads Dashboard — Handoff (2026-04-22, 12:58 MDT)

## Live URLs
- **Dashboard**: https://tokin-ads-dashboard-production.up.railway.app
- **Creative Breakdown**: https://tokin-ads-dashboard-production.up.railway.app/creative_breakdown.html
- **GitHub repo** (public): https://github.com/davidemasi2/tokin-ads-dashboard
- **Skill tarball**: https://github.com/davidemasi2/tokin-ads-dashboard/raw/main/tokin-ads-advisor.tar.gz
- **Install one-liner**: `curl -fsSL https://github.com/davidemasi2/tokin-ads-dashboard/raw/main/tokin-ads-advisor.tar.gz | tar -xzf - -C /tmp && bash /tmp/tokin-ads-advisor/install.sh`

## Dataset
- 721 ads across TC1/TC2/TC3 · $356,556 spend · 2.23× ROAS · 10,675 purchases
- 97 clusters · 312 unique visuals (pHash deduped) · 166 compliance-flagged
- Shopify: 25,571 orders · $934K chews rev (12mo) · $194K merch rev

## Skills installed
- **tokin-ads-advisor** — ad intelligence, bundled data, query helper
- **tokin-jew-db** — live Shopify/Klaviyo DB

## Notion pages
- **Internal Tools Guide** (`34a26136-b372-8187-b7eb-c53325bf1630`) — updated to 4 tools: Command Center · Claude DB Skill · Claude Ads Advisor · Ads Dashboard
- **Paid Media Plan** — **PENDING** (see below for final spec)

---

# 🎯 PAID MEDIA PLAN — Final decision snapshot

## Context
- Onboarding new media buyer → needs safe baseline to start
- Past Passover (Apr 9) and past 4/20 → entering May-Aug Jewish holiday desert
- **Cookies and gelt inventory low** → must shelve gelt/cookie-dependent plays
- Goal: rebuild channel with graduated-risk campaigns, chews LTV is 40% higher than merch ($116 vs $82) but faces 28% compliance-flag rate — so merch is ToFu and chews comes second

## Active 5 campaigns (deploy now)

### A. Shabbat Summer — 🟢 LOW RISK
- **Concept**: Weekly Shabbat ritual items (Kiddush Cup · The Mezazah · Challah Pipe)
- **Hero**: Ad `120236100453450484` "Kiddush Cup (sqr) V5" / "Sip it & Rip It 🍷" — image · **6.04× ROAS** · $917 spend · $17 CPP · 2.28% CTR · 54 purchases
- **Thumb URL**: https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_e2ec163176c5.jpg
- **Backup**: Ad `120234591667130484` V2 — 2.54× · $4K spend · $28 CPP
- **LP**: tokinjew.com/collections/glassware
- **Targeting**: LAL 1% All Website Visitors 180d
- **Budget**: $100/day, 5-ad rotation
- **Expected**: 2.2–2.5× ROAS · $30–40 CPP · steady baseline

### D. Kosher Closet Summer — 🟢 LOW RISK
- **Concept**: Apparel ToFu → post-purchase 20% chews code
- **Hero**: Ad `120235840343690484` "guiltypleasure.2" — video · **4.80× ROAS** · $418 spend · $17 CPP · 5.19% CTR (portfolio-leading CTR)
- **Thumb URL**: https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails/120235840343690484_20bc4d3065.jpg
- **Products (by 2026 order volume)**: Mensch Hat (420/yr) · L'Chaim Tie Dye T-Shirt (415) · One Fish Two Fish T-Shirt (400) · Let's Get Chai T-Shirt (387)
- **Summer aesthetic**: tie-dye, camp nostalgia, BBQ/festival scenes
- **LP**: tokinjew.com/collections/tokin-chews-merch + post-purchase redirect to tokinjewflower.com/kosher-tokin20
- **Budget**: $150/day
- **Expected**: 2.1–2.4× ROAS · $30–40 CPP · 12.5% chews crossover · LTV-ROAS ~3.5×

### F. Pipes & Grinders — 🟢 LOW-MED RISK
- **Concept**: Jewish food-pun paraphernalia as "novelty gifts" (NOT functional gear)
- **Products**: Challah Pipe · Pickle Pipe · Bagel & Lox Grinder · Shofar Pipe · Dreidel Grinder (all appear in summer top-sellers $3–5K each)
- **Evidence**: 33 clean paraphernalia ads at 2.25× ROAS on $12K
- **Copy discipline**: "novelty/collectible/gift/kitchen-meets-kosher" ✅ · never "smoke/hit/bowl/session" ❌
- **Mitigation**: separate Page (`@tokinjew-kitchen` or similar) to isolate if flagged
- **Budget**: $100/day
- **Expected**: 2.0–2.4× ROAS · $30–45 CPP · 12.5% crossover

### C. Daytime/Nighttime Chai Routine — 🟡 MEDIUM RISK
- **Concept**: Functional chews as summer daily routine — replaces lost cookies/gelt volume
- **Hero**: Ad `120239040920820484` "Your New Daytime Chai 👉🏼" — **2.90× ROAS** on $2K · $36 CPP
- **Thumb URL**: https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_9ca11ea08e18.jpg
- **Backups**: `120227491006930484` "Mitzvah-Grade Chai" 2.79× · `120214902880040484` "Let's Get Chai" 2.74×
- **Product matrix**:
  - Morning → Apple-Energy & Focus / Apple THCV ($9K summer rev)
  - Afternoon → Watermelon High Dose ($26K summer rev — top seller)
  - Evening → Passionfruit Guava / Mango Peach
  - Night → Grape-Sleep & Relax ($11K summer rev) / Grape CBN
- **Copy discipline**: "chai" + time-context only · NEVER "relief/anxiety/sleep aid/pain/high/stoned"
- **Budget**: $150-300/day scalable
- **Expected**: 2.3–2.8× ROAS · $35–45 CPP · primary volume engine May-Aug

### E. Which Tokin' Jew Are You? Quiz — 🔴 HIGH RISK
- **Concept**: Interactive archetype quiz → product recommendation → email capture → chews offer
- **Proof**: Ad `120239611228270484` "Mix, Match, & Get Chai" (COMPLIANT) — **3.64× ROAS** · $1.5K · $31 CPP
- **Thumb URL**: https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_aa235400dc5a.jpg
- **Archetypes**: The Rabbi (Sleep & Relax) · The Bubbe (variety pack) · The Mensch (Tokin' Jays) · The Schlimazel (Watermelon High Dose)
- **Infrastructure**: NEW Business Manager + new Page + jump page on `tokinjewquiz.com`
- **Quiz stack**: Typeform or native HTML → email capture → Klaviyo flow → $10 off first chews order
- **Budget**: $50/day × 14 days · scale if CAC < $30
- **Expected**: 2.5–4.0× ROAS · 40-60% email capture on completers · best-case blended LTV-ROAS ~5×
- **Setup time**: 10-14 days (new BM + jump page) — can build in parallel with A/D/F/C execution

## Deployment — "Merch Wall First" (Option 2)

| Week | Launch | Main BM budget | New BM budget |
|---|---|---:|---:|
| W1 | A + D + F | $350/day | — |
| W2 | Add C | $550/day | start BM/jump page build |
| W3 | All 4 live | $650/day | infra build continues |
| W4 | Add E on new BM | $650/day | $50/day |
| W5+ | Scale winners · kill losers | $800–1,200/day | $50–200/day |

**30-day projection** (this deployment): ~$17K spend · 2.4× blended ROAS · $41K revenue · ~650 customers acquired · ~80 merch→chews crossovers banked for future LTV

## Shelved (revive on trigger)

| ID | Campaign | Revive trigger | Evidence |
|---|---|---|---|
| G | Gifting Funnel (Gelt) | Gelt restocked → ramp Oct for Hanukkah | 2.92× ROAS · $27K spend · #1 crossover product ($11.8K from merch-first buyers) |
| H | Hamantaschen / Purim Cookies | Cookies restocked → Feb-Mar 2027 (Purim) | Hero `120219109515800484` hit **7.04× ROAS** on $415 — needs scaling |

## Seasonal calendar

| ID | Campaign | Window | Evidence |
|---|---|---|---|
| I | Passover Bundle (Kosher for Passover) | **Feb-Apr 2027** | Cluster C001 · 67 variants · **3.28× ROAS** (best category) |
| J | 4/20 Kosher | **Apr 2027** (just passed) | 66 ads · 2.60× · 0 flags |

## Non-negotiables for new media buyer
1. Never use: THC, CBD, high, stoned, weed, relief, cure, medicine
2. Never link ads directly to gummy PDPs on new BM — always via jump page
3. Keep main BM's TC1 account health perfect — test only on new BM
4. Naming convention: `[Brand]_[Concept]_[Angle]_[Variant]` so dashboard clusters track them

---

# PENDING next session

## Build Notion "Paid Media Plan" page
- **Parent**: Tokin' Home (`06b26136-b372-83ae-b247-81e3464c837a`)
- **Top of page**: Links to all 4 tools (Command Center, Claude DB Skill, Claude Ads Advisor, Ads Dashboard)
- **Sections**:
  1. Context + why this plan
  2. Evidence tables (bucket ROAS, LTV by first-brand, crossover rates, summer seller rankings)
  3. Campaign A full brief + hero thumbnail (render inline from GitHub raw URL)
  4. Campaign D full brief + hero thumbnail
  5. Campaign F full brief + hero thumbnail
  6. Campaign C full brief + hero thumbnail
  7. Campaign E full brief + jump page spec
  8. Deployment calendar (Option 2 Merch Wall First)
  9. 30/90-day projected economics
  10. Shelved + Seasonal table (revive triggers)
  11. Non-negotiables

## Use these exact image URLs (medium-res 500×500, public GitHub raw)
| Ad | URL |
|---|---|
| A · Kiddush V5 (hero) | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_e2ec163176c5.jpg |
| A · Kiddush V2 | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_fb1766ba75e1.jpg |
| D · guiltypleasure video | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails/120235840343690484_20bc4d3065.jpg |
| D · Gelt that gets you chai V2 | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_7e754b6be9c1.jpg |
| C · Your New Daytime Chai | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_9ca11ea08e18.jpg |
| C · Mitzvah-Grade Chai | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails/120227491006930484_54b52dc3de.jpg |
| C · Let's Get Chai | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_36673b59f385.jpg |
| E · Mix Match Get Chai (quiz) | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_aa235400dc5a.jpg |
| E · Worth Your Two Zuzim | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails/120220249587130484_10732fe177.jpg |
| G · Gelt champ (shelved ref) | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_f45b3b26320f.jpg |
| H · Hamantaschen (shelved ref) | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_bc03ec5ddf3e.jpg |
| I · K4P Passover (seasonal ref) | https://raw.githubusercontent.com/davidemasi2/tokin-ads-dashboard/main/thumbnails_med/adimg_1449383908993328_ee2ab9fb5028.jpg |

## User decisions pending
- Green-light Option 2 "Merch Wall First" deployment sequence?
- Launch creative copy drafts for A/D/F/C?
- Spec out Campaign E jump page (tokinjewquiz.com) + archetype-to-product mapping?
- Draft the post-purchase thank-you redirect spec for D?

---

## Recent commits
```
081305b  Handoff update: Paid Media Plan deliverable documented
a881c3c  Ship tokin-ads-advisor skill tarball (standalone, 145KB)
4d62d23  Add query.py helper for tokin-ads-advisor skill
e044bee  Update HANDOFF: clusters · asset dedup · variant tables · CPP sort
6ab67b5  CPP + full metric sort coverage on Tiers/Clusters/Compliance/All-ads
8e4e9d3  Variant ranking table in Clusters+Reproduce · LP populated (501/721)
5012742  Reproduce rework: 220px hero · top-3 variants table · asset ranking
3b0e503  Cluster sort: Winner-only options (ROAS/CPP/CTR/CPM/purchases/spend)
9e510e0  Perceptual-hash asset dedup: 721 ads → 312 unique visuals
05f6812  Per-asset ranking inside cluster cards with delta-vs-median
```
