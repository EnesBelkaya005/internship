iptal_edilen_kartlar = {"X123", "B789", "Z999"}
onaylananlar = []
reddedilenler = []
while True:
    isim = input("Kişinin adını girin (çıkmak için 'bitti' yazın): ")
    if isim.lower() == "bitti":
        break

    kart = input("Kart numarasını girin: ").strip().upper()

    if kart in iptal_edilen_kartlar:
        reddedilenler.append(isim)
        print(f"[ERİŞİM REDDEDİLDİ] {isim} - İptal edilmiş kart")
    else:
        onaylananlar.append(isim)
        print(f"[ERİŞİM ONAYLANDI] {isim}")

print("Girişine İzin Verilenler:")
for kisi in sorted(onaylananlar):
    print(f" - {kisi}")
print(" Girişi Reddedilenler:")
for kisi in sorted(reddedilenler):
    print(f" - {kisi}")
print(f"Toplam Onaylanan: {len(onaylananlar)}")
print(f"Toplam Reddedilen: {len(reddedilenler)}")