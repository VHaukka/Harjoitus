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

Toiminta on yksinkertainen. Ohjelma käynnistetään Visual Studio Code ympäristössä Crtl + F5 tai terminaalista 
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
parametrejä varten. Luodaan haku laskuri seekid. While true silmukassa pyörii käyttöliittymä, josta tehdään käyttäjän 
valinnat. Alla kuva käyttöliittymän silmukasta. 

Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema
Tilasto kuukausi 1 vuosi 2023 
Anna halutun mittaustuloksen numero:
(1) Lämpötila
(2) Sademäärä
(3) Tuulen nopeus
(4) Tuuli puuskassa
(5) Tuulen suunta
(6) Diagrammi tilasto kuukauden päivä lämpötiloista (kello 12:00)
(7) Lämpötila ja tuulen nopeus Oulun Lentoasema(machine search)
(0) Lopetus ja tulostus

Silmukassa try except virheen korjaus jos valinassa annetaan jotain muuta kuin numero arvo. Valinta numero 
palautetaan intcount funktion arvoksi. Tästä saadaan searchtypelle arvo jolla tehdään if else haaran valinta.
Haaran valinnat 1-5 ovat samakaltaiset, käyn läpi 1 valinnan.

Valmistetaan weather luokka olio johon saadaan temperature luokkaa kutsuttaessa muuttujat seekid, day, time, ja 
temperature_result. Haetaan näille arvot seekid on 1 ensimäisessä haussa. WeatherSeek luokassa metodit ask_day 
ja ask_time. Nämä on perittynä temperature luokassa. Näissä annetaan käyttäjän valinta halutulle päivälle ja 
kellon ajalle. Virheen korjaukset on huomioitu noissa, siltä varalta että käyttäjä syöttää väärän arvon. 
Viimeinen temperature weather haku on make_seek metodi jossa parsitaan csv tiedostosta oikea lämpötila arvo haetulla
päivän ja kellon ajan arvolla. Saatu arvo löytyy temperature_result muuttujasta. Print_seek metodi palauttaa
temperature_result arvon myöhempää käyttöä varten. Nämä saadut temperature luokan arvot lisätään append komenolla 
tyhjään seekresults listaan. Yksi haku kierros on nyt mennyt kun vielä muistetaan lisätä seekid laskuriin + 1. 
Uusi valinta edessä voidaan jatkaa hakuja tai lopettaa ohjelma ja tulostaa. 
Valitaan 0 ohjelma loppuu elif haarassa on break komento. Main haarassa jatketaan tulostukseen. Kutsutaan WeatherResult 
luokkaa täällä on metodi results_seek jossa parametrinä seekresults list. Checkyear_month() funktiosta saadaan 
kuukausi ja vuosi arvo tulostukseen. For lauseella tehdään silmukka jolla saadaa tulostettua seekresults listasta kaikki
arvot ja print_seek metodi hakee temperature_result arvon. Main haarassa WeatherResult antaa tulostus arvot Printout 
muuttujaan ja tästä saadaa tulostus printattua terminaaliin. Tulosteeesta on kuva ohjelman toiminta osiossa. 

Käyttöliittymän valinta 6 kutsuu temperature_statistic funktiota, jossa on toimintana kuukauden päivälämpötilojen 
tulostaminen viivadiagrammi esityksenä. Haetaan csv tiedostosta kaikki kuukauden lämpötilat aikaleimalla 12:00. 
Saadut muuttuja arvot viedään nympy taulukkoon. Tästä taulukosta saadaan käsiteltyä matplotlib.pyplot modullin avulla
graaffinen viivadiagrammi esitys. Lämpöaste, päivämäärä ja näihin arvoihin piirettynä viiva esitys lämpötiloista.
Valinta 7 tulostaa parin tunnin takaisen lämpötilan ja tuulen nopeuden arvon Oulun lentoasemalta. Arvot haetaan kellon 
ajan avulla ilmatieteenlaitoksen konehakupalvelusta. Tässä tarvitaan apuna modullit datetime ja fmiopendata.wfs. 
Hakupolkuun tarvitaan aloitus ja lopetus aika muodossa 2023-02-02T07:02:16Z. Otin aloitus ja lopetus ajan väliksi 
minuutin että datapaketti ei paisunut liian isoksi. Lisäksi vaaditaan paikkatieto. Tässä käytin fmisid numeroa 
ilmateiteenlaitoksen verkkosivuilla on listattuna kaikille havaintoasemille oma id tunnus numero. Hakupolun alku määrittää 
mitä tietoa haetaan onko sää tutka vai merihavaintoja. Merkeillä :: ja & eritellään hakuparametrit. Tuossa alla on 
tämän tehtävän automaattihakupolku. 

download_stored_query(f"fmi::observations::weather::multipointcoverage&fmisid=101786&starttime={start_datetime}&endtime={end_datetime}&")

Palvelu on WFS palvelu joka tarkoittaa, että kyselyt tulee tehdä tallennettujen kyselyiden avulla. Latauksessa käytetään 
StoredQueries kyselyjä. Tämän ohjelman data määrä on pieni joten lopullisen arvoin sain parsittua melko helposti. Nämä kaksi 
arvoa näytetään tkinter modullin avulla omalle pienelle ikkunalle. 

# Lopuksi 

Tässä oli kerrottu pienen python ohjelman rakenne. Aika selvä kun ei ole laajasta ohjelmasta kyse. Käyttöliittymä pyörii 
while true silmukassa jossa kuljetaan valittuun if else haaran toimintaan. Else haara ilmoittaa väärästä numero valinnasta
ja 0 valinta lopetti ohjelman ja tulosti kaikki tehdyt haut. Yksi automaattihaku muissa käytetään koneelle valmiiksi ladattua 
csv tiedostoa.   

# Huomioitavaa

Palvelussa käytössä UTC-aika huomioitava automaattihaun aikaleimassa. Csv tiedosto voi palauttaa NaN tuloksen, 
joka tarkoittaa että havaintotieto puuttuu kokonaan. Lukema -1 sademäärässä ei ole virhe vaan tarkoittaa ettei 
ole satanut lainkaan. Lukema 0 tarkoittaa että on satanut, mutta sadetta ei ole kertynyt edes 0,1 mm.









