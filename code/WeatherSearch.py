import pandas as pd
df = pd.read_csv('Weather_Data202212_1h.csv')
df = df[:-1] # pandas taulukon viimeinen rivi pois

HakuTulokset = []

class SaaTulostus:
    def tulostus_haku(self, HakuTulokset):
        for haku in HakuTulokset:
            print()
            print("**************************************")
            print("Sää tiedon haku tulokset joulukuu 2022")   
            print("Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema")
            print("***************************************************************")
            print(f"{haku.haut}. Haku joulukuun {haku.paiva} päivä kellon ajalle {haku.klo}")
            print(f"{haku.tulosta_haku()}")
            print()

class SaaHaku:
    def __init__(self, haut, paiva, klo):
        self.haut = haut
        self.paiva = paiva
        self.klo = klo

    def ask_paiva(self):
        def paiva_tarkistus():
            while True:
                try:
                    paiva = int(input("Anna haku päivä (1-31): "))
                    if paiva >= 1 and paiva <= 31:
                        return int(paiva) # palutetaan päivän haku arvo funktiolle
                    else:
                        print()
                        print("Virheellinen syöte. Anna oikea päivä kiitos.")
                        print()
                except ValueError:
                    print()
                    print("Virheellinen syöte. Anna luku päivänä kiitos.")
                    print()
        self.paiva = paiva_tarkistus()    

    def ask_klo(self):
        while True:
            klo = str(input("Anna haun kellon aika(HUOM! haku aika tasa tunnein 00:00 muodossa): "))
            result = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00",
            "12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
            kloTemp = []
            kloTemp.append(klo)
            if any(same_value in result for same_value in kloTemp): # jos sama arvo löytyy molemmista taulukoista klo syöte ok. 
                self.klo = klo
                break
            else:
                print()
                print("virheellinen syöte kellon ajassa")
                print()

class Lampotila(SaaHaku):
    def __init__(self, haut, paiva, klo, lampotilan_tulostus):
        super().__init__(haut, paiva, klo)
        self.lampotila_tulos = lampotilan_tulostus

    def tee_haku(self):
        paiva_1 = df[df["Klo"] == self.klo] # pandas taulukko parsitaan annetulla klo arvolla
        paiva_2 = paiva_1[paiva_1["Pv"] == self.paiva] #parsitaan annetulla paivan arvolla  
    
        a = paiva_2["Ilman lämpötila (degC)"] # valitaan parsitulta riviltä lämpötila
        a = (a.to_string(index=False)) # Tulostuksen muotoilu pandas taulukon indeksi numerointi pois
        lampotilan_tulostus = (f"Lämpötila {a} astetta")
        self.lampotila_tulos = lampotilan_tulostus 

    def tulosta_haku(self):
        return self.lampotila_tulos

class Sademaara(SaaHaku):
    def __init__(self, haut, paiva, klo, sademaaran_tulostus):
        super().__init__(haut, paiva, klo)
        self.sademaara_tulos = sademaaran_tulostus

    def tee_haku(self):
        paiva_1 = df[df["Klo"] == self.klo]
        paiva_2 = paiva_1[paiva_1["Pv"] == self.paiva]

        a = paiva_2["Sademäärä (mm)"]
        a = (a.to_string(index=False))
        sademaaran_tulostus = (f"Sademäärä {a} mm")
        self.sademaara_tulos = sademaaran_tulostus

    def tulosta_haku(self):
        return self.sademaara_tulos

class TuulenNopeus(SaaHaku):
    def __init__(self, haut, paiva, klo, tuulennopeus_tulostus):
        super().__init__(haut, paiva, klo)
        self.tuulennopeus_tulos = tuulennopeus_tulostus
        
    def tee_haku(self):
        paiva_1 = df[df["Klo"] == self.klo]
        paiva_2 = paiva_1[paiva_1["Pv"] == self.paiva]

        a = paiva_2["Tuulen nopeus (m/s)"]
        a = (a.to_string(index=False))
        tuulennopeus_tulostus = (f"Tuulen nopeus {a} m/s")
        self.tuulennopeus_tulos = tuulennopeus_tulostus

    def tulosta_haku(self):
        return self.tuulennopeus_tulos

class TuuliPuuskassa(SaaHaku):
    def __init__(self, haut, paiva, klo, tuulipuuskassa_tulostus):
        super().__init__(haut, paiva, klo)
        self.tuulipuuskassa_tulos = tuulipuuskassa_tulostus
       
    def tee_haku(self):
        paiva_1 = df[df["Klo"] == self.klo]
        paiva_2 = paiva_1[paiva_1["Pv"] == self.paiva]

        a = paiva_2["Puuskanopeus (m/s)"]
        a = (a.to_string(index=False))
        tuulipuuskassa_tulostus = (f"Tuuli puuskassa {a} m/s")
        self.tuulipuuskassa_tulos = tuulipuuskassa_tulostus

    def tulosta_haku(self):
        return self.tuulipuuskassa_tulos  

