# Tokin' Chews Meta Ads Dashboard

Self-contained HTML dashboard of every Meta ad across the Tokin' Chews portfolio (Mar–Apr 2026).

**Live:** deployed on Railway. Just open the URL.

## What's here

- `index.html` — the dashboard (Ads / Creative Groups / Audiences / Analysis tabs)
- `fullres/` — half-res creative images (long edge 1024px)
- `thumbnails/` — 64px grid thumbnails
- `landing_pages/` — LP screenshots
- `videos/` — MP4 video ads

## Running locally

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploying on Railway

Railway auto-detects `Procfile` and runs `python3 -m http.server $PORT`. Push to `main` → auto-deploy.

## Updates

Heavy data-pull and analysis machinery lives in a private workspace. New dashboard snapshots get pushed here as the campaign evolves.
