# ikas'a geçiş planı

Karar (6 Ekim 2026): Mağaza Shopify yerine **ikas** üzerinde kurulacak. Gerekçe: Türkçe panel ve destek, yerel ödeme sağlayıcıları ve taksit hazır, fiyat TL bazlı, Arzu Arslan'ın temel bilgisayar becerisi için sade yönetim.

## Taşınanlar (hazır)
| Ne | Nerede |
| --- | --- |
| Logo, renkler, yazı tipleri | `docs/marka/`, `assets/rm-*` |
| Sayfa metinleri: Hikâyem, Özel sipariş | `docs/icerik/hikayem.html`, `ozel-siparis.html` |
| Arama motoru ve Google işletme metinleri | `docs/icerik/seo.md`, `google-isletme.md` |
| Yasal taslaklar | `docs/yasal/` |
| Ürün listesi | Drive: "Renkli Mozaik - Ürün Listesi" |
| Ürün görselleri | Drive klasörü (tam çözünürlük), `docs/gorseller/` (küçük kopyalar) |
| Alan adı | renklimozaik.com |

## Yeniden yapılacaklar
- Tema/tasarım: ikas'ın kendi hazır temaları ve düzenleyicisiyle, aynı yerleşimle (giriş bölümü, 3 koleksiyon kartı, öne çıkanlar, özel sipariş, hikâye).
- Mağaza ayarları, ödeme sağlayıcısı, kargo, menüler: `docs/magaza/ayar-listesi.md` ikas'a göre uyarlanır.
- Ürün toplu aktarımı: ikas'ın kendi Excel şablonu kullanılır (şablon ikas panelinden indirilir; `araclar/urun_csv.py` buna göre uyarlanır).

## Sırayla
1. ☐ ikas hesabı açılır (Arzu Arslan adına, ücretsiz deneme/başlangıç paketi). Hesabı sahibi açar.
2. ☐ Paket seçimi ve ödeme yöntemi (iyzico/PayTR) için fiyat ve komisyon tablosu çıkarılır.
3. ☐ Tema seçilir; marka renkleri, logo ve yazı tipi uygulanır.
4. ☐ Koleksiyonlar: Tabaklar, Panolar, Altlıklar.
5. ☐ Sayfalar: Hikâyem, Özel sipariş, İletişim, iade/teslimat/KVKK/mesafeli satış (avukat kontrolünden sonra).
6. ☐ Ürünler eklenir (fiyatlar netleşince).
7. ☐ Kargo firması ve ücretleri.
8. ☐ Alan adı ikas'a bağlanır (DNS kayıtlarını ikas verir; Shopify için girilen kayıtlar değiştirilir).
9. ☐ Test siparişi, sonra yayın. Google işletme ve Instagram bağlantıları güncellenir.

## Shopify tarafı
- Ücretsiz deneme bitmeden mağazayı kapatın/duraklatın ki ücret çıkmasın. Deneme süresi ve iptal adımlarını Shopify panelinde (Ayarlar → Plan) kontrol edin.
- DNS'e Shopify için girilen A ve CNAME kayıtlarını ikas'ın vereceği değerlerle değiştirin; Shopify kayıtlarıyla ikas kayıtları aynı anda durmasın.
- Bu repodaki Shopify teması (`yeni-tasarim` dalı) arşiv olarak kalır; silinmez.

## Notlar (7 Ekim 2026)
- Hesap açıldı: renklimozaik.myikas.com. Paket: Start (ücretsiz) ile başlanıyor.
- Start: 100 ürüne kadar, ikas Cüzdan ile %3,99 sanal POS (taksit durumu panelden doğrulanacak), özel alan adı bağlama ücretli görünüyor (899 TL, tek seferlik mi yıllık mı panelden doğrulanacak). Ücretsiz pakette yalnızca ikas'ın hazır ücretsiz temalarından biri yayınlanabilir (kaynaklara göre); diğer temalar düzenlenir ama yayınlanamaz. Panelde teyit edilecek.
- Alan adı bağlama: ikas panelinde bir A kaydı ve iki CNAME kaydı gösterir; Shopify için girilen A (23.227.38.65) ve CNAME (shops.myshopify.com) kayıtları silinir.
- Tasarım belirtimi: `docs/ikas/editor-tasarim.md`.
