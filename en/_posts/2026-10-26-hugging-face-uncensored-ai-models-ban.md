---
layout: single
ref: huggingface-uncensored
title: "Is Hugging Face banning unfiltered AI models? What is true and what is not"
date: 2026-10-26
permalink: /en/blog/news/hugging-face-uncensored-ai-models-ban/
excerpt: "A claim is going around social media that 'they are banning all uncensored models'. The verified facts are smaller and more interesting: here is what actually happened."
seo_title: "Hugging Face and uncensored AI models: total ban or just a few repositories?"
seo_description: "Is Hugging Face banning uncensored AI models? What was really removed, what is still online and why the story matters for cybersecurity."
categories:
  - News
header:
  teaser: /assets/images/blog/hugging-face-modelli-ai-uncensored-ban.svg
  image: /assets/images/blog/hugging-face-modelli-ai-uncensored-ban.svg
lang: en
locale: en
tr: tradotto
tr_hash: 7335nj
---

For a few days a message has been circulating on social media: "They are banning all uncensored AI models on Hugging Face, because of the hacker attacks of the last few days". Before sharing it, it is worth separating the facts from the shouted version.

## What "uncensored" models are
An uncensored (or "abliterated") model is a version of an AI model from which the refusals have been removed: it no longer answers "I cannot help you" when asked, for example, to write code for an attack. Hugging Face is the platform where the community publishes and downloads these models.

## What has been verified
- On 23 October an account on X reported that some unfiltered models were disappearing from the platform, including an "abliterated" version of Kimi K2.7 Code.
- In the preceding weeks Hugging Face had disabled a repository based on GLM-5.3 that was openly built for cyberattacks. The official reason given was only a violation of the content policy.
- Those who checked the public list report that the repositories removed are few, while those with "uncensored" or "abliterated" in the name still number in the thousands.

## What has not been verified
- **A general ban.** The analyses I found agree: there is no rule banning all unfiltered models. It seems rather that the most explicit cases are being removed, where the name, documentation and declared use point to attacks.
- **The link with "the hacker attacks of the last few days".** In the sources consulted there is no official confirmation that the removals are a response to specific attacks. Hugging Face has not given detailed reasons. Treat the cause as a hypothesis, not a fact.

## Why the story matters to us
Even if there is no total ban, the direction is clear: platforms are deciding where to draw the line when three things come together, namely removed filters, strong ability to write code and an openly offensive purpose. Meanwhile Anna Vaccarelli, president of Clusit, reminded Tgcom24 that cybercriminals have been quicker than defenders to adopt artificial intelligence, including to write malware.

For anyone running a website or a server, the practical consequence does not change with the fate of one repository: attacking becomes easier and faster, so **updating quickly matters more**. We saw this with [PHP2Shell]({{ '/en/blog/' | relative_url }}), where the most advanced AI models lowered the barrier to exploiting flaws that had been around for years.

## What you can do now
1. Update PHP, your CMS and plugins to fixed versions.
2. Check that backups exist and can be restored.
3. Review access and recently modified files.

If you would like someone to do it for you, see our [services]({{ '/en/services/' | relative_url }}) or [request an assessment]({{ '/en/contact/' | relative_url }}).

## Sources
- [Pasquale Pillitteri: Hugging Face bans the first uncensored models](https://pasqualepillitteri.it/news/27101/hugging-face-banna-modelli-uncensored-kimi-k27-code) (in Italian)
- [Pasquale Pillitteri: Hugging Face removes a GLM-5.3 used for cyberattacks](https://pasqualepillitteri.it/en/news/20174/glm53-huggingface-takedown-cyber-en)
- [AiIdeList: why Hugging Face disabled the offensive GLM-5.3](https://aiidelist.com/blog/hugging-face-disabled-offensive-cyber-glm-5-3-model)
- [Tgcom24: interview with Anna Vaccarelli, president of Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml) (in Italian)
