# 1
class Telefon:
    def __init__(self, model):
        self.model =model

    def qongiroq(self):
        print("qongiroq qilinmoqda")

class Smartfon(Telefon):
    def qongiroq(self):
        print("Video qo‘ng‘iroq")

a = Smartfon("Ipohone")
a.qongiroq()

# 2
class Ota:
    def __init__(self, name):
        self.ism = name

    def gapir(self):
        print("Gapir")

class Bola(Ota):
    def gapir(self):
        super().gapir()
        print("O'g'il gapir")

a = Bola("Sobr")
a.gapir()

# # 3
class Sportchi:
    def __init__(self, ism):
        self.ism = ism

    def oyin(self):
        print("O‘ynayapti", end="")

class Futbolchi(Sportchi):
    def oyin(self):
        super().oyin()
        print(", futbol o‘ynayapti")

a = Futbolchi("Messi")
a.oyin()

# # 4
class Kompyuter:
    def __init__(self, nomi):
        self.nomi = nomi

    def yoqish(self):
        print("Yoqildi")

class Noutbuk(Kompyuter):
    def yoqish(self):
        print("Noutbuk ishga tushdi")

a1 = Kompyuter("HP")
a2 = Noutbuk("Dell")

a1.yoqish()
a2.yoqish()

# # 5
class Ustoz:
    def __init__(self, ism):
        self.ism = ism

    def dars(self):
        print("Dars o‘tmoqda", end="")

class MatematikaUstoz(Ustoz):
    def dars(self):
        super().dars()
        print(", matematika darsi")

a = MatematikaUstoz("Ali")
a.dars()
