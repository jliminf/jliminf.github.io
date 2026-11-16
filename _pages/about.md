---
layout: modern
home: true
title: "Autonomy & Robotics"
permalink: /
redirect_from: [/about/, /about.html]
---
<section class="hero">
  <div>
    <p class="eyebrow"><span class="status-dot"></span>Autonomy · Robotics · AI mission planning</p>
    <h1>Building autonomy<br>for the <em>real world.</em></h1>
    <p class="intro">I’m Jaein Lim, an autonomy engineer and researcher. I develop algorithms that help robots plan, coordinate, and act—and bring them from research to simulation, vehicle integration, and flight testing.</p>
    <div class="hero-actions"><a class="button" href="/projects/">Explore my work <span aria-hidden="true"><svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></span></a><a class="text-link" href="/cv/">View résumé <span aria-hidden="true"><svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></span></a></div>
    <p class="hero-aside"><strong>Senior Member of Technical Staff, Draper</strong><br>Autonomy and Real-time Planning · Cambridge, MA</p>
  </div>
  <figure class="portrait"><img src="/images/jliminf.jpeg" width="1200" height="1200" alt="Portrait of Jaein Lim" fetchpriority="high"><figcaption><span>JAEIN LIM, PH.D.</span><span>CAMBRIDGE, MA</span></figcaption></figure>
</section>
<div class="credibility" aria-label="Background and validation"><div><strong>Draper</strong><span>Autonomy & real-time planning<br>September 2022–present</span></div><div><strong>Georgia Tech</strong><span>Ph.D. in Aerospace Engineering<br>August 2022</span></div><div><strong>3 / 6</strong><span>Coordinated vehicles<br>Flight tests / simulation</span></div></div>
<section class="section">
 <div class="section-heading"><div><p class="eyebrow">01 / Research & engineering</p><h2>Planning. Coordination. Action.</h2></div></div>
 <div class="focus-grid">
  <article class="focus-item"><p class="focus-number">01 — MULTI-AGENT SYSTEMS</p><h3>Helping robots<br>work together.</h3><p>Decentralized path deconfliction, multi-agent pathfinding, and task allocation. Connecting theoretical guarantees with coordination on real vehicles.</p><div class="tags"><span>MAPLE</span><span>CBS-Budget</span><span>Multi-robot planning</span></div></article>
  <article class="focus-item"><p class="focus-number">02 — AI MISSION PLANNING</p><h3>From operator intent<br>to robot action.</h3><p>Context-aware AI agents that reason about mission objectives and vehicle capabilities, with execution tools and interfaces to autonomy systems.</p><div class="tags"><span>vLLM</span><span>Graph-RAG</span><span>MCP</span></div></article>
  <article class="focus-item"><p class="focus-number">03 — AUTONOMY ENGINEERING</p><h3>Algorithms that<br>leave the lab.</h3><p>Motion planning, controller interfaces, and automated testing across simulation and hardware. Experience spanning aerial, ground, undersea, and spacecraft autonomy.</p><div class="tags"><span>C++ / Python</span><span>ROS 2</span><span>SITL / HITL</span></div></article>
 </div>
</section>
<section class="section">
 <div class="section-heading"><div><p class="eyebrow">02 / A closer look</p><h2>Search smarter. Replan faster.</h2></div><a class="text-link" href="/projects/">All work <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></div>
 <article class="work-feature"><div><p class="eyebrow">Motion planning / Heuristic search</p><h3>Spend computation<br>where it matters.</h3><p>My research combines lazy evaluation with incremental search: reuse what a planner already knows, and avoid expensive edge evaluations that do not help find a solution.</p><p>The result is a family of efficient replanning algorithms, including methods with bounded-suboptimality guarantees.</p><a class="text-link" href="/projects/lis">Explore lazy incremental search <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></div><div><div class="research-image"><img src="/images/lis_pr2.png" alt="PR2 robot manipulation planning research visualization" loading="lazy"></div><p class="image-caption">RESEARCH VISUALIZATION · LAZY INCREMENTAL SEARCH</p></div></article>
</section>
<section class="section">
 <div class="section-heading"><div><p class="eyebrow">03 / Selected publications</p><h2>Ideas, in print.</h2></div><a class="text-link" href="/publications/">All publications <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></div>
 {% for paper in site.data.papers limit:4 %}{% include paper-row.html %}{% endfor %}
</section>
<section class="contact-band"><div><p class="eyebrow">Let’s connect</p><h2>Interested in autonomy<br>and multi-robot systems?</h2><p>I’m happy to connect with researchers and engineers working in the field.</p></div><a class="button" href="mailto:jliminf@gmail.com">Get in touch <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></section>
