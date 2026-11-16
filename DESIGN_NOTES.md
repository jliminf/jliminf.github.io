# Portfolio design system

## Shared templates

- `_layouts/modern.html`: shared navigation, page heading, content container, and footer.
- `_includes/section-heading.html`: section heading with optional label and related link. Parameters: `title`, `label`, `url`, `link_text`.
- `_includes/paper-row.html`: a publication row using the shared card-title and metadata styles.
- `_includes/portrait.html`: a compact portrait with the same framing on every screen.
- `_includes/experience.html` and `_includes/education.html`: content shared between the experience page and printable résumé.

## Typography

`assets/css/tokens.css` is the single source for typography, colors, and spacing. `modern.css` maps these tokens to semantic elements and component roles. Use the existing roles when adding pages; do not add local numeric font sizes or inline font overrides.

| Role | Desktop | Mobile | Use |
| --- | --- | --- | --- |
| Page title | 36px | 32px | All h1 headings, including the homepage |
| Section title | 26px | 26px | Main h2 headings |
| Card title | 20px | 20px | h3, publication titles, project-card titles |
| Body | 16px | 16px | Introductory and descriptive prose, lists |
| Metadata / controls | 14px | 14px | Labels, dates, tags, navigation, buttons, footer |

One system sans-serif stack is used throughout. Body weight is 400, headings 500, and emphasis 600. Mobile changes the page-title token once; individual components do not define their own responsive text sizes. Print sizes are centralized in the same token file.

## Color and imagery

White background, dark-blue text and controls, muted slate secondary text, and light blue-gray borders. The header uses the name as plain text, without an initials logo.

`images/jaein-lim-portrait.jpg` is the supplied photograph, preserved unchanged. The portrait component uses a display-only crop to show the face and upper torso. It is 220px wide on desktop and 180px on mobile. Adjust framing in `.portrait-frame`, rather than altering the source photo.

## Content and maintenance

Primary content source: `Jaein-Lim-Resume-Refined(1).pdf`, September 26, 2026 revision. Earlier publications and project URLs are preserved. The web résumé is a printable adaptation.

Edit `_data/papers.yml` for publications. Main content lives in `_pages/` and the shared content includes. GitHub Pages continues to build Jekyll. The `Check site` workflow uses GitHub's Pages build action and validates local links on the primary pages.
