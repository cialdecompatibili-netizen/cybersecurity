---
layout: single
ref: frigoriferi-supermercati
title: "Hacked fridges in French supermarkets: the lesson for anyone with connected devices"
date: 2026-10-26
permalink: /en/blog/vulnerabilities/hacked-fridges-french-supermarkets/
excerpt: "A postponed update and a fridge connected to the internet: what happened in France and what it has to do with your website, your router and your cameras."
seo_title: "The supermarket fridge attack: what it teaches businesses"
seo_description: "The attack on French supermarket refrigeration systems explained simply: missing updates, credentials and what to check in your own company."
categories:
  - Vulnerabilities
header:
  teaser: /assets/images/blog/frigoriferi-hackerati-supermercati-francesi.svg
  image: /assets/images/blog/frigoriferi-hackerati-supermercati-francesi.svg
lang: en
locale: en
tr: tradotto
tr_hash: gi9u0h
---

A fridge you can control remotely is convenient: an operator sees temperatures and alarms without moving. But anything connected to the internet can also be reached by people who should not be able to. That is what happened to French supermarkets, and Anna Vaccarelli, president of Clusit, talked about it in an interview with Tgcom24 on 26 October 2026.

## What happened, in short
The refrigeration systems of several chains were managed remotely and connected to the network. Every device contains **firmware**, the software inside it, which has to be updated over time to fix flaws. As reported, the vendor had already flagged some vulnerabilities the year before, to be fixed with an update, but the updates were reportedly not installed. The gaps made it possible to bypass the credential check. Investigations are ongoing, so the details should be treated with caution.

## Why it matters to you too
Vaccarelli stresses two things:
- An attack of this kind needs only **a computer and an organized group**: the flaws had been known for years and no artificial intelligence was needed.
- It is called **OT security** (Operational Technology) and it is growing: after servers and software, connected objects are in the crosshairs. They are no longer a world apart from the network.

Think about what you have connected to the internet at work: cameras, routers, printers, badge readers, equipment, your management software, your website. All of them run software and all of them need updating.

## Five checks to do this week
1. **List the devices** connected to your network, even the ones "nobody has touched in years".
2. **Look for manufacturer updates** and install them. If there are none any more, consider replacing the device.
3. **Change factory credentials** and any shared by several people.
4. **Close remote access** you do not need; protect the access you do.
5. **Ask your supplier in writing** who is responsible for updates: you or them.

The French lesson is simple: the flaw was known, the fix existed, and nobody installed it. The same goes for an out-of-date PHP application (see [PHP2Shell]({{ '/en/blog/' | relative_url }})).

## Want an inventory of what you have online?
We check versions, configuration and access for websites and servers, and hand you a clear report with priorities. See our [services]({{ '/en/services/' | relative_url }}) or [contact us]({{ '/en/contact/' | relative_url }}).

## Sources
- [Tgcom24: interview with Anna Vaccarelli, president of Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml) (in Italian)
- [Tgcom24: France, hacker attack on the fridges of hundreds of supermarkets](https://www.tgcom24.mediaset.it/mondo/francia-hacker-frigoriferi-supermercati_117612366-202602k.shtml) (in Italian)
