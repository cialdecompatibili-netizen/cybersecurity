---
layout: single
ref: huggingface-uncensored
title: "Hugging Face bandisce i modelli AI senza filtri? Cosa è vero e cosa no"
date: 2026-10-26
permalink: /blog/attualita/hugging-face-modelli-ai-uncensored-ban/
excerpt: "Sui social circola la notizia che 'stanno bannando tutti i modelli uncensored'. I fatti verificati sono più piccoli e più interessanti: ecco cosa è successo davvero."
seo_title: "Hugging Face e modelli AI uncensored: ban totale o solo alcuni repository?"
seo_description: "Hugging Face sta bannando i modelli AI uncensored? Cosa è stato rimosso davvero, cosa resta online e perché la notizia riguarda la sicurezza informatica."
categories:
  - Attualità
header:
  teaser: /assets/images/blog/hugging-face-modelli-ai-uncensored-ban.svg
  image: /assets/images/blog/hugging-face-modelli-ai-uncensored-ban.svg
---

Da qualche giorno gira sui social un messaggio che dice: "Stanno bannando tutti i modelli AI uncensored su Hugging Face, a causa degli attacchi hacker degli ultimi giorni". Prima di rilanciarlo, vale la pena separare i fatti dalla versione gridata.

## Che cosa sono i modelli "uncensored"
Un modello uncensored (o "abliterated") è una versione di un modello AI a cui sono stati tolti i rifiuti: non risponde più "non posso aiutarti" quando gli si chiede, per esempio, di scrivere codice per un attacco. Hugging Face è la piattaforma dove la comunità pubblica e scarica questi modelli.

## Cosa risulta verificato
- Il 23 ottobre un account su X ha segnalato che alcuni modelli senza filtri stavano sparendo dalla piattaforma, tra cui una versione "abliterated" di Kimi K2.7 Code.
- Nelle settimane precedenti Hugging Face aveva disattivato un repository basato su GLM-5.3 costruito dichiaratamente per attacchi informatici. Il motivo ufficiale indicato era solo una violazione della politica sui contenuti.
- Chi ha controllato l'elenco pubblico riferisce che i repository rimossi sono pochi, mentre quelli con "uncensored" o "abliterated" nel nome restano migliaia.

## Cosa non risulta
- **Un divieto generale.** Le analisi che ho trovato concordano: non c'è una regola che vieti tutti i modelli senza filtri. Sembra piuttosto che vengano rimossi i casi più espliciti, dove nome, documentazione e uso dichiarato puntano all'attacco.
- **Il legame con "gli attacchi hacker degli ultimi giorni".** Nelle fonti consultate non c'è una conferma ufficiale che le rimozioni siano una risposta a specifici attacchi. Hugging Face non ha dato motivazioni dettagliate. Tratta la causa come un'ipotesi, non come un fatto.

## Perché la notizia ci riguarda
Anche se il ban totale non c'è, la direzione è chiara: le piattaforme stanno decidendo dove mettere il limite quando si uniscono tre cose, cioè filtri tolti, forte capacità di scrivere codice e scopo apertamente offensivo. Intanto Anna Vaccarelli, presidente del Clusit, ha ricordato a Tgcom24 che i criminali informatici sono stati più rapidi dei difensori nell'adottare l'intelligenza artificiale, anche per scrivere malware.

Per chi gestisce un sito o un server la conseguenza pratica non cambia con il destino di un repository: attaccare diventa più facile e veloce, quindi **aggiornare in fretta conta di più**. Lo abbiamo visto con [PHP2Shell]({{ '/blog/' | relative_url }}), dove i modelli di AI più avanzati hanno abbassato la barriera per sfruttare falle presenti da anni.

## Cosa puoi fare adesso
1. Aggiorna PHP, CMS e plugin a versioni corrette.
2. Controlla che i backup esistano e si possano ripristinare.
3. Verifica accessi e file modificati di recente.

Se vuoi che lo faccia qualcuno per te, guarda i [servizi]({{ '/servizi/' | relative_url }}) o [richiedi una valutazione]({{ '/contatti/' | relative_url }}).

## Fonti
- [Pasquale Pillitteri: Hugging Face banna i primi modelli uncensored](https://pasqualepillitteri.it/news/27101/hugging-face-banna-modelli-uncensored-kimi-k27-code)
- [Pasquale Pillitteri: Hugging Face rimuove un GLM-5.3 per attacchi informatici](https://pasqualepillitteri.it/en/news/20174/glm53-huggingface-takedown-cyber-en)
- [AiIdeList: perché Hugging Face ha disattivato il GLM-5.3 offensivo](https://aiidelist.com/blog/hugging-face-disabled-offensive-cyber-glm-5-3-model)
- [Tgcom24: intervista ad Anna Vaccarelli, presidente del Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml)
