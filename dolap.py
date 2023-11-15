import random

class Urun:
    urun_listesi = []   
    satilan_urunler = []  

    def __init__(self, isim, fiyat, adet):
        self.isim = isim
        self.fiyat = fiyat
        self.adet = adet

    def urun_goster(self):
        print(f"İsim : {self.isim}\nFiyat : {self.fiyat}\nAdet : {self.adet}\n")

    def siparis_ver(self, adet):
        if adet > self.adet:
            print(f"Yeterli stok bulunmamaktadır. Stokta {self.adet} adet bulunmaktadır.")
            return False

        print(f"Tüm Ürünler\n")
        for urun in Urun.urun_listesi:
            urun.urun_goster()

        urun_sec = input("İstediğiniz Ürün İsmi : ")

        for urun in Urun.urun_listesi:
            if urun_sec == urun.isim:
                kart_no = input("Kart Numarası Gir : ")
                kart_tarih = input("Kart Kullanma Tarihi (00/00) : ")
                kart_cvv = input("CVV Girin : ")

                # Satın alınan ürünün bilgilerini ekle
                satilan_urun = {"isim": urun.isim, "fiyat": urun.fiyat, "adet": adet}
                Urun.satilan_urunler.append(satilan_urun)

                print(f"{adet} adet ürün başarıyla sipariş edildi. Sipariş No: {random.randint(10000000, 99999999)}")
                urun.adet -= adet
                return True

        print("Ürün Bulunamadı! Bu İsimde Bir Ürün Yok")
        return False

    def urun_duzenle(self, yeni_fiyat, yeni_adet):
        self.fiyat = yeni_fiyat
        self.adet = yeni_adet
        print("Ürün bilgileri güncellendi.")

    def siparislerim():
        if not Urun.satilan_urunler:
            print("Henüz hiç ürün satın alınmamış.")
            return

        print("\nSatın Alınan Ürünler:")
        for satilan_urun in Urun.satilan_urunler:
            print(f"{satilan_urun['adet']} adet {satilan_urun['isim']} - Toplam Fiyat: {satilan_urun['adet'] * satilan_urun['fiyat']}")

urun_listesi = []

print("Ürün Ekle\nÜrünleri Göster\nÜrün Sipariş Ver\nÜrün Düzenle\nSiparişlerim\nÇıkış\n")

while True:
    cevap = input("Ne Yapmak İstersiniz : ").title()

    if cevap == "Çıkış":
        break

    if cevap == "Ürün Ekle":
        urun_ismi = input("Ürün İsmi: ")
        urun_fiyati = float(input("Ürün Fiyati: "))
        urun_adeti = int(input("Ürün Adeti: "))

        yeni_urun = Urun(urun_ismi, urun_fiyati, urun_adeti)
        Urun.urun_listesi.append(yeni_urun)

    elif cevap == "Ürünleri Göster":
        if Urun.urun_listesi:
            for urun in Urun.urun_listesi:
                urun.urun_goster()
        else:
            print("Henüz ürün eklenmemiş.")

    elif cevap == "Ürün Sipariş Ver":
        if Urun.urun_listesi:
            urun_adi = input("Hangi ürünü sipariş vermek istiyorsunuz? ")
            adet = int(input(f"Kaç adet {urun_adi} sipariş etmek istiyorsunuz? : "))

            for urun in Urun.urun_listesi:
                if urun_adi == urun.isim:
                    urun.siparis_ver(adet)
                    break
            else:
                print("Ürün bulunamadı.")
        else:
            print("Henüz ürün eklenmemiştir.")

    elif cevap == "Ürün Düzenle":
        if Urun.urun_listesi:
            urun_adi = input("Hangi ürünü düzenlemek istiyorsunuz? ")
            for urun in Urun.urun_listesi:
                if urun_adi == urun.isim:
                    yeni_fiyat = float(input(f"Yeni Fiyatı Girin: "))
                    yeni_adet = int(input(f"Yeni Adeti Girin: "))
                    urun.urun_duzenle(yeni_fiyat, yeni_adet)
                    break
            else:
                print("Ürün bulunamadı.")
        else:
            print("Henüz ürün eklenmemiştir.")

    if cevap == "Siparişlerim":
        Urun.siparislerim()
