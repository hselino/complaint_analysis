from zeyrek import MorphAnalyzer
import pandas as pd

def kok_ayir(kelime):
    analyzer = MorphAnalyzer()
    try:
        # Kelimeyi analiz et
        sonuclar = analyzer.analyze(kelime)
        if sonuclar:
            # İlk sonucu al (genellikle en olası kök)
            kok = sonuclar[0].stem
            return kok
        return kelime
    except:
        return kelime

def metin_kok_ayir(metin):
    if isinstance(metin, str):  # Metin string tipinde ise işle
        # Metni kelimelere ayır
        kelimeler = metin.split()
        # Her kelimeyi köküne ayır
        kokler = [kok_ayir(kelime) for kelime in kelimeler]
        return ' '.join(kokler)
    return ""  # String değilse boş string döndür

# CSV dosyasını oku
df = pd.read_csv('normalized_dataset.csv')

# complaint_text sütunundaki her metni köklerine ayır
df['complaint_text_kokler'] = df['complaint_text'].apply(metin_kok_ayir)

# Sonuçları yeni bir CSV dosyasına kaydet
df.to_csv('koklerine_ayrilmis_dataset.csv', index=False)
print("İşlem tamamlandı. Sonuçlar 'koklerine_ayrilmis_dataset.csv' dosyasına kaydedildi.")

# Örnek kullanım
if __name__ == "__main__":
    # Test için örnek metin
    test_metni = "Kitaplarımı okumayı çok seviyorum."
    print("Orijinal metin:", test_metni)
    print("Köklerine ayrılmış hali:", metin_kok_ayir(test_metni)) 