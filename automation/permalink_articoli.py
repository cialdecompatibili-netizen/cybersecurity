#!/usr/bin/env python3
"""Indirizzo degli articoli = /blog/<categoria>/<titolo>/ (EN: /en/blog/<categoria>/<titolo>/).

COSA FA: per ogni articolo di _posts/ e <lingua>/_posts/ scrive nel front matter
`permalink: /blog/<slug-categoria>/<slug-file>/` (categoria SENZA accenti, come le pagine categoria
/blog/attualita/) e crea in redirect/ una pagina che porta dal vecchio indirizzo al nuovo
(stesso formato dell'admin > Redirect: layout redirect, permalink, redirect_to).
PERCHE': `:categories` di Jekyll tiene gli accenti (/vulnerabilita%CC%80/...) e per le lingue
aggiunge da solo la cartella (/en/<cat>/...): non si puo' far uscire /en/blog/<cat>/ senza plugin.
QUANDO LANCIARLO: dopo ogni nuovo articolo EN (le copie dell'admin non portano il permalink)
e quando cambi la categoria di un articolo. Idempotente.
USO:  python automation/permalink_articoli.py            (dry-run, stampa il riepilogo)
      python automation/permalink_articoli.py --apply    (scrive file e redirect)
"""
import re, sys, pathlib, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
APPLY = "--apply" in sys.argv


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def permalink_articolo(categoria, nome_slug, lang="it"):
    pre = "/blog/" if lang == "it" else "/%s/blog/" % lang
    return "%s%s/%s/" % (pre, slug(categoria), nome_slug)


def vecchio_default(categoria, nome_slug, lang):
    # come lo calcolava Jekyll con permalink /:categories/:title/ (minuscolo, accenti tenuti)
    pre = "/" if lang == "it" else "/%s/" % lang
    return "%s%s/%s/" % (pre, categoria.lower(), nome_slug)


def prima_categoria(fm):
    righe = fm.split("\n")
    for i, r in enumerate(righe):
        m = re.match(r"^categor(?:y|ies):\s*(.*?)\s*$", r.rstrip("\r"))
        if not m:
            continue
        resto = m.group(1)
        if resto:
            resto = resto.strip("[]").split(",")[0]
            return resto.strip().strip("'\"")
        for r2 in righe[i + 1:]:
            m2 = re.match(r"^\s*-\s*(.+?)\s*$", r2.rstrip("\r"))
            if m2:
                return m2.group(1).strip("'\"")
            if r2.strip() and not r2.startswith(" "):
                break
    return None


def nome_redirect(da):
    n = re.sub(r"[^a-zA-Z0-9]+", "-", da.strip("/")).strip("-").lower()
    return n or "home"


def stub(da, a):
    return ('---\nlayout: redirect\npermalink: "%s"\nredirect_to: "%s"\n'
            'sitemap: false\nnoindex: true\n---\n') % (da, a)


def cartelle():
    out = [(ROOT / "_posts", "it")]
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and re.fullmatch(r"[a-z]{2}(-[a-z]{2})?", d.name) and (d / "_posts").is_dir():
            out.append((d / "_posts", d.name))
    return out


def main():
    mod = red = ok = 0
    for cartella, lang in cartelle():
        for f in sorted(cartella.glob("*.md")):
            testo = f.read_bytes().decode("utf-8")
            m = re.match(r"---(\r?\n)(.*?)\r?\n---\r?\n", testo, re.S)
            if not m:
                print("SALTATO (niente front matter):", f.name); continue
            nl, fm = m.group(1), m.group(2)
            cat = prima_categoria(fm)
            if not cat:
                print("SALTATO (niente categoria):", f.name); continue
            nome = re.sub(r"\.md$", "", re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.name))
            nuovo = permalink_articolo(cat, nome, lang)
            pm = re.search(r"^permalink:\s*[\"']?([^\"'\r\n]+?)[\"']?\s*$", fm, re.M)
            vecchio = pm.group(1) if pm else vecchio_default(cat, nome, lang)
            if pm and vecchio == nuovo:
                ok += 1; continue
            if pm:
                fm2 = fm[:pm.start()] + "permalink: " + nuovo + fm[pm.end():]
            else:
                ins = re.search(r"^date:.*$", fm, re.M) or re.search(r"^layout:.*$", fm, re.M)
                fm2 = fm[:ins.end()] + nl + "permalink: " + nuovo + fm[ins.end():]
            mod += 1
            print("%s: %s -> %s" % (f.name[:48], vecchio, nuovo))
            if APPLY:
                f.write_bytes((testo[:m.start(2)] + fm2 + testo[m.end(2):]).encode("utf-8"))
            if vecchio != nuovo:
                rf = ROOT / "redirect" / (nome_redirect(vecchio) + ".html")
                red += 1
                if APPLY:
                    rf.parent.mkdir(exist_ok=True)
                    rf.write_bytes(stub(vecchio, nuovo).encode("utf-8"))
    print("articoli gia' a posto: %d | da aggiornare: %d | redirect: %d | %s"
          % (ok, mod, red, "APPLICATO" if APPLY else "dry-run (usa --apply)"))


if __name__ == "__main__":
    main()
