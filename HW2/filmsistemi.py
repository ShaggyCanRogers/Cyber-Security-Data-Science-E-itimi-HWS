class FilmKaydedici:
    def __init__(self, dosya_adı):
        self.dosya_adı = dosya_adı

    def film_kaydet(self):
        film_adı = input("Film adı: ")
        film_türü = input("Film türü: ")

        with open(self.dosya_adı, "a") as dosya:
            dosya.write(f"{film_adı},{film_türü}\n")

        print("Film kaydedildi.")

    def film_ara(self):
        film_adı = input("Aranacak film adı: ")

        with open(self.dosya_adı, "r") as dosya:
            for satır in dosya:
                veriler = satır.strip().split(",")
                kaydedilen_film_adı = veriler[0]

                if film_adı.lower() == kaydedilen_film_adı.lower():
                    print("Film bulundu.")
                    print("Film detayları:")
                    print(f"Adı: {kaydedilen_film_adı}")
                    print(f"Türü: {veriler[1]}")
                    return

        print("Film bulunamadı.")

    def film_sil(self):
        film_adı = input("Silinecek film adı: ")

        dosya_degisti = False

        with open(self.dosya_adı, "r") as dosya:
            veriler = dosya.readlines()

        with open(self.dosya_adı, "w") as dosya:
            for satır in veriler:
                satır = satır.strip()
                if satır:
                    veri = satır.split(",")
                    kaydedilen_film_adı = veri[0].strip()

                    if film_adı.lower() == kaydedilen_film_adı.lower():
                        dosya_degisti = True
                    else:
                        dosya.write(satır + "\n")

        if dosya_degisti:
            print("Film silindi.")
        else:
            print("Film bulunamadı.")

    def calistir(self):
        while True:
            print("Film Kaydetme Programı")
            print("1. Film Kaydet")
            print("2. Film Ara")
            print("3. Film Sil")
            print("4. Çıkış Yap")

            secim = input("Seçiminizi yapın (1-4): ")

            if secim == "1":
                self.film_kaydet()
            elif secim == "2":
                self.film_ara()
            elif secim == "3":
                self.film_sil()
            elif secim == "4":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")


FilmKaydedici("filmler.txt").calistir()