class TuuliSuunta(SaaHaku):
    def __init__(self, haut, paiva, klo, tuulisuunta_tulostus):
        super().__init__(haut, paiva, klo)
        self.tuulisuunta_tulos = tuulisuunta_tulostus
        
    def tee_haku(self): 
        paiva_1 = df[df["Klo"] == self.klo]
        paiva_2 = paiva_1[paiva_1["Pv"] == self.paiva]

        a = paiva_2["Tuulen suunta (deg)"]
        a = int(a.to_string(index=False)) # varmistetaan muuttujan int tyyppi if hakua varten

        if (a >= 338) or (a <= 22): # Pohjoinen 338 - 360 tai 0 - 22
            tuulisuunta_tulostus = (f"Pohjoistuulta suunnasta {a} astetta")       
        elif (a >= 23) and (a <= 67): # Koillinen 23 - 67
            tuulisuunta_tulostus = (f"Koillistuulta suunnasta {a} astetta") 
        elif (a >= 68) and (a <= 112): # Itä 68 - 112
            tuulisuunta_tulostus = (f"Itätuulta suunnasta {a} astetta")
        elif (a >= 113) and (a <= 157): # Kaakko 113 - 157
            tuulisuunta_tulostus = (f"Kaakkoistuulta suunnasta {a} astetta")
        elif (a >= 158) and (a <= 202): # Etelä 158 - 202
            tuulisuunta_tulostus = (f"Etelätuulta suunnasta {a} astetta")
        elif (a >= 203) and (a <= 247): # Lounas 203 - 247
            tuulisuunta_tulostus = (f"Lounaistuulta suunnasta {a} astetta")
        elif (a >= 248) and (a <= 292): # Länsi 248 - 292
            tuulisuunta_tulostus = (f"Länsituulta suunnasta {a} astetta")
        elif (a >= 293) and (a <= 337): # Luode 293 - 337  
            tuulisuunta_tulostus = (f"Luoteistuulta suunnasta {a} astetta")
        else:
            tuulisuunta_tulostus = (f"Tuuli suunnasta {a} astetta")
       
        self.tuulisuunta_tulos = tuulisuunta_tulostus

    def tulosta_haku(self):
        return self.tuulisuunta_tulos

def main():
    haut = 1
    while True:
        def kokonaisluku():
            while True:
                try:
                    print("Sää tiedon tulokset joulukuu 2022 Oulunsalo")
                    syote = int(input("Anna haku numero:\n(1) Lämpötila\n(2) Sademäärä\n(3) Tuulen nopeus\n\
(4) Tuuli puuskassa\n(5) Tuulen suunta\n(0) Lopetus ja tulostus\n"))
                    return int(syote)
                except ValueError:
                    print()
                    print("Virheellinen syöte. Anna oikea haku numero kiitos.")
                    print()
        Hakutyyppi = kokonaisluku() 
        if Hakutyyppi == 1:
            haku = Lampotila(haut, 0 , "", "")
            Lampotila.ask_paiva(haku)
            Lampotila.ask_klo(haku)
            Lampotila.tee_haku(haku)
            HakuTulokset.append(haku)
            haut += 1
        elif Hakutyyppi == 2:
            haku = Sademaara(haut, 0 , "", "")
            Sademaara.ask_paiva(haku)
            Sademaara.ask_klo(haku)
            Sademaara.tee_haku(haku)
            HakuTulokset.append(haku)
            haut += 1
        elif Hakutyyppi == 3:
            haku = TuulenNopeus(haut, 0 , "", "")
            TuulenNopeus.ask_paiva(haku)
            TuulenNopeus.ask_klo(haku)
            TuulenNopeus.tee_haku(haku)
            HakuTulokset.append(haku)
            haut += 1
        elif Hakutyyppi == 4:
            haku = TuuliPuuskassa(haut, 0 , "", "")
            TuuliPuuskassa.ask_paiva(haku)
            TuuliPuuskassa.ask_klo(haku)
            TuuliPuuskassa.tee_haku(haku)
            HakuTulokset.append(haku)
            haut += 1
        elif Hakutyyppi == 5:
            haku = TuuliSuunta(haut, 0 , "", "")
            TuuliSuunta.ask_paiva(haku)
            TuuliSuunta.ask_klo(haku)
            TuuliSuunta.tee_haku(haku)
            HakuTulokset.append(haku)
            haut += 1
        elif Hakutyyppi == 0:
            break
        else:
            print()
            print("Virheellinen valinta. Anna oikea haku numero kiitos.")
            print()

    Tulostus = SaaTulostus()
    Tulostus.tulostus_haku(HakuTulokset)

#Lopuksi käynnistämme ohjelman pääfunktiosta
if __name__ == "__main__":
    main()