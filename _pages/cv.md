---
layout: archive
title: "Resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Computer Science and Technology, Beijing Jiaotong University, 2025
* Master of Engineering in National University of Singapore, 2027

Selected Research Experience
======
* **2024.01 - 2025.04: Document Content Extraction and Comprehension Using LLM**
  * **Advisor: Prof. Xiaoqing Lv, Wangxuan Institute of Computer Technology, Peking University**
  * Developed an email parsing and recommendation system using LLM libraries like SpaCy and keyBERT to evaluate
keyword importance and grammatical weights, creating a service that parses subscribed arXiv alerts; realized the delivery of personalized recommendation lists of research articles based on the parsed data.

* **2024.01 - 2024.10: Orthodontics Image Classification Based on Adapter Learning**
  * **Advisor: Prof. Hongliang Ren, the Chinese University of Hong Kong**
  * Engaged in the adapter learning based orthodontics image classification using MMPretrain to train mainstream pipelines including ResNet50, Vision Transformer, Swin Transformer, and Surgical-Dino for classifying orthodontic diseases.

* **2024.07 - 2024.10: Multi-view Contrastive Learning of Medical Time Series Prediction Pretraining**
  * **Advisor: Prof. Tengfei Ma, the Stony Brook University**
  * Implemented the ViTST and PatchTST models on PAMAP2 dataset and extracted feature representations for contrast learning, while integrated both views into one potential space.
  
Skills
======
* Python, Pytorch
* Java, Matlab
* SQL, Tableau
  

Publications
======
{% assign publications = site.publications | sort: 'date' | reverse %}
{% for item in publications %}
* [**{{ item.title }}**]({{ item.paperurl }}) — {{ item.venue }}, {{ item.date | date: '%Y' }}.
{% endfor %}

  
Service and Leadership
======
* Previously volunteered to instruct Probability seminars and hold Data Science workshop in Academic Support Center
* Have been leader of study groups for almost every coursework and competition throughout the college time
