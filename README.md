# Renkli Mozaik by Arzu Arslan

El emeği mozaik markasının Shopify sitesi. Hedef adres: www.renklimozaik.com, Instagram: @renklimozaik.

## Klasörler
- Kök dizin: Shopify teması (Dawn temelli, MIT lisanslı). Shopify'ın GitHub bağlantısı bu dizini okur.
- `docs/gorev-listesi.md`: görevler ve alınan kararlar.
- `docs/yasal/`: satış sözleşmesi, iade, teslimat, KVKK taslakları (avukat kontrolü gerekir).
- `docs/magaza/`: Shopify mağaza ayar listesi.
- `docs/icerik/`: sayfa metinleri, arama motoru ve Google işletme metinleri.
- `araclar/urun_csv.py`: ürün tablosunu Shopify içe aktarma dosyasına çevirir.
- `docs/marka/`: marka kılavuzu, renk ve yazı tipi bilgileri (`tokens.json`), logolar (`logo/`, SVG).

## Çalışma düzeni
- Canlı mağaza `main` dalından beslenir. Değişiklikler önce `yeni-tasarim` dalında yapılır, Arzu Arslan'ın onayından sonra `main`'e alınır.
- Ürünler, fiyatlar ve siparişler Shopify panelinden yönetilir; bu repoda tutulmaz.
- Şifre, API anahtarı ve müşteri bilgisi bu repoya konmaz.
