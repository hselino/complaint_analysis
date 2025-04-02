import pandas as pd
import re

stopwords = ['ve', 'veya', 'ama', 'fakat', 'lakin', 'ancak', 'çünkü', 'zira', 'eğer', 'ise', 'ile', 'için', 'bu', 'şu', 'o', 'bir', 'da', 'de', 'den', 'dan', 'te', 'ta', 'ki', 'mi', 'ne', 'nasıl', 'neden', 'kim', 'hangi', 'nerede', 'nereden', 'nereye', 'nasıl', 'neden', 'kim', 'hangi', 'nerede', 'nereden', 'nereye', 'nasıl', 'neden', 'kim', 'hangi', 'nerede', 'nereden', 'nereye']

def normalize_text(text):
    if isinstance(text, str):
        # Küçük harfe çevir
        text = text.lower()
        # Noktalama işaretlerini kaldır
        text = re.sub(r'[^\w\s]', ' ', text)
        # Fazla boşlukları temizle
        text = re.sub(r'\s+', ' ', text)
        # Stopwords'leri kaldır
        words = text.split()
        words = [word for word in words if word not in stopwords]
        return ' '.join(words)
    return text

# CSV dosyasını oku
df = pd.read_csv('dataset kopyası.csv')

# Tüm metin sütunlarını normalize et
for column in df.columns:
    if df[column].dtype == 'object':  # Sadece metin sütunlarını işle
        df[column] = df[column].apply(normalize_text)

# Normalize edilmiş veriyi yeni bir CSV dosyasına kaydet
df.to_csv('normalized_dataset.csv', index=False)
print("Metin normalizasyonu tamamlandı. Sonuçlar 'normalized_dataset.csv' dosyasına kaydedildi.") 