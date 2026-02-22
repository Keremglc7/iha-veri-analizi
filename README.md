# İHA Uçuş Verisi Analiz Sistemi 🚁 (UAV Flight Data Analyzer)

Bu proje, Python kullanılarak geliştirilmiş bir veri bilimi (Data Science) simülasyonudur. İnsansız hava araçlarına ait uçuş konumları ve irtifa verileri rastgele simüle edilerek Pandas kütüphanesi ile analiz edilmiştir.

## 🚀 Özellikler (Features)
- **Veri Simülasyonu:** Numpy ile 100 farklı uçuş için rastgele irtifa ve görev bölgesi üretimi.
- **Veri Manipülasyonu:** Pandas DataFrame ile verilerin tablolaştırılması ve bölgesel bazda gruplandırılarak (groupby) analiz edilmesi.
- **Kritik Durum Tespiti:** Belirlenen kritik sınırın (1000m) altında kalan riskli uçuşların filtrelenmesi.
- **Dışa Aktarım:** OS kütüphanesi kullanılarak analiz sonuçlarının ve filtrelenmiş verilerin UTF-8 formatında `.csv` dosyası olarak kaydedilmesi.

## 🛠️ Kullanılan Teknolojiler (Tech Stack)
- Python 3.x
- Pandas
- Numpy
- OS (İşletim sistemi dosya işlemleri)
