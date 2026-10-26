---
title: "Argomenti"
layout: single
permalink: /categorie/
author_profile: false
classes: wide
seo_title: "Argomenti del blog: attualità, vulnerabilità, prevenzione, incidenti"
seo_description: "Gli articoli del blog di sicurezza informatica ordinati per argomento: attualità, vulnerabilità, prevenzione e gestione degli incidenti."
---
{%- comment -%}
Indice editoriale degli argomenti (stile rivista). Cosa fa: legge gli articoli della lingua della pagina,
ricava le categorie dai front matter (categories:), le descrizioni da _data/categorie.json (chiave nome = categoria)
e disegna: indice a riquadri + una sezione per categoria (articolo in evidenza + elenco).
NON toccare: gli id delle sezioni (slugify della categoria) sono gli ancoraggi usati dalle pillole del blog (/categorie/#slug).
Per aggiungere una descrizione: admin > Categorie, oppure _data/categorie.json {nome, descrizione}.
{%- endcomment -%}
{%- assign posts_l = site.posts | where: "lang", page.lang -%}
{%- assign cats_all = posts_l | map: "categories" | join: "," | split: "," | uniq | sort -%}
{%- assign mesi = "gennaio,febbraio,marzo,aprile,maggio,giugno,luglio,agosto,settembre,ottobre,novembre,dicembre" | split: "," -%}

<style>
#page-title{display:none}
.ed{--ed-ink:#14181f;--ed-mute:#5d6673;--ed-line:#e3e6ea;--ed-acc:var(--t-accent,#1f3a5f);max-width:1080px;margin:0 auto;color:var(--ed-ink)}
.ed a{text-decoration:none}
.ed-head{padding:.5rem 0 2.2rem;border-bottom:1px solid var(--ed-line);margin-bottom:2.2rem}
.ed-kicker{font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--ed-acc);margin:0 0 .7rem}
.ed-h1{font-family:'Playfair Display',Georgia,serif;font-size:clamp(2rem,4.2vw,3rem);font-weight:500;line-height:1.1;margin:0 0 .8rem}
.ed-lead{font-size:1.05rem;line-height:1.7;color:var(--ed-mute);max-width:46rem;margin:0}

.ed-index{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem;margin:0 0 3.2rem}
.ed-tile{display:flex;flex-direction:column;gap:.45rem;padding:1.15rem 1.2rem;border:1px solid var(--ed-line);border-radius:12px;background:#fff;color:inherit;transition:border-color .15s,box-shadow .15s}
.ed-tile:hover{border-color:var(--ed-acc);box-shadow:0 6px 18px rgba(20,24,31,.07)}
.ed-tile b{font-family:'Playfair Display',Georgia,serif;font-size:1.2rem;font-weight:500;color:var(--ed-ink)}
.ed-tile span{font-size:.85rem;line-height:1.5;color:var(--ed-mute);flex:1}
.ed-tile i{font-style:normal;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ed-acc)}

.ed-sec{padding:2.4rem 0 1.2rem;border-top:1px solid var(--ed-line);scroll-margin-top:5rem}
.ed-sec-head{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin-bottom:.4rem}
.ed-sec-head h2{font-family:'Playfair Display',Georgia,serif;font-size:1.7rem;font-weight:500;margin:0}
.ed-count{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ed-mute)}
.ed-sec-desc{margin:0 0 1.6rem;color:var(--ed-mute);line-height:1.65;max-width:46rem}

