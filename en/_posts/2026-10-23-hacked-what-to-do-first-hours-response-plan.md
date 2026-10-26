---
layout: single
ref: piano-incidente
title: "Been hit by a cyberattack? What to do in the first hours (and why you need a plan beforehand)"
date: 2026-10-23
excerpt: "When it happens, there is no time to improvise. The first steps to limit the damage, and the action plan that almost every company is missing."
seo_title: "Cyberattack: what to do right away and how to prepare a response plan"
seo_description: "What to do in the first hours after a cyberattack, which mistakes to avoid and how to prepare a written response and recovery plan."
categories:
  - Incidents
header:
  teaser: /assets/images/blog/attacco-hacker-cosa-fare-piano-risposta.svg
  image: /assets/images/blog/attacco-hacker-cosa-fare-piano-risposta.svg
lang: en
locale: en
tr: tradotto
tr_hash: ctvia3
---

Asked "what is the first thing to do after an attack?", Anna Vaccarelli, president of Clusit (the Italian Association for Information Security), answered on Tgcom24 with a quip ("crying over spilt milk"), and then explained the serious part: prevent further damage, close the gaps as soon as possible and, above all, **already have an action plan**. That, she says, is exactly what is missing.

## The first hours: what to do
1. **Stay calm and stop.** Do not delete anything: files and logs are needed to understand what happened.
2. **Isolate the affected system.** Disconnect the computer or server involved from the network, without shutting everything down blindly unless you have to.
3. **Change your credentials** from a clean device: site panel, hosting, database, FTP/SSH, email, keys and tokens.
4. **Close the gap.** Update the vulnerable software or switch off whatever you do not need.
5. **Look for other traces.** New or modified PHP files, unknown users, unusual access and requests in the logs.
6. **Restore from a clean backup**, one from before the intrusion, after closing the gap. If you restart without fixing the cause, they get back in.
7. **Inform those who need to know**: colleagues, affected customers and, if personal data was breached, work out the notification obligations with an adviser.

## The most common mistakes
- Restoring straight away without understanding how they got in.
- Changing passwords from the same compromised computer.
- Not knowing who to call, where the backups are, or when they were last made.

## The plan, before the incident
A short written document, kept up to date, is enough:
- a list of sites, servers and services, with who manages them;
- contacts to call (hosting, suppliers, consultant);
- where the backups are and how to restore them, with a **restore test** that has really been done;
- who decides and who communicates.

Vaccarelli points out that in Italy many still see security as optional. When something happens, the cost of not having a plan is almost always higher than the cost of preparing one.

## We can help you prepare it
Our [services]({{ '/en/services/' | relative_url }}) include checking backups with a restore test, a written restart procedure and a compromise check with a report. If something has just happened to you, [write to us right away]({{ '/en/contact/' | relative_url }}).

## Sources
- [Tgcom24: interview with Anna Vaccarelli, president of Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml) (in Italian)
