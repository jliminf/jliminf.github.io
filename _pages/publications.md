---
layout: modern
title: Publications
permalink: /publications/
description: "Research in multi-agent planning, efficient search, and optimal control."
---
<div class="filters" role="group" aria-label="Filter publications"><button data-filter="all" aria-pressed="true">All publications</button><button data-filter="journal" aria-pressed="false">Journal articles</button><button data-filter="conference" aria-pressed="false">Conference papers</button></div>
<p id="filter-status" class="filter-status" role="status" aria-live="polite">8 publications shown</p>
{% for paper in site.data.papers %}{% include paper-row.html %}{% endfor %}
<p class="note">For the complete, up-to-date publication record, visit <a href="https://scholar.google.com/citations?user=q5Ap8eAAAAAJ">Google Scholar <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a>.</p>
