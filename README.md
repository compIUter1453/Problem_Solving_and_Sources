# Problem Solving and Sources

Bu repo, DSA (Data Structures and Algorithms) soru cozumlerini tek bir yerde toplamak icin hazirlandi.
Amac, LeetCode, AlgoLeague ve benzeri platformlardan cozulmus sorulari duzenli bir yapiyla paylasmaktir.

## Cozumler

- Repo ici liste: [Problems.md](./Problems.md)

## Hedef

- Cozulen sorulari konu bazli klasorlerde tutmak
- Coklu dil destegi saglamak (C++, Python vb.)
- Her cozum icin standart bir aciklama sunmak

## Klasor Kurali

Her soru, cozuldugu yontemin/konunun klasorune eklenmelidir.

Ornek konu klasorleri:
- `dp/`
- `graph/`
- `array/`
- `string/`
- `binary-search/`

Not: Su an repoda `-nzva-main/dp/` klasoru mevcut. Yeni konular icin ayni duzen korunabilir.

## Dosya Isimlendirme

Dosya adlari acik ve aratmasi kolay olmali:

- `TwoSum.cpp`
- `LongestIncreasingSubsequence.py`
- `DijkstraShortestPath.cpp`

## Cevap Eklerken

1. Soruyu uygun konu klasorune ekle.
2. `PROBLEM_TEMPLATE.md` dosyasindaki formati doldur.
3. Cozum kodunu ayni konu klasorune koy.
4. Gerekirse zaman ve bellek karmasikligini belirt.

## Request (PR) Tipi

Yeni cozum eklerken pull request acarken asagidaki tiplerden birini sec:

- `solution`: Yeni soru cozumu eklendi
- `improvement`: Mevcut cozume optimizasyon veya okunabilirlik iyilestirmesi
- `fix`: Hatali cozum duzeltildi
- `docs`: README, template veya dokumantasyon guncellendi

`.github/pull_request_template.md` dosyasini kullanarak standart bir PR acabilirsin.

## Kisa Ornek

- Soru: `Coin Change`
- Konu: `dp`
- Kod: `-nzva-main/dp/CoinChange.cpp`
- Aciklama: `-nzva-main/dp/CoinChange.md` (opsiyonel)
