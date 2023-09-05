Ogrenciler = []

class Okul():
    def __init__(self,name,surname,number,**kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        for key, value in kwargs.items():
            setattr(self, key, value)
        

    def show_info(self):
        print(f"""
        Ad: {self.name}
        Soyad: {self.surname}
        Numara: {self.number}
""")



class Ekle(Okul):
    def __init__(self, name="", surname="", number="", **kwargs):
        super().__init__(name, surname, number, **kwargs)
        ad = input("Öğrencinin adını girin: ")
        soyad = input("Öğrencinin soyadını girin: ")
        numara = input("Öğrencinin numarasını girin: ")
        if self.name == ad and self.surname == surname:
            print("Bu isim önceden alınmış")
        elif self.number == number:
            print("Numara başka bir öğrencininkiyle aynı olamaz")
        ogrenci = Okul(name=ad, surname=soyad, number=numara)
        Ogrenciler.append(ogrenci)
        print("Öğrenci başarıyla eklendi!")
    

a = Ekle()
