---
layout: single
title: "Servizi"
permalink: /servizi/
ref: servizi
author_profile: false
classes: wide
seo_title: "Servizi di sicurezza informatica per siti, e-commerce e PMI"
seo_description: "Pulizia siti hackerati, controlli di sicurezza, messa in sicurezza di PHP e CMS, monitoraggio, backup con prova di ripristino e supporto alla conformità. Incarico scritto, prezzo concordato prima."
---
{%- comment -%}
Pagina servizi commerciale. Struttura: hero > 4 situazioni (indice) > gruppi di servizi > per chi > metodo > formule > FAQ > CTA.
NON scrivere prezzi, certificazioni o numeri che non siano veri: tutto cio' che e' qui deve poter essere mantenuto.
Gli id (#emergenza, #verifica, #protezione, #continuita, #persone) sono usati dai riquadri iniziali.
Per cambiare i colori: variabile --sv-acc (eredita --t-accent del tema).
{%- endcomment -%}
<style>
#page-title{display:none}
.sv{--sv-ink:#14181f;--sv-mute:#5d6673;--sv-line:#e3e6ea;--sv-soft:#f4f6f9;--sv-acc:var(--t-accent,#1f3a5f);max-width:1080px;margin:0 auto;color:var(--sv-ink)}
.sv a{text-decoration:none}
.sv h2,.sv h3{margin-top:0}
.sv-kicker{font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--sv-acc);margin:0 0 .7rem}
.sv-hero{padding:.6rem 0 2.6rem}
.sv-h1{font-family:'Playfair Display',Georgia,serif;font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:500;line-height:1.1;margin:0 0 1rem;max-width:20ch}
.sv-lead{font-size:1.1rem;line-height:1.7;color:var(--sv-mute);max-width:44rem;margin:0 0 1.6rem}
.sv-cta{display:flex;gap:.8rem;flex-wrap:wrap;align-items:center}
.sv-cta small{color:var(--sv-mute);font-size:.85rem}
.sv-btn2{display:inline-block;padding:.7em 1.3em;border:1px solid var(--sv-acc);border-radius:6px;color:var(--sv-acc) !important;font-weight:600;font-size:.95rem}
.sv-btn2:hover{background:var(--sv-soft)}

.sv-situ{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin:0 0 3.4rem}
.sv-situ a{display:flex;flex-direction:column;gap:.45rem;padding:1.2rem 1.25rem;border:1px solid var(--sv-line);border-radius:12px;background:#fff;color:inherit;transition:border-color .15s,box-shadow .15s}
.sv-situ a:hover{border-color:var(--sv-acc);box-shadow:0 6px 18px rgba(20,24,31,.07)}
.sv-situ b{font-family:'Playfair Display',Georgia,serif;font-size:1.15rem;font-weight:500}
.sv-situ span{font-size:.88rem;line-height:1.55;color:var(--sv-mute);flex:1}
.sv-situ i{font-style:normal;font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--sv-acc)}

.sv-sec{padding:2.6rem 0 1.4rem;border-top:1px solid var(--sv-line);scroll-margin-top:5rem}
.sv-sec h2{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.6rem,3vw,2.1rem);font-weight:500;margin:0 0 .5rem}
.sv-intro{color:var(--sv-mute);line-height:1.7;max-width:46rem;margin:0 0 1.6rem}
.sv-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.1rem}
.sv-card{padding:1.3rem 1.35rem;border:1px solid var(--sv-line);border-radius:12px;background:#fff}
.sv-card h3{font-size:1.05rem;font-weight:700;line-height:1.3;margin:0 0 .5rem}
.sv-card p{margin:0;font-size:.93rem;line-height:1.65;color:var(--sv-mute)}
.sv-card ul{margin:.6rem 0 0;padding-left:1.1rem;font-size:.9rem;line-height:1.6;color:var(--sv-mute)}

.sv-who{display:flex;flex-wrap:wrap;gap:.6rem;margin:0}
.sv-who span{padding:.5rem 1rem;border:1px solid var(--sv-line);border-radius:999px;font-size:.92rem;background:var(--sv-soft)}

.sv-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.2rem;counter-reset:st;margin:0;padding:0;list-style:none}
.sv-steps li{counter-increment:st;padding:1.2rem 1.3rem;background:var(--sv-soft);border-radius:12px}
.sv-steps li::before{content:counter(st);display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.8rem;color:var(--sv-acc);margin-bottom:.3rem}
.sv-steps b{display:block;margin-bottom:.3rem}
.sv-steps span{font-size:.92rem;line-height:1.6;color:var(--sv-mute)}

