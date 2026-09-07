# DJOS Website

Public landing page for **DJOS — DJ Operating System**.

## Purpose

This repository is intentionally separate from the private/local DJOS application code. It can be deployed as a static site and expanded later into the full public DJOS website.

## Local preview

No build step is required.

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Cloudflare Pages

Deploy the repository as a static site:

- Framework preset: `None`
- Build command: leave empty
- Build output directory: `/`

The generated `*.pages.dev` URL can later be replaced or supplemented with a custom domain without rebuilding the website.

## Attribution

The public footer contains the required GetSongBPM backlink and also links to MusicBrainz.
