---
permalink: /
layout: splash
title: "Hi, I'm Zhicheng He（何智成）"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a first-year graduate student in the Department of Biomedical Engineering at the National University of Singapore. I completed my undergraduate degree in Computer Science at Beijing Jiaotong University. My research interests include medical image analysis and multi-modal large language models.

I am very fortunate to be advised by [Prof. Xiaoqing Lv](https://ieeexplore.ieee.org/author/37599114400) of [Wangxuan Institute of Computer Technology](https://www.icst.pku.edu.cn/), Peking University. Meanwhile, I am honored to be recommended by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang) of [Ren Lab](http://www.labren.org/mm/) from The Chinese University of Hong Kong. Moreover, I am thrilled to be instructed by [Prof. Tengfei Ma](https://ai.stonybrook.edu/people/faculty/TengfeiMa) of Department of Biomedical Informatics from Stony Brook University, who also agreed to be my recommender.

You can find my CV here: [Zhicheng He's Curriculum Vitae](../assets/CV-He%20Zhicheng.pdf).

[WeChat](../images/wechat_qr.png) / [CSDN](https://blog.csdn.net/m0_72020568?spm=1000.2115.3001.5343)

News
------
I'm happy to join [Dr. Yueming Jin](https://yuemingjin.github.io/)'s team in 2025 as a MEng student.

Latest Progress
------
{% assign latest_progress = site.progress | sort: 'date' | reverse | slice: 0,5 %}
{% if latest_progress and latest_progress.size > 0 %}
<ul>
{% for item in latest_progress %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a> <small>({{ item.date | date: "%Y-%m-%d" }})</small></li>
{% endfor %}
</ul>
<p><a href="/progress/">View all progress →</a></p>
{% else %}
<p>No progress updates yet.</p>
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
