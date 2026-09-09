---
title: "Toward Robust Unlearning for LLMs" 
author: "Rishub Tamirisa, Bhrugu Bharathi, Andy Zhou, Bo Li, Mantas Mazeika "

---

##### Links

+ [Paper (ICLR 2024 Workshop Ver.)](https://openreview.net/pdf?id=4rPzaUF6Ej)

---

##### Abstract

Recent rapid advances in AI enabled by large language models (LLMs) have raised widespread concerns regarding their potential for malicious misuse. While traditional open-source software has long established mechanisms for combating such adversarial behavior, systems involving large neural networks are nontrivial to interpret—let alone intervene on—for safe use. Various alignment methods have been proposed to steer model responses towards a desired "safe" output distribution. However, these techniques are superficial and remain susceptible to adversarial prompting, and can be undone entirely with supervised fine-tuning. These vulnerabilities necessitate a machine unlearning approach, in which the underlying representations of these target concepts are corrupted or forgotten. We introduce state-of-the-art methods for unlearning desired concepts from LLMs. We demonstrate our results on the MMLU benchmark, showing that we can decrease accuracy on a forget set of concepts to chance levels while maintaining accuracy on the retain set.

---

##### Figure 1: The necessity of robust unlearning.

![](paper1.png)

---
