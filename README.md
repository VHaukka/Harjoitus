# Kurssin Harjoitus

Tehtävän alustava kuvaus. Sää tietojen haku www sivuilta. Talletus ja näyttäminen käyttöliitymällä.

# Python haku ohjelma tammikuun 2023 säätiedoista

Tehtävänä on harjoitus projekti Codenowpython ja AI kurssin lopuksi. Tässä readme filessä on kerrottu lyhyesti 
tekemäni ohjelman toiminta ja rakenne. 
Aihe projekti työ tekemiseen oli vaapaa. Valitsin sää tietojen hakemiseen ja tulostamiseen soveltuvan 
pienene python ohjelman. Lähtökohtana pidin tekemisessä yksinkertaista ohjelmaa. Ei mitään liian laajaa 
vaikeasti toteutettavaa. Tässä onnistuin omasta mielestä, mutta tuli kyllä mietittyä että oliko sittenkin 
liian suppea sovellus. Mutta näillä mentiin maaliin. Tekeminen lähti UML mallin rakentamisesta ja suunnitelman 
selvittämisestä erisellä projektityön esittely tunnilla. Esitelmää varten tein muutaman sivun Powerpoint 
esityksen. Tämä esittely tuli tarpeeseen. Oli hyvä että alustus tehtiin rauhassa ennen kuin riennettiin ohjelma 
koodin kirjoittamiseen.

# Ohjelman toiminta

Toiminta on yksinkertainen. Ohjelma käynnistetään Visual Studio Code ympäristössä Crtl + F5 tai VSCode terminaalista 
komenolla python weatherSearch.py. Ohjelmaa käytetään terminaalissa näkyvän käyttöliittymä kautta. Käyttäjä voi hakea
valinalla 1-5 koneelta olevalta csv tiedostolta kuukauden säätietojen arvoja. Näissä valinoissa käyttäjältä kysytään
päivän ja kello aika. 6 valinalla tulostetaan diagrammi koko kuukauden päivälämpötiloista tiedot haetaan samasta
csv tiedostosta. 
7 valita tulostaa parin tunnin takaisen lämpötilan ja sademäärän Oulun lentoaseman mittauspisteeltä. Tässä toiminassa 
tehdään automaattihaku ilmaiteteenlaitoksen koneluettevaan palveluun. Ohjelma lopetaan ja tulostetaan tehdyt haut 
valinalla 0. Tulostus juoksevalla numeroinilla, tehtyjen hakuja mukaan alla esimerkki tulosteesta. 

Sään haku tulokset:
Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema
***************************************************************
1. Haku 5.1 2023 kello 06:00
Lämpötila -7.3 astetta


*****************************
Sään haku tulokset:
Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema
***************************************************************
2. Haku 1.1 2023 kello 23:00
Luoteistuulta suunnasta 302 astetta

# Ohjelman rakenne

Ohjelmassa on seitsemän luokkaa, kolme funktioa ja main funkio. Alustus tiedoissa import tarvittavat modullit joita tässä 
on kuusi kappaletta. Alussa kerrotaan kommentissa csv tiedoston haku ja ohjelman rajoiteet. Avataan tiedosto 
pandas taulukkoon myöhempää käyttöä varten. Luodaan tyhjä seekresults lista hakutietojen talletusta varten. 
Ohjelma käynnistyy main funktiosta. Alussa kutsutaan checkyear_month() funktiosta kuukausi ja vuosi tiedot tulostus
parametrejä varten. Luodaan haku laskuri seekid. While true silmukassa pyörii käyttöliittymä , josta tehdään käyttäjän 
valinnat. Silmukassa try except virheen korjaus jos valinassa annetaan jotain muuta kuin numero arvo. Valinta numero 
palautetaan intcount funktion arvoksi. Tästä tulee searchtype arvo jolla tehdään if else haaran valinta. 
 






