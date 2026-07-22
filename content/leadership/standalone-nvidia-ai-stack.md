---
title: "Two NVIDIA courses later: what the AI stack looks like from the infrastructure side"
date: 2026-07-19T17:30:00+01:00
---

Conclusion first: after working through two of NVIDIA's hands-on Deep Learning Institute courses, I am convinced the AI stack is about 10% model and 90% infrastructure — and that the 90% is where most organisations will succeed or fail.

The two courses were ["Fundamentals of Accelerated Data Science"](https://learn.nvidia.com/courses/course-detail?course_id=course-v1%3ADLI+C-DS-02+V2) — the [RAPIDS](https://rapids.ai/) ecosystem, finishing with a graded coding assessment on a simulated epidemic dataset — and ["Adding New Knowledge to LLMs"](https://learn.nvidia.com/courses/course-detail?course_id=course-v1%3ADLI+C-FX-26+V1), a five-lab tour of how you actually get domain knowledge into a model: curation to synthetic data to training to compression. I did them as deliberate upskilling; I have spent my career running large-scale scientific infrastructure, most of it at EMBL-EBI, and I wanted to see the AI stack from inside the labs rather than from the vendor slide decks.

Here is what the notebooks teach you that the keynotes do not.

### Lesson one: "teaching an LLM" is a data pipeline with a model at the end

The fine-tuning course devotes its entire first lab to data: cleaning, deduplication, language identification, quality filtering with NeMo Curator, then generating synthetic training data — topics, sub-topics, question-answer pairs, even maths problems with worked solutions. Only in lab three do you touch the model, walking the escalation ladder: continued pretraining, supervised fine-tuning, then direct preference optimisation (DPO) for alignment. The worked domain example is legal Q&A — nicely concrete, and a long way from "prompt engineering".

Anyone who has run a bioinformatics platform recognises this shape instantly. It is ETL. The glamorous step at the end consumes whatever quality the pipeline upstream delivered, and no amount of GPU spend repairs poor input data. Institutions have known "garbage in, garbage out" since punch cards; the LLM era has simply raised the price of the garbage.

The practical implication for technology leaders: if your AI initiative's budget is mostly compute and hardly any data engineering, the ratio is wrong.

### Lesson two: acceleration is memory management wearing a cape

The data science course delivers its central insight quietly, in an early module on memory management. cuDF gives you a pandas-like dataframe on the GPU, and the speed-ups are real — until you move data between CPU and GPU carelessly, at which point the transfer costs eat everything. The course drills the discipline: keep the data resident on the device, chain operations there, watch your types, scale out with Dask when a dataset outgrows one card.

This is the oldest lesson in high-performance computing: locality wins. The same principle that governs CPU caches and kept our petabyte archives fast governs a DGX. I find this oddly reassuring. The hardware is exotic; the physics of data movement is not, and people who have spent years thinking about storage tiers and network hops already have the right instincts.

The graded assessment made the point concretely — population-scale analysis (finding infected individuals, nearest treatment facilities, risk factors with cuML and XGBoost) that would crawl on CPU becomes interactive on GPU, but only if you write it GPU-shaped. The tool does not save you from a bad access pattern.

### Lesson three: evaluation is the adult in the room

The middle lab of the LLM course is pure evaluation: benchmark the base model on your domain with NIM microservices, then and only then customise, then measure again. It is the least glamorous lab and the most important. Without the before-and-after numbers, a fine-tuning project is a faith-based initiative.

Tech leadership translation: "we fine-tuned a model" is not an outcome. "Domain accuracy went from X to Y at Z cost per query" is an outcome. Insist on the harness before approving the training run — exactly as you would insist on load tests before a migration.

The course also had us read the [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948) — reasoning capability trained largely through reinforcement learning. Worth the evening: it is a useful reminder that the frontier keeps moving, and that the pipeline skills (data, evaluation, serving) depreciate far more slowly than any specific model does.

### Lesson four: compression is where AI meets the accountant

The final lab chains quantisation, depth pruning and knowledge distillation, then measures inference speed. That ordering is the tell: in production, the question is rarely "how good can the model be?" and nearly always "how good can it be within this serving budget?".

Running models on my own hardware at home — an 8GB GPU that concentrates the mind wonderfully — taught me the same economics in miniature. Quantisation is the difference between a model that runs and one that does not. At datacentre scale the same trade appears with more zeros attached: serving cost compounds per query, forever, which is why a slightly worse model that is three times cheaper to serve usually wins.

### The through-line

What NVIDIA's courses taught me, beyond the tools, is that the AI stack rewards exactly the disciplines infrastructure people have been practising for decades: pipeline hygiene, locality, measurement, cost engineering. The unfamiliar parts are genuinely new and worth learning properly — DPO was not in my vocabulary two years ago. But the load-bearing walls are old friends.

Fair caveat: DLI courses are excellent and they are also a funnel — every solution is spelled N-V-I-D-I-A, and NeMo/NIM are one opinionated path among several. Take the concepts as portable; hold the product choices to the same procurement scrutiny as any other vendor stack.

If your organisation is building AI capability: hire for the 90%. The model layer changes quarterly. The infrastructure judgement compounds.

What proportion of your AI effort goes into data and evaluation versus the model itself — and is that ratio a decision or an accident?

## Sources

- [NVIDIA DLI, "Fundamentals of Accelerated Data Science"](https://learn.nvidia.com/courses/course-detail?course_id=course-v1%3ADLI+C-DS-02+V2)
- [NVIDIA DLI, "Adding New Knowledge to LLMs"](https://learn.nvidia.com/courses/course-detail?course_id=course-v1%3ADLI+C-FX-26+V1)
- [RAPIDS — open source GPU-accelerated data science](https://rapids.ai/)
- [The DeepSeek-R1 paper (course reading, worth the evening)](https://arxiv.org/abs/2501.12948)
