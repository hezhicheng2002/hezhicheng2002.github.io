---
permalink: /
layout: single
title: "Hi, I'm Zhicheng He（何智成）"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a second-year Master of Engineering (MEng) by Research student in the Department of Biomedical Engineering at the National University of Singapore, working in the [Intelligent Medical Vision & Robotics (iMVR) Lab](https://github.com/jinlab-imvr) under the supervision of [Dr. Yueming Jin](https://yuemingjin.github.io/). I completed my undergraduate degree in Computer Science at Beijing Jiaotong University. My research interests include medical image analysis and multi-modal large language models.

[View my CV →](/cv/)

I am very fortunate to be advised by [Prof. Xiaoqing Lv](https://ieeexplore.ieee.org/author/37599114400) of [Wangxuan Institute of Computer Technology](https://www.icst.pku.edu.cn/), Peking University. Meanwhile, I am honored to be recommended by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang) of [Ren Lab](http://www.labren.org/mm/) from The Chinese University of Hong Kong. Moreover, I am thrilled to be instructed by [Prof. Tengfei Ma](https://ai.stonybrook.edu/people/faculty/TengfeiMa) of Department of Biomedical Informatics from Stony Brook University, who also agreed to be my recommender.

News
------
- 2026: [MedVAR](https://arxiv.org/abs/2602.14512) is submitted to <strong>Nature Biomedical Engineering</strong>.
- 2026: [TeethGNN](https://arxiv.org/abs/2609.09801) is accepted by <strong>Biocybernetics and Biomedical Engineering</strong>.
- 2026: [ReMem](https://arxiv.org/abs/2607.24794) is accepted by <strong>ECCV 2026</strong>.
- 2026: [SciXplain](https://doi.org/10.1007/978-3-032-36207-0_28) is accepted by <strong>DAS 2026</strong>.
- 2026: Ad-hoc Reviewer for <strong>Nature Biomedical Engineering</strong>.
- 2026: [MedVAR](https://arxiv.org/abs/2602.14512) is available on arXiv.
- 2025: [Granulon](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_Granulon_Awakening_Pixel-Level_Visual_Encoders_with_Adaptive_Multi-Granularity_Semantics_for_CVPR_2026_paper.html) is accepted by <strong>CVPR 2026</strong>.
- 2025: [DINOv3-FD](https://openreview.net/forum?id=cAVWntFxlF) is accepted by <strong>MIDL 2026</strong>.
- 2025: I join [Dr. Yueming Jin](https://yuemingjin.github.io/)'s lab as an MEng by Research student.

Selected Publications
------
{% assign selected_publication_urls = "/publication/2026-02-16-medvar|/publication/2026-01-01-dinov3-fd|/publication/2026-09-09-teethgnn" | split: "|" %}
{% assign publications = site.publications %}
{% if publications and publications.size > 0 %}
<ul>
{% for selected_url in selected_publication_urls %}
  {% assign item = publications | where: 'permalink', selected_url | first %}
  {% unless item %}{% continue %}{% endunless %}
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