.sv-plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem}
.sv-plan{display:flex;flex-direction:column;padding:1.5rem 1.5rem 1.4rem;border:1px solid var(--sv-line);border-radius:14px;background:#fff}
.sv-plan.sv-main{border:2px solid var(--sv-acc)}
.sv-plan h3{font-family:'Playfair Display',Georgia,serif;font-size:1.3rem;font-weight:500;margin:0 0 .3rem}
.sv-plan .sv-for{font-size:.88rem;color:var(--sv-mute);margin:0 0 1rem;line-height:1.5}
.sv-plan ul{margin:0 0 1.2rem;padding-left:1.1rem;line-height:1.7;font-size:.93rem;flex:1}
.sv-note{font-size:.88rem;color:var(--sv-mute);margin:1.1rem 0 0}

.sv-faq details{border-bottom:1px solid var(--sv-line);padding:1rem 0}
.sv-faq summary{cursor:pointer;font-weight:600;font-size:1.02rem;list-style:none}
.sv-faq summary::-webkit-details-marker{display:none}
.sv-faq summary::after{content:"+";float:right;font-size:1.3rem;color:var(--sv-acc)}
.sv-faq details[open] summary::after{content:"\2212"}
.sv-faq p{margin:.7rem 0 0;line-height:1.7;color:var(--sv-mute);max-width:46rem}

.sv-end{margin:3rem 0 1rem;padding:2.4rem 2rem;border-radius:16px;background:var(--sv-acc);color:#fff;text-align:center}
.sv-end h2{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.5rem,3vw,2rem);font-weight:500;margin:0 0 .6rem;color:#fff}
.sv-end p{margin:0 auto 1.4rem;max-width:36rem;line-height:1.7;color:rgba(255,255,255,.88)}
.sv-end a{display:inline-block;padding:.8em 1.6em;background:#fff;color:var(--sv-acc) !important;border-radius:6px;font-weight:700}
@media(max-width:640px){.sv-end{padding:1.8rem 1.2rem}}
</style>

<div class="sv">

<header class="sv-hero">
  <p class="sv-kicker">Sicurezza informatica per siti e PMI</p>
  <h1 class="sv-h1">Il tuo sito e i tuoi dati, al sicuro e sotto controllo</h1>
  <p class="sv-lead">Aggiornamenti, controlli, pulizia dopo un attacco, backup che si ripristinano davvero. Lavoriamo con incarico scritto, ti spieghiamo ogni passo in italiano e concordiamo il prezzo prima di iniziare.</p>
  <div class="sv-cta">
    <a class="btn btn--primary" href="{{ '/contatti/' | relative_url }}">Richiedi una valutazione</a>
    <a class="sv-btn2" href="#emergenza">Sei già sotto attacco?</a>
  </div>
</header>

<nav class="sv-situ" aria-label="Di cosa hai bisogno">
  <a href="#emergenza"><b>Mi hanno hackerato</b><span>Il sito mostra pagine strane, Google segnala pericolo, i clienti ricevono mail che non hai mandato.</span><i>Pronto intervento</i></a>
  <a href="#verifica"><b>Voglio sapere se sono a rischio</b><span>Versioni vecchie, plugin dimenticati, accessi aperti: controlliamo e ti diamo le priorità.</span><i>Controlli</i></a>
  <a href="#protezione"><b>Voglio mettere tutto in sicurezza</b><span>Aggiornamenti, configurazioni, protezione degli accessi e della posta.</span><i>Protezione</i></a>
  <a href="#continuita"><b>Voglio dormire tranquillo</b><span>Monitoraggio, backup provati e un piano scritto per ripartire se succede qualcosa.</span><i>Continuità</i></a>
</nav>

<section class="sv-sec" id="emergenza">
  <p class="sv-kicker">1 · Pronto intervento</p>
  <h2>Hai subito un attacco</h2>
  <p class="sv-intro">Quando il sito è compromesso, ogni ora conta. Prima fermiamo i danni, poi capiamo come sono entrati, poi ripuliamo e chiudiamo la porta, altrimenti rientrano.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Pulizia di siti hackerati</h3><p>Ricerca e rimozione di malware, backdoor, file iniettati e account sconosciuti su siti PHP, WordPress e altri CMS.</p></div>
    <div class="sv-card"><h3>Spam SEO e reindirizzamenti</h3><p>Pagine di farmaci, giochi o prodotti falsi comparse nel tuo dominio, o visitatori mandati su siti truffa: le troviamo e le togliamo.</p></div>
    <div class="sv-card"><h3>Rimozione dagli avvisi di Google</h3><p>Se il browser o il motore di ricerca segnalano il sito come pericoloso, ti aiutiamo a ripulirlo e a chiedere il riesame.</p></div>
    <div class="sv-card"><h3>Analisi di cosa è successo</h3><p>Da dove sono entrati, cosa hanno toccato, per quanto tempo. Ti consegniamo una relazione scritta, utile anche per le comunicazioni dovute.</p></div>
    <div class="sv-card"><h3>Cambio di credenziali e chiavi</h3><p>Password di pannello, database, FTP/SSH, caselle di posta, chiavi API e token: tutto ciò che potrebbe essere stato visto.</p></div>
    <div class="sv-card"><h3>Ripristino e rimessa online</h3><p>Ripartenza da un backup pulito o ricostruzione del sito, con la falla chiusa prima di tornare online.</p></div>
  </div>
</section>

<section class="sv-sec" id="verifica">
  <p class="sv-kicker">2 · Controlli</p>
  <h2>Scopri dove sei vulnerabile, prima degli altri</h2>
  <p class="sv-intro">Un controllo non può garantire che non sia successo nulla: ti diciamo cosa abbiamo trovato, cosa no e in che ordine intervenire.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Check-up di sicurezza</h3><p>Il punto di partenza: censimento di siti, server e servizi, versioni di PHP e CMS, plugin, accessi, esposizione verso internet.</p><ul><li>Elenco di ciò che hai online</li><li>Priorità: cosa sistemare prima</li><li>Relazione scritta</li></ul></div>
    <div class="sv-card"><h3>Verifica delle vulnerabilità</h3><p>Controllo di versioni e componenti contro le falle note, anche quelle appena uscite (come <a href="{{ '/blog/' | relative_url }}">PHP2Shell</a>).</p></div>
    <div class="sv-card"><h3>Controllo di compromissione</h3><p>File modificati di recente, file PHP dove non dovrebbero stare, utenti e accessi anomali, richieste sospette nei log.</p></div>
    <div class="sv-card"><h3>Test di sicurezza del sito</h3><p>Prove sul sito o sull'applicazione, con incarico scritto, per trovare errori comuni come quelli dell'elenco OWASP: login, form, caricamento file, permessi.</p></div>
    <div class="sv-card"><h3>Esposizione e configurazione</h3><p>Servizi e porte aperte, certificati HTTPS, intestazioni di sicurezza, directory e file di backup dimenticati, pannelli raggiungibili da chiunque.</p></div>
    <div class="sv-card"><h3>Dispositivi e reti in ufficio</h3><p>Router, telecamere, stampanti, NAS e altri apparecchi collegati: aggiornamenti mancanti e password di fabbrica, il problema dei frigoriferi francesi in piccolo.</p></div>
  </div>
</section>

<section class="sv-sec" id="protezione">
  <p class="sv-kicker">3 · Protezione</p>
  <h2>Chiudiamo le porte che sono rimaste aperte</h2>
  <p class="sv-intro">Quasi tutti gli attacchi riusciti passano da software non aggiornato e credenziali deboli. Qui si lavora su quello.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Aggiornamento di PHP e applicazioni</h3><p>Passaggio a versioni corrette e supportate di PHP, CMS, plugin e librerie, con verifica che il sito funzioni ancora. Su hosting gestito, controllo con il provider che sia stato fatto davvero.</p></div>
    <div class="sv-card"><h3>Messa in sicurezza (hardening)</h3><p>Permessi dei file, funzioni inutili disattivate, pannelli nascosti, aree riservate protette, configurazione del server più chiusa.</p></div>
    <div class="sv-card"><h3>Accessi e password</h3><p>Verifica in due passaggi, password univoche, account separati con i soli permessi che servono, rimozione degli utenti che non lavorano più con te.</p></div>
    <div class="sv-card"><h3>Firewall e protezione dal traffico ostile</h3><p>Configurazione di un firewall per siti web (WAF) e di limiti contro i tentativi automatici di accesso, per guadagnare tempo mentre si aggiorna.</p></div>
    <div class="sv-card"><h3>HTTPS e intestazioni di sicurezza</h3><p>Certificati corretti, reindirizzamento sicuro, intestazioni che riducono furti di sessione e inserimento di codice altrui.</p></div>
    <div class="sv-card"><h3>Sicurezza della posta aziendale</h3><p>Configurazione di SPF, DKIM e DMARC, per rendere più difficile mandare mail false a nome tuo e migliorare la consegna dei messaggi veri.</p></div>
  </div>
</section>

<section class="sv-sec" id="continuita">
  <p class="sv-kicker">4 · Continuità</p>
  <h2>Controllo continuo e ripartenza garantita dalla prova</h2>
  <p class="sv-intro">La sicurezza non è un intervento una tantum: escono nuove falle ogni settimana. E il giorno che serve, il backup deve funzionare.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Monitoraggio del sito</h3><p>Controllo che il sito sia raggiungibile, che i file non cambino senza motivo e che il dominio e il certificato non scadano all'improvviso.</p></div>
    <div class="sv-card"><h3>Avvisi sulle falle che ti riguardano</h3><p>Seguiamo gli avvisi di sicurezza e ti scriviamo quando uno riguarda le tecnologie che usi, con cosa fare e in quanto tempo.</p></div>
    <div class="sv-card"><h3>Aggiornamenti periodici</h3><p>Aggiornamento regolare di sistema, CMS e plugin, con copia di sicurezza prima di ogni intervento importante.</p></div>
    <div class="sv-card"><h3>Backup con prova di ripristino</h3><p>Copie automatiche conservate fuori dal server e, soprattutto, una prova vera di ripristino: un backup mai provato è solo una speranza.</p></div>
    <div class="sv-card"><h3>Piano di risposta agli incidenti</h3><p>Un documento breve e chiaro: chi chiamare, cosa fare nelle prime ore, dove sono le copie, chi decide e chi comunica.</p></div>
    <div class="sv-card"><h3>Relazione periodica</h3><p>Un riepilogo in italiano di cosa è stato controllato, cosa è stato cambiato e cosa resta da fare. Senza gergo.</p></div>
  </div>
</section>

<section class="sv-sec" id="persone">
  <p class="sv-kicker">5 · Persone e regole</p>
  <h2>La parte che nessun software risolve</h2>
  <p class="sv-intro">Secondo l'intervista della presidente del Clusit a Tgcom24, nella grande maggioranza dei casi l'attacco riesce per un errore umano. Per questo accanto agli interventi tecnici offriamo un supporto leggero sulle abitudini.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Formazione base anti-phishing</h3><p>Un incontro breve, con esempi reali di messaggi truffa, falsi bonifici e finti corrieri, per chi lavora con te.</p></div>
    <div class="sv-card"><h3>Regole semplici per il team</h3><p>Una pagina di regole pratiche su password, posta, dispositivi personali e cosa fare in caso di dubbio. Scritta per essere letta davvero.</p></div>
    <div class="sv-card"><h3>Supporto tecnico alla conformità</h3><p>Checklist delle misure tecniche richieste da GDPR e NIS2 per il tuo caso e prima valutazione di cosa manca. Non sostituisce il parere di un legale o di un DPO.</p></div>
  </div>
</section>

<section class="sv-sec" id="per-chi">
  <p class="sv-kicker">Per chi lavoriamo</p>
  <h2>Realtà che dipendono dal web per lavorare</h2>
  <div class="sv-who"><span>E-commerce</span><span>Hotel e strutture ricettive</span><span>Ristoranti e locali</span><span>Studi professionali</span><span>Agenzie web e sviluppatori</span><span>PMI e imprese artigiane</span><span>Associazioni ed enti</span></div>
  <p class="sv-note">Il settore ricettivo, per esempio, è tra i più colpiti secondo la presidente del Clusit. Se gestisci siti per i tuoi clienti, possiamo occuparci della parte di sicurezza al posto tuo.</p>
</section>

<section class="sv-sec" id="metodo">
  <p class="sv-kicker">Come lavoriamo</p>
  <h2>Quattro passi, tutto per iscritto</h2>
  <ol class="sv-steps">
    <li><b>Incarico scritto</b><span>Definiamo quali sistemi rientrano nell'intervento e chi ci autorizza. Non interveniamo su ciò che non è tuo.</span></li>
    <li><b>Valutazione</b><span>Versioni, configurazione, segnali di compromissione. Ti diciamo cosa abbiamo trovato e cosa no.</span></li>
    <li><b>Intervento</b><span>Correzioni concordate, con prezzo definito prima di iniziare. Niente sorprese in fattura.</span></li>
    <li><b>Relazione</b><span>Cosa abbiamo controllato, cosa abbiamo cambiato, cosa resta da fare e quando ricontrollare.</span></li>
  </ol>
</section>

<section class="sv-sec" id="formule">
  <p class="sv-kicker">Formule</p>
  <h2>Parti da dove serve</h2>
  <p class="sv-intro">Il prezzo dipende dal numero di sistemi e dal tipo di hosting: lo concordiamo per iscritto prima di cominciare.</p>
  <div class="sv-plans">
    <div class="sv-plan">
      <h3>Check-up</h3>
      <p class="sv-for">Per capire a che punto sei.</p>
      <ul><li>Censimento di siti e server</li><li>Controllo di versioni e vulnerabilità</li><li>Controllo di compromissione</li><li>Relazione con le priorità</li></ul>
      <a class="sv-btn2" href="{{ '/contatti/' | relative_url }}">Richiedi il check-up</a>
    </div>
    <div class="sv-plan sv-main">
      <h3>Messa in sicurezza</h3>
      <p class="sv-for">Per sistemare ciò che non va.</p>
      <ul><li>Tutto il check-up</li><li>Aggiornamenti e hardening</li><li>Accessi, password e chiavi</li><li>Backup con prova di ripristino</li><li>Piano di risposta scritto</li></ul>
      <a class="btn btn--primary" href="{{ '/contatti/' | relative_url }}">Chiedi un preventivo</a>
    </div>
    <div class="sv-plan">
      <h3>Sorveglianza continua</h3>
      <p class="sv-for">Per non pensarci più.</p>
      <ul><li>Monitoraggio e aggiornamenti periodici</li><li>Avvisi sulle falle che ti riguardano</li><li>Relazione periodica</li><li>Corsia preferenziale in caso di incidente</li></ul>
      <a class="sv-btn2" href="{{ '/contatti/' | relative_url }}">Parliamone</a>
    </div>
  </div>
  <p class="sv-note">Hai già subito un attacco? Salta le formule: <a href="{{ '/contatti/' | relative_url }}">scrivici subito</a> e partiamo dal pronto intervento.</p>
</section>

<section class="sv-sec sv-faq" id="faq">
  <p class="sv-kicker">Domande frequenti</p>
  <h2>Quello che ci chiedono più spesso</h2>
  <details><summary>Siamo una piccola azienda: interessiamo davvero agli hacker?</summary><p>Sì. Gli attacchi sono quasi sempre automatici e cercano software vecchio e credenziali deboli, non nomi famosi. E un sito piccolo può servire come ponte verso un cliente più grande. Ne parliamo nell'articolo <a href="{{ '/blog/' | relative_url }}">sul blog</a>.</p></details>
  <details><summary>Potete garantire che non verremo mai attaccati?</summary><p>No, e diffidate di chi lo promette. Mettiamo in sicurezza dalle falle note e riduciamo molto il rischio; se succede qualcosa, avete un piano e copie su cui ripartire.</p></details>
  <details><summary>Quanto costa?</summary><p>Dipende da quanti sistemi hai e da come sono ospitati. Dopo una prima valutazione ricevi un prezzo scritto, che non cambia a lavori iniziati.</p></details>
  <details><summary>Mi serve dare accesso al server o al sito?</summary><p>Sì, per controllare e intervenire. Si fa con un incarico scritto che elenca i sistemi coinvolti; al termine si cambiano gli accessi temporanei.</p></details>
  <details><summary>Il mio hosting è gestito: devo comunque fare qualcosa?</summary><p>Spesso sì. Alcuni provider aggiornano i server che gestiscono loro, ma non le applicazioni (CMS, plugin, siti su misura). Ti aiutiamo a farti dare conferma scritta e a coprire il resto.</p></details>
  <details><summary>Cosa non fate?</summary><p>Non interveniamo su sistemi di cui non hai la titolarità o un incarico scritto. Non diamo pareri legali: per GDPR e NIS2 ti aiutiamo sulla parte tecnica e ti consigliamo di sentire anche un legale o un DPO.</p></details>
</section>

<aside class="sv-end">
  <h2>Cominciamo da una valutazione</h2>
  <p>Raccontaci cosa hai online e cosa ti preoccupa. Ti rispondiamo con i passi successivi e un prezzo chiaro.</p>
  <a href="{{ '/contatti/' | relative_url }}">Richiedi una valutazione</a>
</aside>

</div>
