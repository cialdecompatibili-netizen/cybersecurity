---
layout: single
title: "Services"
permalink: /en/services/
ref: servizi
lang: en
locale: en
tr: tradotto
tr_hash: 13870ty
author_profile: false
classes: wide
seo_title: "Cybersecurity services for websites, e-commerce and SMEs"
seo_description: "Cleaning hacked sites, security checks, hardening PHP and CMS, monitoring, backups with a restore test and compliance support. Written engagement, price agreed beforehand."
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
  <p class="sv-kicker">Cybersecurity for websites and SMEs</p>
  <h1 class="sv-h1">Your website and your data, secure and under control</h1>
  <p class="sv-lead">Updates, checks, cleanup after an attack, backups that really restore. We work under a written engagement, explain every step in plain English and agree the price before we start.</p>
  <div class="sv-cta">
    <a class="btn btn--primary" href="{{ '/en/contact/' | relative_url }}">Request an assessment</a>
    <a class="sv-btn2" href="#emergenza">Already under attack?</a>
  </div>
</header>

<nav class="sv-situ" aria-label="What do you need">
  <a href="#emergenza"><b>I have been hacked</b><span>The site shows strange pages, Google flags danger, customers receive emails you never sent.</span><i>Emergency response</i></a>
  <a href="#verifica"><b>I want to know if I am at risk</b><span>Old versions, forgotten plugins, open access: we check and give you the priorities.</span><i>Checks</i></a>
  <a href="#protezione"><b>I want to secure everything</b><span>Updates, configuration, protection of access and email.</span><i>Protection</i></a>
  <a href="#continuita"><b>I want peace of mind</b><span>Monitoring, tested backups and a written plan to restart if something happens.</span><i>Continuity</i></a>
</nav>

<section class="sv-sec" id="emergenza">
  <p class="sv-kicker">1 · Emergency response</p>
  <h2>You have been attacked</h2>
  <p class="sv-intro">When a site is compromised, every hour counts. First we stop the damage, then we work out how they got in, then we clean up and close the door, otherwise they come back.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Cleaning hacked websites</h3><p>Finding and removing malware, backdoors, injected files and unknown accounts on PHP, WordPress and other CMS sites.</p></div>
    <div class="sv-card"><h3>SEO spam and redirects</h3><p>Pages for drugs, games or fake products that have appeared on your domain, or visitors sent to scam sites: we find them and remove them.</p></div>
    <div class="sv-card"><h3>Clearing Google warnings</h3><p>If the browser or the search engine flags the site as dangerous, we help you clean it and request a review.</p></div>
    <div class="sv-card"><h3>Analysis of what happened</h3><p>Where they got in, what they touched, for how long. We hand you a written report, which is also useful for any notifications you owe.</p></div>
    <div class="sv-card"><h3>Changing credentials and keys</h3><p>Panel, database, FTP/SSH and mailbox passwords, API keys and tokens: everything that may have been seen.</p></div>
    <div class="sv-card"><h3>Recovery and going back online</h3><p>Restart from a clean backup or rebuild of the site, with the flaw closed before going back online.</p></div>
  </div>
</section>

<section class="sv-sec" id="verifica">
  <p class="sv-kicker">2 · Checks</p>
  <h2>Find out where you are vulnerable, before anyone else does</h2>
  <p class="sv-intro">A check cannot guarantee that nothing has happened: we tell you what we found, what we did not and in what order to act.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Security check-up</h3><p>The starting point: an inventory of sites, servers and services, PHP and CMS versions, plugins, access, exposure to the internet.</p><ul><li>A list of what you have online</li><li>Priorities: what to fix first</li><li>Written report</li></ul></div>
    <div class="sv-card"><h3>Vulnerability check</h3><p>Checking versions and components against known flaws, including brand-new ones (like <a href="{{ '/en/blog/' | relative_url }}">PHP2Shell</a>).</p></div>
    <div class="sv-card"><h3>Compromise check</h3><p>Recently modified files, PHP files where they should not be, unusual users and access, suspicious requests in the logs.</p></div>
    <div class="sv-card"><h3>Website security testing</h3><p>Tests on the site or application, under a written engagement, to find common mistakes like those on the OWASP list: login, forms, file upload, permissions.</p></div>
    <div class="sv-card"><h3>Exposure and configuration</h3><p>Open services and ports, HTTPS certificates, security headers, forgotten directories and backup files, panels reachable by anyone.</p></div>
    <div class="sv-card"><h3>Office devices and networks</h3><p>Routers, cameras, printers, NAS and other connected devices: missing updates and factory passwords, the French fridge problem in miniature.</p></div>
  </div>
