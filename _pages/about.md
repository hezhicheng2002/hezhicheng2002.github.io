---
permalink: /
layout: single
title: "Hi, I'm Zhicheng He（何智成）"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a first-year graduate student in the Department of Biomedical Engineering at the National University of Singapore. I completed my undergraduate degree in Computer Science at Beijing Jiaotong University. My research interests include medical image analysis and multi-modal large language models.

I am very fortunate to be advised by [Prof. Xiaoqing Lv](https://ieeexplore.ieee.org/author/37599114400) of [Wangxuan Institute of Computer Technology](https://www.icst.pku.edu.cn/), Peking University. Meanwhile, I am honored to be recommended by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang) of [Ren Lab](http://www.labren.org/mm/) from The Chinese University of Hong Kong. Moreover, I am thrilled to be instructed by [Prof. Tengfei Ma](https://ai.stonybrook.edu/people/faculty/TengfeiMa) of Department of Biomedical Informatics from Stony Brook University, who also agreed to be my recommender.

News
------
I'm happy to join [Dr. Yueming Jin](https://yuemingjin.github.io/)'s team in 2025 as a MEng student.

Publications
------
{% assign publications = site.publications | sort: 'date' | reverse %}
{% if publications and publications.size > 0 %}
<ul>
{% for item in publications %}
  <li>
    <strong>{{ item.title }}</strong><br>
    {{ item.citation }}<br>
    {% if item.paperurl %}<a href="{{ item.paperurl }}">Paper</a>{% endif %}
    {% if item.slidesurl %} | <a href="{{ item.slidesurl }}">Slides</a>{% endif %}
  </li>
{% endfor %}
</ul>
<p><a href="/publications/">View all publications →</a></p>
{% else %}
<p>No publications yet.</p>
{% endif %}

Latest Notes
------
{% assign latest_notes = site.notes | sort: 'date' | reverse | slice: 0,5 %}
{% if latest_notes and latest_notes.size > 0 %}
<ul>
{% for item in latest_notes %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a> <small>({{ item.date | date: "%Y-%m-%d" }})</small></li>
{% endfor %}
</ul>
<p><a href="/notes/">View all notes →</a></p>
{% else %}
<p>No notes published yet.</p>
{% endif %}
