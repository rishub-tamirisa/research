---
title: "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning" 
# date: 2015-12-01
# # tags: ["keyword 1","keyword 2","keyword 4"]
# author: [
#     "Nathaniel Li", "Alexander Pan", "Anjali Gopal", "Summer Yue", "Daniel Berrios",
#     "Alice Gatti", "Justin D. Li", "Ann-Kathrin Dombrowski", "Shashwat Goel", "Long Phan",
#     "Gabriel Mukobi", "Nathan Helm-Burger", "Rassin Lababidi", "Lennart Justen",
#     "Andrew B. Liu", "Michael Chen", "Isabelle Barrass", "Oliver Zhang", "Xiaoyuan Zhu",
#     "Rishub Tamirisa", "Bhrugu Bharathi", "Adam Khoja", "Ariel Herbert-Voss",
#     "Cort B. Breuer", "Andy Zou", "Mantas Mazeika", "Zifan Wang", "Palash Oswal",
#     "Weiran Liu", "Adam A. Hunt", "Justin Tienken-Harder", "Kevin Y. Shih", "Kemper Talley",
#     "John Guan", "Russell Kaplan", "Ian Steneker", "David Campbell", "Brad Jokubaitis",
#     "Alex Levinson", "Jean Wang", "William Qian", "Kallol Krishna Karmakar", "Steven Basart",
#     "Stephen Fitz", "Mindy Levine", "Ponnurangam Kumaraguru", "Uday Tupakula", "Vijay Varadharajan",
#     "Yan Shoshitaishvili", "Jimmy Ba", "Kevin M. Esvelt", "Alexandr Wang", "Dan Hendrycks"
# ]
# description: "This paper shows other things. Published in Journal Name, 2015." 
# summary: "This paper shows other things using other techniques and different data." 
# cover:
#     image: "paper2.png"
#     alt: "Image caption"
#     relative: false
# editPost:
#     URL: "https://doi.org/10.1073/pnas.1816454115"
#     Text: "Other Journal Name"

---

---

##### Links

+ [Paper](https://arxiv.org/pdf/2403.03218.pdf)
+ [Project Page (with code & data)](https://www.wmdp.ai/)
<!-- + [Online appendix](appendix2.pdf) -->

---

##### Abstract

he White House Executive Order on Artificial Intelligence highlights the risks of large language models (LLMs) empowering malicious actors in developing biological, cyber, and chemical weapons. To measure these risks of malicious use, government institutions and major AI labs are developing evaluations for hazardous capabilities in LLMs. However, current evaluations are private, preventing further research into mitigating risk. Furthermore, they focus on only a few, highly specific pathways for malicious use. To fill these gaps, we publicly release the Weapons of Mass Destruction Proxy (WMDP) benchmark, a dataset of 4,157 multiple-choice questions that serve as a proxy measurement of hazardous knowledge in biosecurity, cybersecurity, and chemical security. WMDP was developed by a consortium of academics and technical consultants, and was stringently filtered to eliminate sensitive information prior to public release. WMDP serves two roles: first, as an evaluation for hazardous knowledge in LLMs, and second, as a benchmark for unlearning methods to remove such hazardous knowledge. To guide progress on unlearning, we develop CUT, a state-of-the-art unlearning method based on controlling model representations. CUT reduces model performance on WMDP while maintaining general capabilities in areas such as biology and computer science, suggesting that unlearning may be a concrete path towards reducing malicious use from LLMs.

---

##### Figure 1: The WMDP Benchmark.

![](paper2.png)

---

##### Citation

```BibTeX
@misc{li2024wmdp,
title={The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning},
author={Nathaniel Li and Alexander Pan and Anjali Gopal and Summer Yue and Daniel Berrios and Alice Gatti and Justin D. Li and Ann-Kathrin Dombrowski and Shashwat Goel and Long Phan and Gabriel Mukobi and Nathan Helm-Burger and Rassin Lababidi and Lennart Justen and Andrew B. Liu and Michael Chen and Isabelle Barrass and Oliver Zhang and Xiaoyuan Zhu and Rishub Tamirisa and Bhrugu Bharathi and Adam Khoja and Ariel Herbert-Voss and Cort B. Breuer and Andy Zou and Mantas Mazeika and Zifan Wang and Palash Oswal and Weiran Liu and Adam A. Hunt and Justin Tienken-Harder and Kevin Y. Shih and Kemper Talley and John Guan and Russell Kaplan and Ian Steneker and David Campbell and Brad Jokubaitis and Alex Levinson and Jean Wang and William Qian and Kallol Krishna Karmakar and Steven Basart and Stephen Fitz and Mindy Levine and Ponnurangam Kumaraguru and Uday Tupakula and Vijay Varadharajan and Yan Shoshitaishvili and Jimmy Ba and Kevin M. Esvelt and Alexandr Wang and Dan Hendrycks},
year={2024},
eprint={2403.03218},
archivePrefix={arXiv},
primaryClass={cs.LG}
}
```
