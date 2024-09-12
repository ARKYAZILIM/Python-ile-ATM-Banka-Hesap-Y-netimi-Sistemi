class BankaHesabi:
    def __init__(self, hesap_no, sifre, bakiye=0):
        self.hesap_no = hesap_no
        self.sifre = sifre
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.bakiye} TL")

    def bakiye_goruntule(self):
        print(f"Güncel bakiye: {self.bakiye} TL")


class ATM:
    def __init__(self):
        self.hesaplar = {}

    def hesap_ekle(self, hesap):
        self.hesaplar[hesap.hesap_no] = hesap

    def giris(self, hesap_no, sifre):
        hesap = self.hesaplar.get(hesap_no)
        if hesap and hesap.sifre == sifre:
            print(f"{hesap_no} ile giriş yapıldı.")
            return hesap
        else:
            print("Hatalı giriş!")
            return None


atm = ATM()
atm.hesap_ekle(BankaHesabi("1234", "pass123", 500))
atm.hesap_ekle(BankaHesabi("5678", "pass456", 1000))

hesap_no = input("Hesap numaranızı girin: ")
sifre = input("Şifrenizi girin: ")
hesap = atm.giris(hesap_no, sifre)

if hesap:
    while True:
        print("\n1. Para Yatır\n2. Para Çek\n3. Bakiye Görüntüle\n4. Çıkış")
        secim = int(input("Seçiminiz: "))

        if secim == 1:
            miktar = float(input("Yatırılacak miktarı girin: "))
            hesap.para_yatir(miktar)
        elif secim == 2:
            miktar = float(input("Çekilecek miktarı girin: "))
            hesap.para_cek(miktar)
        elif secim == 3:
            hesap.bakiye_goruntule()
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")