.ed-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:2.4rem;align-items:start}
.ed-feat{display:block;color:inherit}
.ed-feat h3{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.4rem,2.6vw,1.9rem);font-weight:500;line-height:1.25;margin:.4rem 0 .7rem;color:var(--ed-ink)}
.ed-feat:hover h3{color:var(--ed-acc)}
.ed-feat p{margin:0 0 .9rem;line-height:1.75;color:var(--ed-mute)}
.ed-meta{font-size:.78rem;color:#8a929e}
.ed-more{display:inline-block;margin-top:.2rem;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ed-acc)}
.ed-list{list-style:none;margin:0;padding:0}
.ed-list li{padding:.95rem 0;border-bottom:1px solid var(--ed-line)}
.ed-list li:first-child{padding-top:0}
.ed-list li:last-child{border-bottom:none}
.ed-list a{display:block;color:inherit}
.ed-list strong{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.05rem;font-weight:500;line-height:1.35;margin:.15rem 0 0;color:var(--ed-ink)}
.ed-list a:hover strong{color:var(--ed-acc)}
.ed-all{margin:2.6rem 0 1rem;padding-top:1.6rem;border-top:1px solid var(--ed-line);text-align:center}
.ed-sec:target .ed-sec-head h2{color:var(--ed-acc)}
@media(max-width:760px){.ed-grid{grid-template-columns:1fr;gap:1.4rem}}
</style>

<div class="ed">
  <header class="ed-head">
    <p class="ed-kicker">Blog</p>
    <h1 class="ed-h1">Argomenti</h1>
    <p class="ed-lead">Gli articoli del blog ordinati per tema: cosa succede nel mondo della sicurezza informatica, quali falle riguardano il tuo sito, come prevenire i problemi e cosa fare quando ne capita uno.</p>
  </header>

  <nav class="ed-index" aria-label="Argomenti">
    {%- for cname in cats_all -%}
    {%- assign cdata = site.data.categorie | where: "nome", cname | first -%}
    {%- assign n = 0 -%}
    {%- for p in posts_l -%}{%- if p.categories contains cname -%}{%- assign n = n | plus: 1 -%}{%- endif -%}{%- endfor %}
    <a class="ed-tile" href="#{{ cname | slugify }}">
      <b>{{ cname }}</b>
      <span>{{ cdata.descrizione | strip_html | truncate: 95 }}</span>
      <i>{{ n }} {% if n == 1 %}articolo{% else %}articoli{% endif %}</i>
    </a>
    {%- endfor %}
  </nav>

  {%- for cname in cats_all -%}
  {%- assign cdata = site.data.categorie | where: "nome", cname | first -%}
  {%- assign cposts = "" | split: "" -%}
  {%- for p in posts_l -%}{%- if p.categories contains cname -%}{%- assign cposts = cposts | push: p -%}{%- endif -%}{%- endfor -%}
  {%- assign feat = cposts | first %}
  <section class="ed-sec" id="{{ cname | slugify }}">
    <div class="ed-sec-head">
      <h2>{{ cname }}</h2>
      <span class="ed-count">{{ cposts.size }} {% if cposts.size == 1 %}articolo{% else %}articoli{% endif %}</span>
    </div>
    {%- if cdata.descrizione and cdata.descrizione != "" %}
    <p class="ed-sec-desc">{{ cdata.descrizione | strip_html }}</p>
    {%- endif %}
    <div class="ed-grid">
      <a class="ed-feat" href="{{ feat.url | relative_url }}">
        {%- assign m = feat.date | date: "%-m" | minus: 1 %}
        <span class="ed-meta">{{ feat.date | date: "%-d" }} {{ mesi[m] }} {{ feat.date | date: "%Y" }} · {{ feat.content | number_of_words | divided_by: 200 | plus: 1 }} min di lettura</span>
        <h3>{{ feat.title }}</h3>
        <p>{{ feat.excerpt | strip_html | strip_newlines | truncate: 220 }}</p>
        <span class="ed-more">Leggi l'articolo &rarr;</span>
      </a>
      {%- if cposts.size > 1 %}
      <ul class="ed-list">
        {%- for p in cposts offset: 1 %}
        {%- assign m = p.date | date: "%-m" | minus: 1 %}
        <li><a href="{{ p.url | relative_url }}"><span class="ed-meta">{{ p.date | date: "%-d" }} {{ mesi[m] }} {{ p.date | date: "%Y" }}</span><strong>{{ p.title }}</strong></a></li>
        {%- endfor %}
      </ul>
      {%- endif %}
    </div>
  </section>
  {%- endfor %}

  <div class="ed-all"><a class="btn btn--primary" href="{{ '/blog/' | relative_url }}">Tutti gli articoli</a></div>
</div>
