#AD: WAHIB HAEL ABDULWARETH MOQBEL 
#NO: 20360859109

import os


class Account:

    def __init__(self, account_type, account_name, balance):
        self._account_type = account_type
        self._account_name = account_name
        self._balance = balance

    @property
    def account_type1(self):
        return self._account_type

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Hesap bakiyesi negatif olamaz.")
        self._balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetersiz bakiye.")
        else: 
            self.balance -= amount

    def close_account(self):
        if self.account_type == "SavingAccount":
            closing_fee = self.balance * 0.10
            self.balance -= closing_fee
            print(f"{self.account_name} Hesabı kapatıldı.(SavingAccount olmasından %10 eksilir). Elde edilen para miktarı : {closing_fee}")
            print(f"Kalan bakiyeniz : {self.balance}")
            return closing_fee
        elif self.account_type == "NormalAccount":
            print(f"Hesap Adı: {self.account_name}, Hesap Miktarı: {self.balance}")
            print(f"{self.account_name} Hesabı başarıyla kapatıldı ")
            return self.balance

class Transaction:
    def __init__(self, account_name, amount):
        self.account_name = account_name
        self.amount = amount

    def para_dondur(self):
        pass

def para_cek(amount):
    if amount < 0:
        raise ValueError("Negatif miktar çekilemez.")
    return -amount

def para_ekle(amount):
    if amount < 0:
        raise ValueError("Negatif miktar eklenemez.")
    return amount

def para_guncelle(account, transaction):
    if transaction.amount < 0:
        account.withdraw(-transaction.amount)
    else:
        account.deposit(transaction.amount)

def hesap_kapat(account):
    account.close_account()

def hesap_olustur():
    while True:
        account_name = input("Hesap Adı: ")

        while True:
            try:
                account_type = input("Hesap Türü seçiniz (SavingAccount/NormalAccount): ")
                if account_type not in ["SavingAccount", "NormalAccount"]:
                    raise ValueError("Geçersiz hesap türü.")
                break
            except ValueError:
                print("Geçersiz hesap türü. Lütfen tekrar girininiz.")

        while True:
            try:
                initial_balance = float(input("Hesap başlangıç miktarı: "))
                if initial_balance < 0:
                    raise ValueError("Hesap bakiyesi negatif olamaz.")
                break
            except ValueError:
                print("Geçersiz miktar. Lütfen pozitif bir miktar girininiz.")

        account = Account(account_type, account_name, initial_balance)
        return account

def kaydet(account_list):
    current_dir = os.getcwd()
    print("Suanki çalışan directory :", current_dir)
    file_path = "hesaplar.txt"

    with open(file_path, "w+") as file:
        for account in account_list:
            file.write(f"{account.account_type},{account.account_name},{account.balance}\n")
    print(f"Hesaplar dosyaya kaydedildi: {os.path.abspath(file_path)}")

def yukle():
    account_list = []
    file_path = "hesaplar.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                account_type, account_name, balance = data
                account = Account(account_type, account_name, float(balance))
                account_list.append(account)
        print(f"Hesaplar dosyadan yüklendi: {os.path.abspath(file_path)}")
    else:
        print("Hesaplar dosyası bulunamadı. Yeni bir dosya oluşturulacak.")
    return account_list

def read_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def menu():
    account_list = []

    while True:
        print("--------> İŞLEM MENÜSÜ <--------")
        print("1. Hesap oluştur.")
        print("2. Hesap kapat.")
        print("3. Kaydet ve yükle.")
        print("4. Para çek.")
        print("5. Para yükle.")
        print("6. Göster.")
        print("0. Çıkış.")
        choice = input("İşlem numarasını giriniz: ")

        if choice == "1":
            account = hesap_olustur()
            if account:
                account_list.append(account)

        elif choice == "2":
            account_name = input("Hesap Adı: ")
            for account in account_list:
                if account.account_name == account_name:
                    hesap_kapat(account)
                    account_list.remove(account)
                    break
            else:
                print("Hesap bulunamadı.")

        elif choice == "3":
            kaydet(account_list)
            account_list = yukle()

        elif choice == "4":
            while True:
                account_name = input("Hesap Adı: ")
                amount = read_float_input("Miktar giriniz: ")
                if amount < 0:
                    print("Negatif miktar çekilemez.")
                    continue
                transaction = Transaction(account_name, para_cek(amount))
                for account in account_list:
                    if account.account_name == transaction.account_name:
                        para_guncelle(account, transaction)
                        break
                else:
                    print("Hesap bulunamadı.")
                break

        elif choice == "5":
            while True:
                account_name = input("Hesap Adı: ")
                amount = read_float_input("Miktar giriniz: ")
                transaction = Transaction(account_name, para_ekle(amount))
                for account in account_list:
                    if account.account_name == transaction.account_name:
                        para_guncelle(account, transaction)
                        break
                else:
                    print("Hesap bulunamadı.")
                break

        elif choice == "6":
            if not account_list: 
                print("Gösterilecek Hesap yok. ")
            else: 
                for account in account_list:
                    print(f"Hesap Adı: {account.account_name}, Hesap Türü: {account.account_type}, Bakiye: {account.balance}")
        
        elif choice == "0":
            break
            
        else:
            print("Geçersiz işlem numarası.")

if __name__ == "__main__":
    menu()