</section>

<section class="sv-sec" id="protezione">
  <p class="sv-kicker">3 · Protection</p>
  <h2>We close the doors that were left open</h2>
  <p class="sv-intro">Almost all successful attacks go through out-of-date software and weak credentials. This is where we work.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Updating PHP and applications</h3><p>Moving to fixed, supported versions of PHP, CMS, plugins and libraries, checking that the site still works. On managed hosting, we confirm with the provider that it has really been done.</p></div>
    <div class="sv-card"><h3>Hardening</h3><p>File permissions, unneeded functions switched off, hidden panels, protected private areas, a tighter server configuration.</p></div>
    <div class="sv-card"><h3>Access and passwords</h3><p>Two-step verification, unique passwords, separate accounts with only the permissions needed, removal of users who no longer work with you.</p></div>
    <div class="sv-card"><h3>Firewall and protection from hostile traffic</h3><p>Setting up a web application firewall (WAF) and limits against automated login attempts, to buy time while you update.</p></div>
    <div class="sv-card"><h3>HTTPS and security headers</h3><p>Correct certificates, secure redirects, headers that reduce session theft and injection of other people's code.</p></div>
    <div class="sv-card"><h3>Business email security</h3><p>Setting up SPF, DKIM and DMARC, to make it harder to send fake emails in your name and to improve delivery of genuine messages.</p></div>
  </div>
</section>

<section class="sv-sec" id="continuita">
  <p class="sv-kicker">4 · Continuity</p>
  <h2>Ongoing monitoring and a restart proven by testing</h2>
  <p class="sv-intro">Security is not a one-off job: new flaws come out every week. And on the day you need it, the backup has to work.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Site monitoring</h3><p>Checking that the site is reachable, that files do not change for no reason and that the domain and certificate do not suddenly expire.</p></div>
    <div class="sv-card"><h3>Alerts on the flaws that affect you</h3><p>We follow security advisories and write to you when one concerns the technologies you use, with what to do and how quickly.</p></div>
    <div class="sv-card"><h3>Regular updates</h3><p>Regular updating of system, CMS and plugins, with a backup copy before every major change.</p></div>
    <div class="sv-card"><h3>Backups with a restore test</h3><p>Automatic copies kept off the server and, above all, a real restore test: a backup that has never been tested is just a hope.</p></div>
    <div class="sv-card"><h3>Incident response plan</h3><p>A short, clear document: who to call, what to do in the first hours, where the copies are, who decides and who communicates.</p></div>
    <div class="sv-card"><h3>Periodic report</h3><p>A summary in plain language of what was checked, what was changed and what is left to do. No jargon.</p></div>
  </div>
</section>

<section class="sv-sec" id="persone">
  <p class="sv-kicker">5 · People and rules</p>
  <h2>The part no software solves</h2>
  <p class="sv-intro">According to the Clusit president's interview on Tgcom24, in the vast majority of cases the attack succeeds because of human error. That is why, alongside technical work, we offer light support on habits.</p>
  <div class="sv-grid">
    <div class="sv-card"><h3>Basic anti-phishing training</h3><p>A short session with real examples of scam messages, fake bank transfers and fake couriers, for the people who work with you.</p></div>
    <div class="sv-card"><h3>Simple rules for the team</h3><p>A page of practical rules on passwords, email, personal devices and what to do when in doubt. Written to be actually read.</p></div>
    <div class="sv-card"><h3>Technical support for compliance</h3><p>A checklist of the technical measures required by GDPR and NIS2 for your case and a first assessment of what is missing. It does not replace the advice of a lawyer or a DPO.</p></div>
  </div>
</section>

<section class="sv-sec" id="per-chi">
  <p class="sv-kicker">Who we work for</p>
  <h2>Businesses that depend on the web to operate</h2>
  <div class="sv-who"><span>E-commerce</span><span>Hotels and accommodation</span><span>Restaurants and venues</span><span>Professional firms</span><span>Web agencies and developers</span><span>SMEs and craft businesses</span><span>Associations and organizations</span></div>
  <p class="sv-note">The hospitality sector, for example, is among the hardest hit according to the Clusit president. If you manage websites for your clients, we can take care of the security side for you.</p>
