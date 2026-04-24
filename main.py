#2-m
class Sonlar:
    def __init__(self, ovqati, uxlai, yuri):
        self.ovqati = ovqati
        self.uxlai = uxlai
        self.yuri = yuri
        
    def ovqat(self):
        print(self.ovqati)
        
    def uxla(self):
        print(f"{self.ovqati} {self.uxlai}")
        
    def yur(self):
        print(f"{self.uxlai} {self.yuri}")
        
u1 = Sonlar("Hayvon ovqat yeydi", "Hayvon uxlaydi", "Hayvon yuradi")
u1.ovqat()
u1.uxla()
u1.yur()
