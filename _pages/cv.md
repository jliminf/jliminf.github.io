---
layout: modern
title: Résumé
permalink: /cv/
description: "Jaein Lim, Ph.D. · Autonomy, robotics, and AI mission planning."
---
<div class="resume-tools"><a class="button" href="{{ "/files/Jaein-Lim-Resume.pdf" | relative_url }}" download="Jaein-Lim-Resume.pdf">Download résumé (PDF) <svg class="out-arrow" aria-hidden="true" viewBox="0 0 16 16" fill="none"><path d="M3 13 13 3M3 3h10v10" stroke="currentColor" stroke-width="1.3"/></svg></a></div>
<p><a href="mailto:jliminf@gmail.com">jliminf@gmail.com</a> · Cambridge, MA · <a href="https://www.linkedin.com/in/jaein-lim-9a5135236/">LinkedIn</a> · <a href="https://scholar.google.com/citations?user=q5Ap8eAAAAAJ">Google Scholar</a></p>
<p>Autonomy engineer and researcher with a Ph.D. in aerospace engineering and experience advancing planning algorithms from research through simulation, vehicle integration, and flight testing. Leads work in decentralized multi-agent coordination and AI mission planning, with additional experience in undersea and spacecraft autonomy and flight-software verification.</p>
{% include experience.html %}
{% include education.html %}
<h2>Technical skills</h2>
<div class="skill-list"><div><h3>Programming & robotics</h3><p>C++, Python, ROS 2, MATLAB/Simulink, Git, Docker</p></div><div><h3>AI & mission planning</h3><p>vLLM, graph-RAG, MCP, agent execution harnesses, vehicle API integration</p></div><div><h3>Planning & control</h3><p>Multi-agent pathfinding, decentralized coordination, lazy and incremental search, trajectory optimization, optimal control</p></div><div><h3>Simulation & verification</h3><p>GitLab CI, AirSim, ArduPilot SITL, PX4 SITL/HITL, processor-in-the-loop testing</p></div></div>
<h2>Selected publications</h2>
{% for paper in site.data.papers limit:4 %}{% include paper-row.html %}{% endfor %}
