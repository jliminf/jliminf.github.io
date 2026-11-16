---
layout: modern
home: true
title: "Autonomy & Robotics"
permalink: /
redirect_from: [/about/, /about.html]
---
<section class="hero">
  <div>
    <p class="eyebrow">Autonomy · Robotics · AI mission planning</p>
    <h1>Jaein Lim, Ph.D.</h1>
    <p class="intro">I’m an autonomy engineer and researcher at Draper. I develop algorithms that help robots plan, coordinate, and act—and bring them from research to simulation, vehicle integration, and flight testing.</p>
    <div class="hero-actions"><a class="button" href="/projects/">Explore my work <span aria-hidden="true"><svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></span></a><a class="text-link" href="/cv/">View résumé <span aria-hidden="true"><svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></span></a></div>
    <p class="hero-aside"><strong>Senior Member of Technical Staff, Draper</strong><br>Autonomy and Real-time Planning · Cambridge, MA</p>
  </div>
  {% include portrait.html %}
</section>
<div class="credibility" aria-label="Background"><div><strong>Draper</strong><span>Autonomy & real-time planning<br>September 2022–present</span></div><div><strong>Georgia Tech</strong><span>Ph.D. in Aerospace Engineering<br>August 2022</span></div></div>
<section class="section">
 {% include section-heading.html label="01 / Focus" title="Research & engineering" %}
 <div class="focus-grid">
  <article class="focus-item"><p class="focus-number">01 — MULTI-AGENT SYSTEMS</p><h3>Multi-agent coordination</h3><p>Decentralized path deconfliction, multi-agent pathfinding, and task allocation. Connecting theoretical guarantees with coordination on real vehicles.</p><div class="tags"><span>MAPLE</span><span>CBS-Budget</span><span>Multi-robot planning</span></div></article>
  <article class="focus-item"><p class="focus-number">02 — AI MISSION PLANNING</p><h3>AI mission planning</h3><p>Context-aware AI agents that reason about mission objectives and vehicle capabilities, with execution tools and interfaces to autonomy systems.</p><div class="tags"><span>vLLM</span><span>Graph-RAG</span><span>MCP</span></div></article>
  <article class="focus-item"><p class="focus-number">03 — AUTONOMY ENGINEERING</p><h3>Autonomy engineering</h3><p>Motion planning, controller interfaces, and automated testing across simulation and hardware. Experience spanning aerial, ground, undersea, and spacecraft autonomy.</p><div class="tags"><span>C++ / Python</span><span>ROS 2</span><span>SITL / HITL</span></div></article>
 </div>
</section>
<section class="section">
 {% include section-heading.html label="02 / A closer look" title="Lazy incremental search" url="/projects/" link_text="All work" %}
 <article class="work-feature"><div><p class="eyebrow">Motion planning / Heuristic search</p><h3>Efficient replanning</h3><p>My research combines lazy evaluation with incremental search: reuse what a planner already knows, and avoid expensive edge evaluations that do not help find a solution.</p><p>The result is a family of efficient replanning algorithms, including methods with bounded-suboptimality guarantees.</p><a class="text-link" href="/projects/lis">Explore lazy incremental search <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></div><div><div class="research-image"><img src="/images/lis_pr2.png" alt="PR2 robot manipulation planning research visualization" loading="lazy"></div><p class="image-caption">RESEARCH VISUALIZATION · LAZY INCREMENTAL SEARCH</p></div></article>
</section>
<section class="section">
 {% include section-heading.html label="03 / Publications" title="Selected publications" url="/publications/" link_text="All publications" %}
 {% for paper in site.data.papers limit:4 %}{% include paper-row.html %}{% endfor %}
</section>
<section class="contact-band"><div><p class="eyebrow">Let’s connect</p><h2>Research and collaboration</h2><p>I’m happy to connect with researchers and engineers working in the field.</p></div><a class="button" href="mailto:jliminf@gmail.com">Get in touch <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></section>
