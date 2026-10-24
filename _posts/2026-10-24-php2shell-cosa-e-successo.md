---
layout: single
title: "PHP2Shell: cosa è successo e perché l'AI accorcia i tempi"
date: 2026-10-24
excerpt: "Due falle critiche in PHP, trovate con l'aiuto dell'AI, e una lezione pratica per chi gestisce un sito: aggiornare in fretta non è più un'opzione."
seo_title: "PHP2Shell: cosa è successo e perché l'AI accorcia i tempi"
seo_description: "Le falle PHP2Shell (CVE-2026-109618 e CVE-2026-109619) spiegate in modo semplice, e cosa cambia con l'AI per chi gestisce un sito."
categories:
  - journal
---

Il 21 ottobre 2026 PHP ha pubblicato correzioni d'emergenza per due vulnerabilità, CVE-2026-109618 e CVE-2026-109619, chiamate PHP2Shell. Sono falle nel cuore del linguaggio, e per questo riguardano un sito su qualunque CMS giri, non solo una piattaforma in particolare.

## In parole semplici
Entrambe nascono dalla gestione degli errori: in certe situazioni, come la memoria esaurita, PHP lascia dati di una richiesta in uno stato incoerente o usa memoria già liberata. Un attaccante può sfruttarlo con richieste web costruite ad arte per eseguire codice sul server, senza bisogno di password.

## Perché l'AI cambia il discorso
I ricercatori di Wiz hanno spiegato che difetti presenti da decenni erano difficili da trasformare in un attacco, perché serviva una catena di passaggi molto complessa. I modelli di AI più avanzati hanno abbassato quella barriera. La conseguenza pratica è che il tempo tra la scoperta di una falla e il suo sfruttamento si accorcia: aggiornare il prima possibile conta più di prima.

## Cosa fare
Controllare la versione di PHP e portarla a 8.5.12, 8.4.27, 8.3.36 o 8.2.35 (o successiva nel proprio ramo). Poi verificare i segni di compromissione e che il backup sia ripristinabile. La guida passo passo è nella pagina [Emergenza PHP2Shell]({{ '/emergenza-php2shell/' | relative_url }}).
