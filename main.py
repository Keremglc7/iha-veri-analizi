import pandas as pd
import numpy as np
import random
import os

print("İHA Uçuş Kontrol Sistemine Bağlanılıyor...")

ucus_sayisi = 100
ucus_numaralari = range(1, ucus_sayisi + 1)

irtifalar = np.random.randint(500 , 3000, size=ucus_sayisi)

bolgeler = ["Teknopark","Pendik Sahil","Sabiha Gökçen Hava Sahası","Gebze"]

konumlar= random.choices(bolgeler, k=ucus_sayisi)

df = pd.DataFrame({
    "ucus_no": ucus_numaralari,
    "Konum": konumlar,
    "irtifa_m": irtifalar
})


max_irtifa = df["irtifa_m"].max()
min_irtifa = df["irtifa_m"].min()
ortalama_irtifa = df["irtifa_m"].mean()

kritik_ucuslar = df[df["irtifa_m"] < 1000]

konum_istatistikleri = df.groupby("Konum")["irtifa_m"].mean().round(1)

print("-" * 50)
print("İHA İRTİFA VE KONUM ANALİZ RAPORU")
print("-" * 50)
print(f"Toplam Gerçekleşen Uçuş: {ucus_sayisi}")
print(f"Maksimum İrtifa: {max_irtifa}m | Minimum İrtifa: {min_irtifa}m")
print(f"Genel İrtifa Ortalaması: {ortalama_irtifa:.1f}m\n")

print("BÖLGESEL ORTALAMALAR:")
print(konum_istatistikleri)
print("\n" + "-" * 50)

if len(kritik_ucuslar) > 0:
    print(f"DİKKAT! 1000m altına inilen {len(kritik_ucuslar)} adet kritik uçuş tespit edildi!")
else:
    print("Tüm uçuşlar güvenli irtifada gerçekleşti.")
print("\n" + "="*50)


print("KAYIT İŞLEMİ")

masaustu_yolu = os.path.expanduser("~/Desktop")
rapor_yolu = f"{masaustu_yolu}/iha_ucus_raporu.csv"
kritik_yolu = f"{masaustu_yolu}/kritik_ucuslar_uyari.csv"

df.to_csv(rapor_yolu, index=False, encoding="utf-8-sig")
kritik_ucuslar.to_csv(kritik_yolu, index=False, encoding="utf-8-sig")

print("BAŞARILI! Dosyalar direkt olarak Masaüstüne kaydedildi.")