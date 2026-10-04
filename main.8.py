class Inson:
    def __init__(self, ism):
        self.ism = ism

    def malumot(self):
        print(self.ism)


class Talaba(Inson):
    def oqish(self):
        print("Talaba o'qiyapti")


class Oquvchi(Talaba):
    def dars(self):
        print("O'quvchi dars qilmoqda")


class Student(Oquvchi):
    def imtihon(self):
        print("Imtihon topshirmoqda")


class Universitet(Student):
    def universitet(self):
        print("Universitetda o'qiydi")


class Fakultet(Universitet):
    def fakultet(self):
        print("Fakultet")


class Guruh(Fakultet):
    def guruh(self):
        print("Guruh")


class Kurs(Guruh):
    def kurs(self):
        print("Kurs")


class Fan(Kurs):
    def fan(self):
        print("Python fani")


class Oqituvchi(Fan):
    def oqituvchi(self):
        print("O'qituvchi")


class Dars(Oqituvchi):
    def dars_vaqti(self):
        print("Dars vaqti")


class Xona(Dars):
    def xona(self):
        print("205-xona")


class Bino(Xona):
    def bino(self):
        print("A bino")


class Kutubxona(Bino):
    def kutubxona(self):
        print("Kutubxona")


class Kitob(Kutubxona):
    def kitob(self):
        print("Python kitobi")


class Imtihon(Kitob):
    def imtihon_test(self):
        print("Python imtihoni")


class Baho(Imtihon):
    def baho(self):
        print("95 ball")


class Sertifikat(Baho):
    def sertifikat(self):
        print("Sertifikat")


class Kompyuter(Sertifikat):
    def kompyuter(self):
        print("Lenovo")


class Login(Kompyuter):
    def login(self):
        print("Akbar123")


class UniversitetTizimi(Login):
    def tizim(self):
        print("Universitet tizimi")



a = UniversitetTizimi("Akbar")

a.malumot()
a.oqish()
a.dars()
a.imtihon()
a.universitet()
a.fakultet()
a.guruh()
a.kurs()
a.fan()
a.oqituvchi()
a.dars_vaqti()
a.xona()
a.bino()
a.kutubxona()
a.kitob()
a.imtihon_test()
a.baho()
a.sertifikat()
a.kompyuter()
a.login()
a.tizim()