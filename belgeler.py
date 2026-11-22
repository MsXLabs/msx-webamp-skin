import sys, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '_ortak'))
import yardimci as y
os.chdir(HERE)
y.mit('.')
y.yaz('README.md', """# MsXLabs Mavi Karanlık — klasik (Winamp 2 uyumlu) skin

**Türkçe** · [English below](#english)

Koyu lacivert zemin, altın vurgulu, tamamen **özgün çizilmiş** klasik `.wsz` skin. Winamp 2 skin biçimini destekleyen oynatıcılarda
(ör. [Webamp](https://webamp.org), Winamp 2.x/5.x uyumlu oynatıcılar) çalışır. Türkçe karakterler (ç ş ğ ı ü ö İ) metin
sprite'ında desteklenir; başlıklar "MSX PLAYER / MSX DALGA / MSX LİSTE", düğme etiketleri Türkçedir.

![önizleme](screenshots/webamp-onizleme.png)

## Kurulum
- **Webamp / skins.webamp.org:** `msx-mavi-karanlik.wsz` dosyasını sayfaya sürükleyin ya da `initialSkin: { url }` verin.
- **Winamp 2 uyumlu oynatıcılar:** dosyayı `Skins` klasörüne kopyalayın, skin menüsünden seçin.
- **Yerel önizleme:** `onizleme/index.html` (yönerge dosya içinde; `webamp@2.3.1` MIT).

## Telif / özgünlük
Tüm bitmap'ler MsXLabs tarafından çizildi; Winamp, Nullsoft veya üçüncü taraf skin görseli içermez. "Winamp" adı yalnızca *biçim
uyumluluğunu* belirtmek için kullanılır; bu skin Winamp/Nullsoft/Webamp ile bağlantılı değildir ve onların onayını iddia etmez.
Görseller ve skin: MIT (bkz. `LICENSE`). Yazı tipi gömülü değil (bitmap).

## Lisans
MIT. Yapım: **MsXLabs — https://www.msxlabs.org**

---

## English
A fully **original** classic `.wsz` skin: deep navy with gold accents, Turkish-aware text sprites (ç ş ğ ı ü ö İ) and Turkish
button labels. Works in players that support the Winamp 2 skin format, e.g. [Webamp](https://webamp.org).

**Install:** drag `msx-mavi-karanlik.wsz` onto Webamp, or put it in your player's `Skins` folder and select it.
**Originality:** every bitmap was drawn by MsXLabs; no Winamp/Nullsoft or third-party skin artwork. "Winamp" appears only to
describe *format compatibility*; no affiliation or endorsement is claimed.
**License:** MIT — see `LICENSE`. By **MsXLabs — https://www.msxlabs.org**
""")
y.yaz('CHANGELOG.md', "# Changelog\n\n## 1.0.0 — 2026-11-22\n- İlk yayın paketi: ana pencere, EQ, liste, dalga (visualizer) ve imleçler dahil 44 dosyalık skin.\n- Initial release package: 44-file skin incl. main, EQ, playlist, visualizer sprites and cursors.\n")
y.gonderim('.', 'Winamp Skin Museum (skins.webamp.org) — yükleme',
 "Ücretsiz; müzede yükleme için hesap gerekmeyebilir (**[DOĞRULANMADI]** — yükleme sayfası elle kontrol edilmeli). Yüklenen skin Internet Archive'a da gider.",
 "Ön inceleme yok gibi; yüklemeden sonra önizleme sunucuda üretilir. Süre **[DOĞRULANMADI]**.",
 "Skin sayfasında yazar adı/bağlantı alanı **[DOĞRULANMADI]**. Skin içindeki başlıklar zaten 'MSX'. Kredi: **MsXLabs — https://www.msxlabs.org** README'de.",
 "1. skins.webamp.org → Upload → `msx-mavi-karanlik.wsz`.\n2. Skin müzesi sayfasının URL'sini `YAYIN-DEFTERI.md`'ye ekle.\n3. (İsteğe bağlı) Webamp Discord/GitHub topluluğuna kısa duyuru — owner onayıyla.",
 "MsXLabs Mavi Karanlık: koyu lacivert + altın, Türkçe karakter destekli, tamamen özgün klasik skin. Winamp/Nullsoft görseli içermez.",
 "MsXLabs Mavi Karanlık: deep navy + gold, Turkish-aware, fully original classic skin. Contains no Winamp/Nullsoft artwork.")
sha = y.sha256('msx-mavi-karanlik.wsz')
y.yaz('KANIT.md', f"""# Kanıt (22 Kas 2026)
- `msx-mavi-karanlik.wsz` (44 dosya, ~0,97 MB) SHA256: {sha}. Kaynak: MK Player'ın özgün klasik skin'i (`msx-mavikaranlik-klasik.wsz`).
- Yerel önizleme: `webamp@2.3.1` (MIT) paketiyle statik sunucuda `onizleme/index.html`; skin yüklendi, 3 pencere (ana/EQ/liste) çizildi, konsol hatası yok.
  Ekran görüntüsü `screenshots/webamp-onizleme.png` (2x ölçek, işlenmemiş).
- Özgünlük: bitmap'ler önizlemede gözle denetlendi — "MSX PLAYER/DALGA/LİSTE" başlıkları, Türkçe düğme etiketleri, özgün düğme ve zemin çizimi; Winamp varsayılan skin görseli yok. İçindeki `PLEDIT.TXT` renkleri site paletindedir.
- Not: önizleme kayan yazısındaki "WINAMP 2.91" metni Webamp'ın kendi varsayılan metnidir, skin'e ait değildir.
- Sır/özel veri taraması: bkz. `../TARAMA.md`.
""")
