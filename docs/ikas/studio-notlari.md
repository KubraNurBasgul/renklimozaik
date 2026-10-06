# ikas Studio notları (builders.ikas.com, 6 Ekim 2026'da okundu)

## Güncel sistem
- Tema geliştirme **ikas Studio** üzerinden yapılır: partners.ikas.com'da tema oluşturulur, bir **geliştirici mağazasında** (bizde dev-renklimozaik.myikas.com) açılan editörde düzenlenir.
- İki yol vardır ve aynı temada birlikte kullanılabilir: **No-code editör** (İçerik ve Tasarım modları) ve **Kod modu** (beta; yerelde Preact + JavaScript + CSS ile bölüm/bileşen yazılır; dışarıdan paket kurulamaz). Belge, emin değilseniz no-code ile başlamayı önerir.
- Yeni temada Anasayfa, 404 ve Ödeme sayfası hazır gelir; diğer sayfa tipleri editörden eklenir: Ürün, Kategori, Marka, Arama, Hesabım, Giriş, Kayıt, Adreslerim, Siparişlerim, Sipariş Detay, Favori Ürünler, Şifremi Unuttum, Şifremi Kurtar, Müşteri Mail Onaylama, Sepet, Blog (ana, kategori, yazı), Özel Sayfa. Ürün/kategori/marka/blog sayfaları için mağazada ilgili verinin önceden tanımlı olması gerekir (örn. en az bir ürün).
- Ödeme sayfası ikas'ın hazır bölümüdür; yalnızca izin verilen ayarlar değiştirilebilir.

## Yayınlama
1. Editörün sol altındaki "Temayı Yönet" ile tema partner paneline gönderilir.
2. partners.ikas.com'da ilgili tema açılır, "izin verilen mağazalar" listesine mağaza eklenir (mağazaya önce erişim alınmış olmalı).
3. Mağazada "Temalarım" altında görünür. "Satışa çıkartma" özelliği belgede "yakında" olarak geçer.
Açık: Start (ücretsiz) pakette partner temasının yayınlanıp yayınlanamayacağı belgelerden anlaşılmıyor; test edilecek.

## Kod modu notları
- `npm install ikas -g` (CLI 0.0.30), `ikas theme init -e <editör-url>`, sonra proje klasöründe `ikas theme dev`; açılan sekmede "Bağlan".
- CLI girişi tarayıcıda OAuth ile yapar (geri çağırma adresi 127.0.0.1); bulut ortamında tarayıcı olmadığı için giriş ve canlı önizleme (yerel geliştirme sunucusu + "Bağlan") kullanıcının kendi bilgisayarında yapılmalıdır.
- Proje Preact tabanlıdır (Next.js değil); `src/components/<Bileşen>/index.tsx`, `styles.css`, `src/global.css`. `ikas.config.json`, `types.ts` dosyaları otomatik üretilir, elle düzenlenmez.

## Karar (6 Ekim 2026, güncel)
Özel tema (Studio/Kod modu) yapılmaz. Mağazanın kendi **ücretsiz temaları** incelenir, en uygun olan seçilip onun düzenleyicisinde `docs/ikas/editor-tasarim.md` belirtimine göre özelleştirilir. Arzu Arslan ileride geliştirmek isterse özel tema yeniden konuşulur.

Tema seçim ölçütleri: ana sayfada görsel + metin giriş bölümü, kare koleksiyon kartları, sade ve açık arka plan, serif başlık yazı tipine uyum, büyük ürün fotoğrafı ve galeri olan ürün sayfası, telefonda düzgün görünüm, ücretsiz pakette yayınlanabilir olması. Sektör etiketlerine göre ev dekorasyonu/mobilya (Stella), takı ve kişisel bakım (The Nile), organik ve doğal ürünler (Siva) ve aksesuar (Toros) adayları öne çıkıyor; panelde doğrulanacak.
