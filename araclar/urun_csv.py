#!/usr/bin/env python3
"""Google Sheets ürün tablosunu Shopify'ın ürün içe aktarma CSV'sine çevirir.

Kullanım:
  1) Tabloyu "Dosya → İndir → Virgülle ayrılmış değerler (.csv)" ile kaydedin.
  2) python3 araclar/urun_csv.py urun-listesi.csv shopify-urunler.csv
  3) Shopify: Ürünler → İçe aktar → shopify-urunler.csv. Ürünler TASLAK olarak gelir; görselleri ürünlere
     panelden ekleyip her ürünü kontrol ettikten sonra yayınlayın.
Fiyatı ve adı boş satırlar atlanır.
"""
import csv, html, re, sys

TR = str.maketrans("çğıöşüÇĞİÖŞÜâÂ", "cgiosuCGIOSUaA")

def slug(s):
    s = re.sub(r"\(öneri\)", "", s, flags=re.I).strip().translate(TR).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def num(s):
    s = (s or "").strip().replace("TL", "").replace("₺", "").replace(".", "").replace(",", ".").strip()
    return s

def govde(r):
    satirlar = []
    for et, k in (("Boyut", "Boyut (cm)"), ("Malzeme", "Malzeme"), ("Yapım süresi", "Yapım süresi"), ("Ağırlık", "Ağırlık (kg)")):
        v = (r.get(k) or "").strip()
        if v:
            satirlar.append(f"<li><strong>{et}:</strong> {html.escape(v)}{' cm' if k.startswith('Boyut') and not v.lower().endswith('cm') else ''}{' kg' if k.startswith('Ağırlık') and not v.lower().endswith('kg') else ''}</li>")
    h = ""
    kisa = (r.get("Kısa açıklama") or "").strip()
    if kisa:
        h += f"<p>{html.escape(kisa)}</p>"
    if r.get("Ürün türü", "").strip() == "Özel sipariş":
        h += "<p><strong>Bu ürün size özel hazırlanır; iade ve değişim kapsamı dışındadır.</strong></p>"
    if satirlar:
        h += "<ul>" + "".join(satirlar) + "</ul>"
    return h

KOLONLAR = ["Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published", "Option1 Name", "Option1 Value",
            "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty",
            "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Requires Shipping",
            "Variant Taxable", "Status"]

def main(girdi, cikti):
    sayi = 0
    with open(girdi, newline="", encoding="utf-8-sig") as f, open(cikti, "w", newline="", encoding="utf-8") as o:
        w = csv.DictWriter(o, fieldnames=KOLONLAR); w.writeheader()
        for r in csv.DictReader(f):
            ad = re.sub(r"\s*\(öneri\)", "", (r.get("Ürün adı") or "")).strip()
            fiyat = num(r.get("Fiyat (TL)"))
            if not ad or not fiyat:
                continue
            tur = (r.get("Ürün türü") or "").strip()
            etiket = ", ".join(x for x in ((r.get("Koleksiyon") or "").strip(), tur) if x)
            agirlik = num(r.get("Ağırlık (kg)"))
            gram = str(int(float(agirlik) * 1000)) if agirlik else ""
            stok = (r.get("Stok") or "").strip()
            ozel = tur == "Özel sipariş"
            w.writerow({
                "Handle": slug(ad), "Title": ad, "Body (HTML)": govde(r), "Vendor": "Renkli Mozaik",
                "Type": tur, "Tags": etiket, "Published": "FALSE", "Option1 Name": "Title", "Option1 Value": "Default Title",
                "Variant SKU": "", "Variant Grams": gram,
                "Variant Inventory Tracker": "" if ozel else "shopify", "Variant Inventory Qty": "" if ozel else (stok or "0"),
                "Variant Inventory Policy": "continue" if ozel else "deny", "Variant Fulfillment Service": "manual",
                "Variant Price": fiyat, "Variant Requires Shipping": "TRUE", "Variant Taxable": "TRUE", "Status": "draft"})
            sayi += 1
    print(f"{sayi} ürün yazıldı → {cikti}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
