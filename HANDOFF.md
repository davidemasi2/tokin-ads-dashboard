# Tokin Ads — Handoff (2026-04-22, 17:45 MDT)

## Session summary

Built the **Summer 2026 Paid Media Plan** from scratch with data-verified heroes, rebuilt the 4-campaign brief around verified creative (visually inspected), refreshed the Meta token + pulled all accessible video thumbs, and pushed the full 500 MB creative library to Google Drive as a public asset.

## Live URLs

| Asset | URL |
| --- | --- |
| Ads Dashboard (Railway) | https://tokin-ads-dashboard-production.up.railway.app |
| Creative Breakdown | https://tokin-ads-dashboard-production.up.railway.app/creative_breakdown.html |
| GitHub repo (public) | https://github.com/davidemasi2/tokin-ads-dashboard |
| Skill tarball | https://github.com/davidemasi2/tokin-ads-dashboard/raw/main/tokin-ads-advisor.tar.gz |
| **Creative Library (Google Drive, public)** | https://drive.google.com/drive/folders/1DfDDbQ8hOyvcaktNXRaoSNtXYZrtWO2s |

## Google Drive Creative Library (NEW)

- **Root folder**: `Tokin Ads Creative Library` (id `1DfDDbQ8hOyvcaktNXRaoSNtXYZrtWO2s`) — public, anyone with link can view
- **fullres/** — 1,136 images · 344 MB · folder id `1Xm_z-auJqSoVfO6B3pmK9CZKdvEdHNoT`
- **videos/** — 77 MP4s · 113 MB · folder id `1P4w_AA2JuG8TG5F24zGIPXxEfVWfbZud`
- **thumbnails_med/** — 989 thumbs · 42 MB · folder id `1_yVe0sWsrh2BUeSxJjfoaEnoXG1zQ5is`
- **Upload script**: `upload_to_drive.py` — parallel multipart uploads via Drive REST API, OAuth token param

## Dataset

- 721 ads across TC1/TC2/TC3 · $356,556 spend · 2.23× ROAS · 10,675 purchases
- 97 clusters · 312 unique visuals (pHash deduped) · 166 compliance-flagged
- Shopify: 25,571 orders · $934K chews rev (12mo) · $194K merch rev

## Notion pages

| Page | ID | Status |
| --- | --- | --- |
| **📣 Paid Media Plan — Summer 2026** (live) | `34a26136-b372-818d-881f-cefa231532ca` | Current source of truth |
| 🛠️ Internal Tools Guide | `34a26136-b372-8187-b7eb-c53325bf1630` | Updated with Creative Library link |
| Tokin' Home (parent) | `06b26136-b372-83ae-b247-81e3464c837a` | Unchanged |
| [ARCHIVED] Paid Media Plan — 2026 Summer | `32726136-b372-811b-b1c9-c4871caa9a03` | Superseded, redirect banner |

## Skills installed

- **tokin-ads-advisor** — ad intelligence, bundled data, query helper
- **tokin-jew-db** — live Shopify/Klaviyo DB

---

# 🎯 PAID MEDIA PLAN — Locked Spec

## Context

- Past Passover (Apr 9) and past 4/20 → entering May-Aug Jewish holiday desert until Rosh Hashanah (Sept)
- **Cookies and gelt inventory LOW** → shelve gelt/cookie-dependent plays
- Goal: onboard Camilla on a safe baseline while banking chews LTV via merch crossover
- LTV: chews-first $116 · merch-first $82 (chews +40% but 28% flag rate vs merch 0%)

## 4 Active Campaigns

### 🟢 A · Shabbat Kiddush Cup — LOW RISK · $100/day · BM1 merch-clean

- **Hero #1**: Kiddush V5 `120236100453450484` · 6.04× ROAS · $917 · $17 CPP · 2.28% CTR
- **Hero #2**: Kiddush V2 `120234591667130484` · 2.54× ROAS · $4K · 142 purchases (scale-volume)
- **Hero #3**: Kiddush V8 `120236100453440484` · 1.79× · ⚠️ cannabis leaves in visual → BM2 weed-test only
- **LP**: tokinjew.com/collections/glassware/products/kiddush-cup-pipe
- **Compliance**: 🟢 all 3 clean, 0 flags

### 🟡 B · Chews (Classic + Functional) — MED RISK · $200/day · BM3 weed-production

- **Hero #1 Guava Nagila** `120217536466960484` · 2.16× on $9.3K · 242 purchases
- **Hero #2 Watermelon Sugar Chai** `120217256695430484` · 2.39× on $3.5K · top-seller SKU
- **Hero #3 Let's Get Chai (Static Assorted)** `120214902880040484` · 2.74× on $1.3K
- **Hero #4 Pom B-roll VIDEO** `120227491006930484` · 2.79× on $2.6K · video thumb available, MP4 blocked by IG Reel permissions
- **Backup** Ran-It-By-Rabbi `120235374415200484` · **REQUIRES copy scrub** — body contains "10mg TH" → change to "10mg per piece"
- **Compliance**: 🟡 bucket flag rate 28% — strictest copy discipline applies

### 🧩 C · Clean Merch → Weed Upsell — TEST · $75/day · BM1 → BM2 crossover

- **No proven hero** — zero apparel ads ever run above $100 spend historically
- Creative brief in Notion §5: 3 static + 1 UGC video featuring Mensch Hat (420/yr), L'Chaim Tie Dye (415/yr), One Fish Two Fish (400/yr)
- Post-purchase Klaviyo flow → 20% flower code → route to tokinjewflower.com
- Graduation bar: 2.0× ROAS at $500 spend → scale to $150/day

### 🧩 D · Paraphernalia Novelty — TEST · $75/day · BM2 weed-test

- **Hero #1** Burning Bush Dreidel Pipe `120233960513670484` · 1.36× on $165 · only proven paraph creative
- **Hero #2** Shabbat Lifestyle (NEW, to be shot) — repurposed from K4P Citrus 5.63× ROAS winner on $10K. Shoot Kiddush Cup Pipe on Shabbat table (NO matzah, NO seder-specific props) for evergreen year-round use. 3 copy variants in Notion: "Elevate Your Shabbat" · "Set The Holy Table" · "A Cup For Every Kiddush"
- Creative briefs queued: Pickle Pipe · Challah Pipe (video exists, 3.80% CTR no purchases) · Bagel & Lox Grinder · Shofar Pipe (Sept)
- Compliance: separate Page `@tokinjew-kitchen` or `@tokinjew-novelty` required

## 3-BM Architecture

| BM | Name | Page | Campaigns | Budget |
| --- | --- | --- | --- | --- |
| 🛡️ BM1 | `merch-clean` | `@tokinjew` (main) | A1 V5 · A2 V2 · C Merch Test | $150–200 |
| 🧪 BM2 | `weed-test` | `@tokinjew-kitchen` (new) | A3 V8 · D1 Burning Bush · D2 Shabbat Lifestyle · Paraph tests · Quiz funnel | $100–150 |
| 💰 BM3 | `weed-production` | `@tokinchews` (existing) | B1-B4 chews rotation · graduated winners | $150–300 scalable |

**Rules**: Never cross-contaminate. Winners graduate BM2 → BM3 only after 14d stable + 0 flags + $1K at 2.0×.

## Deployment Schedule

| Week | Launch | Main BM1 | Test BM2 | Prod BM3 | Total |
| --- | --- | --- | --- | --- | --- |
| W1 | A V5/V2 + B chews rotation | $100 | — | $200 | $300 |
| W2 | + A3 V8 on BM2 + D1 Burning Bush | $100 | $100 | $200 | $400 |
| W3 | Commission C creative | $100 | $100 | $200 | $400 |
| W4 | + C merch test + D2 Shabbat Lifestyle | $150 | $150 | $200 | $500 |
| W5+ | Scale winners · kill losers | $200 | $150 | $300 | $650–1,200 |

**30-day projection**: ~$13.5K spend · 2.3× blended ROAS · ~$31K revenue · ~450 new customers

## Compliance playbook

| Category | Rule |
| --- | --- |
| Banned vocab | THC · CBD · high · stoned · weed · relief · cure · medicine · anxiety · pain · sleep aid |
| "TH" abbreviation | Never use — Meta pattern-matches as THC |
| Images | No cannabis leaves on BM1/BM3 |
| Paraphernalia framing | "novelty · collectible · gift · kitchen-meets-kosher" — never "smoke/hit/bowl/session" |
| Naming | `[Brand]_[Concept]_[Angle]_[Variant]` |

## Shelved (inventory-gated)

- **Gelty Pleasure (Gelt)** — 2.92× on $27K / 922 purchases · revive October for Hanukkah
- **Hamantaschen Cookies** — 2.03× on $3.8K · revive Feb-Mar 2027 for Purim

## Seasonal Calendar

- **K4P Passover** — 5.63× on $10K / 618 purchases · Feb-Apr 2027
- **4/20 Kosher Jays LTO** — 6.25× on $370 · April 2027
- **Hanukkah Bundle** — 2.27× on $7.6K · December

---

# Open Decisions (for next session)

| # | Decision | Owner | Urgency |
| --- | --- | --- | --- |
| 1 | Approve BM role assignments (TC1/TC2/TC3/TC4 → BM1/BM2/BM3) | Davide | Before W1 |
| 2 | Commission C Merch creative (~$1-2K + 2-week lead) | Davide | Before W2 |
| 3 | Commission D2 Shabbat Lifestyle shoot ($800-1.5K) | Davide | Before W4 |
| 4 | Copy-scrub Ran-It-By-Rabbi ("TH" → "per piece") | Camilla | Before B relaunch |
| 5 | Kiddush V8 on BM2 only or pull? (cannabis leaves visual) | Davide | Before W2 |
| 6 | Fund Pickle Pipe + Challah Pipe tests at $30/day? | Davide | Before W4 |
| 7 | O1 Gelt Waitlist pre-build — commit now or wait Oct? | Davide | Anytime |
| 8 | O2 Gummy subscription-first — add as B5 variant or parallel? | Davide + Camilla | Before W3 |

---

# Known Blockers / Blind Spots

- **87 hero videos are Instagram Reels** — Graph API does not return `source` URLs for IG-originated content. Only `permalink_url` + thumbnails. 77 MP4s we have in `videos/` are from older TC1 direct-upload flights. Workaround: link IG permalinks in brief, use 1080px thumbnails as inline previews.
- **Challah Pipe video `2160373734372228`** returns OAuth error `"Application does not have permission for this action"` — the Page it was posted from hasn't granted our app asset-level access. Requires BM admin action.
- **No proven clean merch apparel heroes** in dataset (spend > $100) — C must be scratch-built.
- **No proven paraphernalia heroes above $165 spend** — D must rely on Burning Bush + new creative.
- **Meta token lifespan ~2 hours** — every new session requires refresh via developers.facebook.com/tools/explorer
- **Google Drive access token (OAuth Playground) expires 1 hour** — re-issue via oauthplayground if bulk re-upload is needed

---

# Recent commits (GitHub public repo)

```
02e320f  Refresh: add 213 new video thumbnails + missing images from Meta pull
b4da427  Handoff update: Paid Media Plan deliverable documented (prior handoff)
a881c3c  Ship tokin-ads-advisor skill tarball (standalone, 145KB)
```

---

# Scripts updated this session

- `upload_to_drive.py` (NEW) — parallel Drive upload via OAuth access token
- `pull_videos.py` · `pull_videos_missing.py` · `pull_tc1_assets.py` · `pull_tc1_tc4.py` · `pull_ads_retry.py` · `pullall.py` · `pull.py` — all refreshed with 2026-04-22 Meta token

## Non-negotiables for new media buyer (Camilla)

1. Banned vocab: THC · CBD · high · stoned · weed · relief · cure · medicine
2. No direct gummy-PDP links on new BM — always via jump page
3. Main BM (TC1) health is sacred — test on BM2 only
4. Naming convention: `[Brand]_[Concept]_[Angle]_[Variant]`
5. Paraphernalia = "novelty/gift" framing, never functional
6. Weekly true-ROAS review: `(Rev − COGS − Spend − Fees) / Spend` · target >2.0 true
7. Separate Page for high-risk paraphernalia tests
8. Every hero gets a video variant test within 14 days

---

**Source of truth**: [📣 Paid Media Plan — Summer 2026 (Notion)](https://www.notion.so/34a26136b372818d881fcefa231532ca) · **Last updated**: 2026-04-22 17:45 MDT
