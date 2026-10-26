#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera le copertine SVG degli articoli (assets/images/blog/<slug>.svg) e le aggiunge al front matter
(header.teaser + header.image) se mancano. Rilanciabile: non crea doppioni.
Per cambiare i colori modifica BG1/BG2/ACC. Per una nuova copertina aggiungi una riga in COPERTINE.
Uso: python automation/genera_copertine.py   (dalla radice del repo)
"""
import os, re, io

BG1, BG2, ACC, SOFT = "#0b1f3a", "#1f4470", "#5cc4e8", "#ffffff"
RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAD, "assets", "images", "blog")

def stroke(w=10, c=ACC, extra=""):
    return f'fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}'

MOTIVI = {
 "code": f'<text x="900" y="400" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="200" font-weight="700" fill="{SOFT}">&lt;/&gt;</text><path d="M640 470h520" {stroke(8)}/>',
 "target": "".join(f'<circle cx="900" cy="338" r="{r}" {stroke(10 if r>100 else 8, ACC if i%2==0 else SOFT)}/>' for i,r in enumerate((190,135,80))) + f'<circle cx="900" cy="338" r="22" fill="{ACC}"/><path d="M900 110v70M900 496v70M672 338h70M1058 338h70" {stroke(10,SOFT)}/>',
 "fridge": f'<rect x="780" y="130" width="240" height="420" rx="26" {stroke(10,SOFT)}/><path d="M780 300h240M820 200v50M820 340v90" {stroke(10)}/><path d="M1080 250q55 40 0 80M1120 215q90 75 0 150" {stroke(9)}/><circle cx="1050" cy="290" r="9" fill="{ACC}"/>',
 "user": f'<circle cx="900" cy="250" r="82" {stroke(10,SOFT)}/><path d="M740 520q10-140 160-140t160 140" {stroke(10,SOFT)}/><path d="M1100 140l90 150h-180z" {stroke(9)}/><path d="M1100 195v45" {stroke(9)}/><circle cx="1100" cy="262" r="6" fill="{ACC}"/>',
 "checklist": f'<rect x="740" y="120" width="330" height="440" rx="24" {stroke(10,SOFT)}/>' + "".join(f'<path d="M785 {y}l22 22 40-44" {stroke(9)}/><path d="M880 {y}h130" {stroke(9,SOFT)}/>' for y in (230,330,430)) + f'<circle cx="1110" cy="480" r="78" fill="{BG2}" {stroke(9)}/><path d="M1110 430v52l36 22" {stroke(9,SOFT)}/>',
 "chip": f'<rect x="760" y="200" width="280" height="280" rx="30" {stroke(10,SOFT)}/>' + "".join(f'<path d="M{x} 200v-60M{x} 480v60" {stroke(9)}/>' for x in (820,900,980)) + "".join(f'<path d="M760 {y}h-60M1040 {y}h60" {stroke(9)}/>' for y in (270,340,410)) + f'<text x="900" y="372" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="110" font-weight="700" fill="{ACC}">AI</text>',
 "lock": f'<rect x="770" y="300" width="260" height="210" rx="28" {stroke(10,SOFT)}/><path d="M830 300v-70a70 70 0 0 1 140 0" {stroke(10)}/><circle cx="900" cy="390" r="22" fill="{ACC}"/><path d="M900 410v52" {stroke(10)}/>',
 "unlock": f'<rect x="770" y="300" width="260" height="210" rx="28" {stroke(10,SOFT)}/><path d="M830 300v-70a70 70 0 0 1 140 0v10" {stroke(10)}/><path d="M970 240l60-10" {stroke(0.1,BG1)}/><circle cx="900" cy="390" r="22" fill="{ACC}"/><path d="M900 410v52" {stroke(10)}/><path d="M1090 250l30 30M1120 250l-30 30" {stroke(8,SOFT)}/>',
}

COPERTINE = {  # slug file post (senza data) : motivo
 "php2shell-cosa-e-successo": "code",
 "siamo-tutti-nel-mirino-anche-le-piccole-aziende": "target",
 "frigoriferi-hackerati-supermercati-francesi": "fridge",
 "errore-umano-attacchi-hacker-formazione": "user",
 "attacco-hacker-cosa-fare-piano-risposta": "checklist",
 "hugging-face-modelli-ai-uncensored-ban": "lock",
 "ai-attacchi-informatici-come-difendersi": "chip",
 "modelli-ai-uncensored-cosa-sono": "unlock",
}

def svg(motivo):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" role="img" aria-hidden="true">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient></defs>
<rect width="1200" height="675" fill="url(#g)"/>
<g opacity=".10" stroke="{SOFT}" stroke-width="1">{"".join(f'<path d="M{x} 0v675"/>' for x in range(0,1200,60))}{"".join(f'<path d="M0 {y}h1200"/>' for y in range(0,675,60))}</g>
<circle cx="900" cy="338" r="270" fill="{ACC}" opacity=".07"/>
{MOTIVI[motivo]}
</svg>
'''

os.makedirs(OUT, exist_ok=True)
posts_dir = os.path.join(RAD, "_posts")
for nome in sorted(os.listdir(posts_dir)):
    if not nome.endswith(".md"): continue
    base = nome[11:-3]
    if base not in COPERTINE: continue
    with io.open(os.path.join(OUT, base + ".svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(svg(COPERTINE[base]))
    p = os.path.join(posts_dir, nome)
    with io.open(p, "r", encoding="utf-8", newline="") as f: t = f.read()
    if re.search(r"^header:", t, re.M): continue
    nl = "\r\n" if "\r\n" in t else "\n"
    blocco = f"header:{nl}  teaser: /assets/images/blog/{base}.svg{nl}  image: /assets/images/blog/{base}.svg{nl}"
    m = re.match(r"(---\r?\n.*?\r?\n)(---\r?\n)", t, re.S)
    if m:
        t = m.group(1) + blocco + m.group(2) + t[m.end():]
        with io.open(p, "w", encoding="utf-8", newline="") as f: f.write(t)
        print("copertina + front matter:", nome)
