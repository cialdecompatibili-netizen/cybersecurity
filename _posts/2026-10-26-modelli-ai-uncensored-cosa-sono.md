---
layout: single
ref: modelli-uncensored-spiegati
title: "Modelli AI 'uncensored': cosa sono, a cosa servono e perché preoccupano chi fa sicurezza"
date: 2026-10-26
excerpt: "Si parla di modelli senza filtri e di rimozioni su Hugging Face. Spieghiamo in parole semplici cosa sono, chi li usa per lavoro e cosa cambia per un'azienda."
seo_title: "Modelli AI uncensored e abliterated: cosa sono e quali rischi comportano"
seo_description: "Cosa sono i modelli di intelligenza artificiale uncensored o abliterated, usi legittimi, rischi per la sicurezza informatica e cosa possono fare le aziende."
categories:
  - Attualità
---

Dopo le notizie sulle rimozioni di alcuni modelli da Hugging Face, molti ci hanno chiesto: ma cosa sono questi modelli "uncensored", e perché fanno tanto discutere? Proviamo a spiegarlo senza gergo.

## Come funziona un modello AI con i "freni"
I modelli di intelligenza artificiale più usati (quelli dei grandi fornitori) sono addestrati anche a **rifiutare** certe richieste. Se chiedi come costruire un'arma o di scrivere un programma per attaccare un sito, rispondono che non possono aiutarti. Sono i cosiddetti filtri di sicurezza.

## Cosa significa "uncensored" o "abliterated"
Per molti modelli aperti, cioè scaricabili ed eseguibili sul proprio computer, qualcuno pubblica una **versione modificata** in cui quei rifiuti sono stati tolti. Il termine tecnico è "abliterated", quello comune è "uncensored". Il modello risponde a tutto: alle domande innocue e a quelle pericolose. Non è un'altra intelligenza: è la stessa, senza freni.

È un fenomeno grande. Secondo una rassegna pubblicata da Slash Digital, uno studio del 2025 ne aveva contati più di 11.000 su Hugging Face, uno dei quali con oltre 19 milioni di installazioni.

## Chi li usa e perché
Non sono solo uno strumento per criminali. Chi lavora in sicurezza li usa perché i modelli ufficiali spesso rifiutano anche richieste legittime:
- **analisi di codice sospetto** e di malware da parte di chi difende;
- **test di sicurezza autorizzati** sui propri sistemi;
- **lettura di una vulnerabilità** da parte di un amministratore che deve correggerla;
- scrittori e ricercatori con temi scomodi.

Un esempio citato dalla stessa rassegna: durante un'intrusione subita dalla stessa Hugging Face, i modelli commerciali avrebbero bloccato le richieste di analisi forense perché non distinguono chi risponde a un incidente da chi attacca, e il team avrebbe analizzato i registri degli attaccanti con un modello aperto sulla propria infrastruttura. Va detto che, secondo la stessa fonte, questo non è un argomento contro i filtri sui modelli ospitati da altri.

## Dove sta il problema
Se i filtri non ci sono, lo stesso modello può aiutare chi vuole **scrivere malware, preparare messaggi truffa convincenti o cercare falle** con meno competenze e meno tempo. La presidente del Clusit, Anna Vaccarelli, ha ricordato a Tgcom24 che i criminali informatici hanno adottato l'intelligenza artificiale più in fretta dei difensori e che esistono gruppi che vendono kit di attacco già pronti.

Per questo le piattaforme stanno cominciando a tracciare dei confini: i casi più espliciti, con nome e uso dichiarato per attacchi, sono stati rimossi, mentre migliaia di altri modelli restano online, spesso dietro condizioni d'uso da accettare. Alcune licenze vietano già certi usi: per esempio quella di Llama 3.3 esclude il codice malevolo.

## Cosa cambia per un'azienda
Poco di immediato, e questo è l'aspetto da capire. Non puoi decidere quali modelli userà chi attacca. Puoi però ridurre ciò che trovano:
1. **Aggiorna presto.** Le falle note e già corrette sono il bersaglio più facile, per un umano o per un'AI.
2. **Proteggi gli accessi:** password uniche, verifica in due passaggi.
3. **Diffida dei messaggi troppo perfetti.** I testi truffa generati dall'AI non hanno più gli errori di una volta: verifica sempre per un'altra strada.
4. **Tieni backup provati** e un piano per ripartire.

Se vuoi capire quanto è esposto il tuo sito, guarda i nostri [servizi]({{ '/servizi/' | relative_url }}) oppure [richiedi una valutazione]({{ '/contatti/' | relative_url }}).

Per l'aggiornamento della notizia, leggi anche [Hugging Face bandisce i modelli AI senza filtri? Cosa è vero e cosa no]({{ '/blog/' | relative_url }}).

## Fonti
- [Pasquale Pillitteri: Hugging Face banna i primi modelli uncensored](https://pasqualepillitteri.it/news/27101/hugging-face-banna-modelli-uncensored-kimi-k27-code)
- [Slash Digital: modelli uncensored, cosa sono, usi e rischi](https://slash-digital.io/en/insights/uncensored-models/)
- [AiIdeList: perché Hugging Face ha disattivato il GLM-5.3 offensivo](https://aiidelist.com/blog/hugging-face-disabled-offensive-cyber-glm-5-3-model)
- [Tgcom24: intervista ad Anna Vaccarelli, presidente del Clusit](https://www.tgcom24.mediaset.it/tgtech/attacchi-hacker-sicurezza-cyber-criminali-vaccarelli_118063555-202602k.shtml)
