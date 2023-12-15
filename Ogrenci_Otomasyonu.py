class Ogrenci:
    def __init__(self, isim, yas, notu):
        self.isim = isim
        self.yas = yas
        self.notu = notu

    def __str__(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Notu: {self.notu}"


class OgrenciYonetici:
    def __init__(self):
        # Öğrencileri depolamak için boş bir liste başlat
        self.ogrenci_listesi = []

    def ogrenci_ekle(self):
        isim = input("Öğrenci İsmi: ")
        yas = int(input("Öğrenci Yaşı: "))
        notu = float(input("Öğrenci Notu: "))

        yeni_ogrenci = Ogrenci(isim, yas, notu)
        self.ogrenci_listesi.append(yeni_ogrenci)

    def ogrencileri_goruntule(self):
        for ogrenci in self.ogrenci_listesi:
            print(ogrenci)

    def dosyaya_kaydet(self, dosya_adi):
        with open(dosya_adi, "w") as dosya:
            for ogrenci in self.ogrenci_listesi:
                dosya.write(f"{ogrenci.isim},{ogrenci.yas},{ogrenci.notu}\n")

    def dosyadan_yukle(self, dosya_adi):
        with open(dosya_adi, "r") as dosya:
            for satir in dosya:
                # Satırdaki verileri ayırarak öğrenci özelliklerini al
                isim, yas, notu = satir.strip().split(',')
                yeni_ogrenci = Ogrenci(isim, int(yas), float(notu))
                self.ogrenci_listesi.append(yeni_ogrenci)

def kullanici_menu():
    yonetici = OgrenciYonetici()

    while True:
        print("\nÖğrenci Dosya Yönetim Sistemi:")
        print("1. Yeni bir öğrenci ekleyin")
        print("2. Öğrencileri görüntüleyin")
        print("3. Öğrencileri bir dosyaya kaydedin")
        print("4. Öğrencileri bir dosyadan yükleyin")
        print("5. Çıkış")

        c = int(input("Menudan bir rakam seçiniz: "))

        if c == 1:
            yonetici.ogrenci_ekle()
        elif c == 2:
            yonetici.ogrencileri_goruntule()
        elif c == 3:
            dosya_adi = input("Dosya adını giriniz: ")
            yonetici.dosyaya_kaydet(dosya_adi)
        elif c == 4:
            dosya_adi = input("Dosya adını giriniz: ")
            yonetici.dosyadan_yukle(dosya_adi)
        elif c == 5:
            break
        else:
            print("Yanlış bir değer girdiniz.")

if __name__ == "__main__":
    kullanici_menu()
