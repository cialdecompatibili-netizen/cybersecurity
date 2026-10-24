---
layout: single
ref: php2shell
title: "PHP2Shell: cosa fare adesso (CVE-2026-109618 e CVE-2026-109619)"
date: 2026-10-24
excerpt: "Due falle critiche in PHP, trovate con l'aiuto dell'AI. Versioni corrette, cosa controllare e cosa fare subito."
seo_title: "PHP2Shell: cosa fare adesso (CVE-2026-109618 e CVE-2026-109619)"
seo_description: "PHP2Shell: versioni PHP corrette, come controllare il tuo sito e cosa fare subito, spiegato in italiano."
categories:
  - avvisi
---

I ricercatori di Wiz hanno spiegato che difetti presenti da decenni erano difficili da trasformare in attacco, ma i modelli di AI più avanzati hanno abbassato quella barriera. È il motivo per cui aggiornare in fretta conta più di prima.

Il 21 ottobre 2026 il team di sicurezza di PHP ha rilasciato aggiornamenti d'emergenza per due vulnerabilità critiche, **CVE-2026-109618** e **CVE-2026-109619**, soprannominate PHP2Shell. Entrambe hanno punteggio CVSS v4.0 di 9,2 su 10 e, con richieste web costruite ad arte, possono permettere l'esecuzione di codice sul server senza autenticazione. Il rischio maggiore riguarda le configurazioni con Apache e mod_php. Le falle sono nell'interprete PHP, non in un singolo CMS: sono esposti anche WordPress, Joomla o applicazioni su misura, se girano su una versione vulnerabile.

## Versioni corrette

| Ramo PHP | Versione corretta |
|---|---|
| 8.5 | 8.5.12 |
| 8.4 | 8.4.27 |
| 8.3 | 8.3.36 |
| 8.2 | 8.2.35 |

Il ramo 8.2 non riceverà più correzioni dopo il 31 dicembre 2026. Se usi un ramo più vecchio di quelli elencati, non è più supportato: va portato a un ramo che lo è.

## Cosa fare subito

1. **Controlla la versione.** Da terminale: `php -v`. Su hosting condiviso: pannello di controllo, sezione "Versione PHP". Attenzione: la riga di comando può mostrare una versione diversa da quella usata dal sito.
2. **Aggiorna** a una versione corretta tramite il fornitore del sistema operativo, del pacchetto o dell'hosting, poi riavvia il servizio web.
3. **Se non puoi aggiornare subito**, le misure temporanee riducono l'esposizione ma non la eliminano. Per esempio, disattivare `session.upload_progress.enabled` blocca solo uno dei percorsi dimostrati per CVE-2026-109619 e non protegge da CVE-2026-109618. Un firewall applicativo (WAF) può guadagnare tempo. La soluzione vera è l'aggiornamento.
4. **Controlla se c'è stata compromissione**: file PHP nuovi o modificati di recente, accessi anomali, richieste strane nei log. Per i server esposti a internet e non aggiornati nei giorni scorsi, è prudente cambiare anche password e chiavi.
5. **Verifica il backup**: che esista, sia recente e si possa ripristinare.

## Hai un hosting gestito?
Alcuni provider hanno già aggiornato i server che gestiscono loro. Chiedi conferma scritta della versione in uso. Il problema resta per VPS, hosting non gestiti e applicazioni mai aggiornate.

## Vuoi che lo facciamo noi?
Verifica, aggiornamento, controllo di compromissione, cambio di password e chiavi, backup verificato: vedi i [servizi]({{ '/servizi/' | relative_url }}) oppure [contattaci]({{ '/contatti/' | relative_url }}).

## Fonti
- [Avviso di sicurezza ufficiale di PHP](https://www.php.net/archive/2026.php#2026-10-21-5)
- [Help Net Security: PHP2Shell, aggiornare subito](https://helpnetsecurity.com/2026/10/21/php2shell-php-vulnerabilities-patched-cve-2026-109618-cve-2026-109619)
- [Tanium: risposta a CVE-2026-109618 e CVE-2026-109619](https://www.tanium.com/blog/php2shell-responding-to-cve-2026-109618-and-cve-2026-109619)