</section>

<section class="sv-sec" id="metodo">
  <p class="sv-kicker">How we work</p>
  <h2>Four steps, everything in writing</h2>
  <ol class="sv-steps">
    <li><b>Written engagement</b><span>We define which systems are in scope and who authorizes us. We do not work on what is not yours.</span></li>
    <li><b>Assessment</b><span>Versions, configuration, signs of compromise. We tell you what we found and what we did not.</span></li>
    <li><b>Intervention</b><span>Agreed fixes, with the price set before we begin. No surprises on the invoice.</span></li>
    <li><b>Report</b><span>What we checked, what we changed, what is left to do and when to check again.</span></li>
  </ol>
</section>

<section class="sv-sec" id="formule">
  <p class="sv-kicker">Plans</p>
  <h2>Start where you need to</h2>
  <p class="sv-intro">The price depends on the number of systems and the type of hosting: we agree it in writing before we start.</p>
  <div class="sv-plans">
    <div class="sv-plan">
      <h3>Check-up</h3>
      <p class="sv-for">To understand where you stand.</p>
      <ul><li>Inventory of sites and servers</li><li>Version and vulnerability check</li><li>Compromise check</li><li>Report with priorities</li></ul>
      <a class="sv-btn2" href="{{ '/en/contact/' | relative_url }}">Request the check-up</a>
    </div>
    <div class="sv-plan sv-main">
      <h3>Securing</h3>
      <p class="sv-for">To fix what is wrong.</p>
      <ul><li>The whole check-up</li><li>Updates and hardening</li><li>Access, passwords and keys</li><li>Backups with a restore test</li><li>Written response plan</li></ul>
      <a class="btn btn--primary" href="{{ '/en/contact/' | relative_url }}">Ask for a quote</a>
    </div>
    <div class="sv-plan">
      <h3>Ongoing watch</h3>
      <p class="sv-for">So you can stop worrying.</p>
      <ul><li>Monitoring and regular updates</li><li>Alerts on the flaws that affect you</li><li>Periodic report</li><li>Priority lane in case of an incident</li></ul>
      <a class="sv-btn2" href="{{ '/en/contact/' | relative_url }}">Let's talk</a>
    </div>
  </div>
  <p class="sv-note">Already been attacked? Skip the plans: <a href="{{ '/en/contact/' | relative_url }}">write to us right away</a> and we start with emergency response.</p>
</section>

<section class="sv-sec sv-faq" id="faq">
  <p class="sv-kicker">Frequently asked questions</p>
  <h2>What we are asked most often</h2>
  <details><summary>We are a small company: are we really of interest to hackers?</summary><p>Yes. Attacks are almost always automated and look for old software and weak credentials, not famous names. And a small site can serve as a bridge to a bigger customer. We cover this in an article <a href="{{ '/en/blog/' | relative_url }}">on the blog</a>.</p></details>
  <details><summary>Can you guarantee we will never be attacked?</summary><p>No, and be wary of anyone who promises it. We secure you against known flaws and greatly reduce the risk; if something does happen, you have a plan and copies to restart from.</p></details>
  <details><summary>How much does it cost?</summary><p>It depends on how many systems you have and how they are hosted. After an initial assessment you receive a written price, which does not change once work has started.</p></details>
  <details><summary>Do I need to give you access to the server or the site?</summary><p>Yes, in order to check and intervene. It is done under a written engagement that lists the systems involved; when we finish, temporary access is changed.</p></details>
  <details><summary>My hosting is managed: do I still need to do anything?</summary><p>Often yes. Some providers update the servers they manage, but not the applications (CMS, plugins, custom sites). We help you get written confirmation and cover the rest.</p></details>
  <details><summary>What do you not do?</summary><p>We do not work on systems you do not own or have a written engagement for. We do not give legal opinions: for GDPR and NIS2 we help with the technical side and recommend you also consult a lawyer or a DPO.</p></details>
</section>

<aside class="sv-end">
  <h2>Let's start with an assessment</h2>
  <p>Tell us what you have online and what worries you. We reply with the next steps and a clear price.</p>
  <a href="{{ '/en/contact/' | relative_url }}">Request an assessment</a>
</aside>

</div>
