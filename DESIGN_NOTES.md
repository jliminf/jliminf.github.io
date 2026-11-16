# Portfolio refresh

This branch updates the existing GitHub Pages/Jekyll site. Existing project and publication detail URLs are retained. Primary pages and legacy detail pages use `_layouts/modern.html` and `assets/css/modern.css`.

## Content

Primary source: `Jaein-Lim-Resume-Refined(1).pdf`, latest available revision dated September 26, 2026. Publications also retain earlier papers already on the site. Acceptance status is retained from that résumé rather than inferred. Contact, work history, education, and role descriptions are sourced from the résumé. The public web résumé is a concise adaptation; it excludes phone number and clearance information.

The LinkedIn photo could not be retrieved (HTTP 999). The draft retains `images/jliminf.jpeg` from the original repository; replace that file with the requested LinkedIn portrait when supplied. It is not represented as a newly retrieved LinkedIn image.

The original résumé PDF transfer was unavailable. `/cv/` is an updated printable HTML résumé with a Print / Save as PDF action.

## Editing and preview

- Main content: `_pages/about.md`, `_pages/projects.md`, `_includes/experience.html`, `_includes/education.html`.
- Publications: `_data/papers.yml`.
- Run `bundle install` then `bundle exec jekyll serve` for the canonical preview.
- GitHub Pages continues to build the repository using Jekyll. No hosting migration is required.
- The included CI workflow builds Jekyll and verifies internal links on pull requests and pushes.

## Accessibility

Responsive navigation, skip link, visible keyboard focus, descriptive image alternatives, accessible publication filters, reduced-motion support, and print styling are included. Core content and links work without JavaScript.

## Validation completed

- Desktop and 390-pixel mobile layout inspected in a browser using a static Liquid/Markdown preview.
- Journal publication filtering and mobile navigation tested successfully.
- Internal links and assets on seven primary pages checked successfully.
- JavaScript syntax and Git whitespace checks passed.
- The canonical GitHub Pages Jekyll build passed in GitHub Actions. The check workflow uses the same Pages build action before validating links, avoiding the legacy Mac-only Bundler lockfile.

## Apply to GitHub Pages

Copy the contents of this source directory into your existing `jliminf.github.io` checkout, including `.github`, commit, and push to your publishing branch. Keep your existing GitHub Pages settings. Review the build check and Pages deployment before considering the live update complete.
