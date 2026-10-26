---
layout: single
ref: modelli-uncensored-spiegati
title: "'Uncensored' AI models: what they are, what they are for and why they worry security people"
date: 2026-10-26
permalink: /en/blog/news/uncensored-ai-models-explained/
excerpt: "There is talk of unfiltered models and removals on Hugging Face. We explain in plain words what they are, who uses them for work and what changes for a business."
seo_title: "Uncensored and abliterated AI models: what they are and what risks they bring"
seo_description: "What uncensored or abliterated artificial intelligence models are, legitimate uses, cybersecurity risks and what businesses can do."
categories:
  - News
header:
  teaser: /assets/images/blog/modelli-ai-uncensored-cosa-sono.svg
  image: /assets/images/blog/modelli-ai-uncensored-cosa-sono.svg
lang: en
locale: en
tr: tradotto
tr_hash: 18k83e8
---

After the news about some models being removed from Hugging Face, many people have asked us: what are these "uncensored" models, and why is there so much debate? Let us try to explain without jargon.

## How an AI model with "brakes" works
The most widely used artificial intelligence models (those from the big providers) are also trained to **refuse** certain requests. If you ask how to build a weapon or to write a program to attack a website, they reply that they cannot help. These are the so-called safety filters.

## What "uncensored" or "abliterated" means
For many open models, meaning ones you can download and run on your own computer, someone publishes a **modified version** from which those refusals have been removed. The technical term is "abliterated", the common one is "uncensored". The model answers everything: harmless questions and dangerous ones. It is not a different intelligence: it is the same one, without brakes.

It is a large phenomenon. According to a roundup published by Slash Digital, a 2025 study had counted more than 11,000 of them on Hugging Face, one with over 19 million installs.

## Who uses them and why
They are not only a tool for criminals. People who work in security use them because the official models often refuse legitimate requests too:
- **analysis of suspicious code** and malware by defenders;
- **authorized security tests** on their own systems;
- **reading about a vulnerability** by an administrator who has to fix it;
- writers and researchers working on uncomfortable themes.

One example cited in the same roundup: during an intrusion suffered by Hugging Face itself, commercial models would reportedly have blocked forensic analysis requests because they cannot tell someone responding to an incident from someone attacking, and the team would have analyzed the attackers' logs with an open model on its own infrastructure. It should be said that, according to the same source, this is not an argument against filters on models hosted by others.

## Where the problem lies
Without filters, the same model can help anyone who wants to **write malware, craft convincing scam messages or look for flaws** with less skill and less time. The president of Clusit, Anna Vaccarelli, reminded Tgcom24 that cybercriminals have adopted artificial intelligence faster than defenders and that there are groups selling ready-made attack kits.

That is why platforms are beginning to draw boundaries: the most explicit cases, with a name and declared use for attacks, have been removed, while thousands of other models stay online, often behind terms of use that must be accepted. Some licenses already forbid certain uses: for example, the Llama 3.3 license excludes malicious code.

## What changes for a business
Little that is immediate, and that is the point to understand. You cannot decide which models attackers will use. But you can reduce what they find:
1. **Update early.** Known flaws that have already been fixed are the easiest target, for a human or for an AI.
2. **Protect access:** unique passwords, two-step verification.
3. **Distrust messages that look too perfect.** AI-generated scam texts no longer have the mistakes they used to: always verify another way.
4. **Keep tested backups** and a plan to restart.

If you want to understand how exposed your site is, see our [services]({{ '/en/services/' | relative_url }}) or [request an assessment]({{ '/en/contact/' | relative_url }}).

For the latest on the story, also read [Is Hugging Face banning unfiltered AI models? What is true and what is not]({{ '/en/blog/' | relative_url }}).

## Sources
- [Pasquale Pillitteri: Hugging Face bans the first uncensored models](https://pasqualepillitteri.it/news/27101/hugging-face-banna-modelli-uncensored-kimi-k27-code) (in Italian)
- [Slash Digital: uncensored models, what they are, uses and risks](https://slash-digital.io/en/insights/uncensored-models/)
- [AiIdeList: why Hugging Face disabled the offensive GLM-5.3](https://aiidelist.com/blog/hugging-face-disabled-offensive-cyber-glm-5-3-model)
- [Tgcom24: interview with Anna Vaccarelli, president of Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml) (in Italian)
