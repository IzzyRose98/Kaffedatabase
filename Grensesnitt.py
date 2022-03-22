
import sqlite3
import uuid
from datetime import date

con = sqlite3.connect("KaffeDatabase.db") 
cursor = con.cursor()


menu = input("Skriv inn 'a' for å avslutte, 's' for å legge inn smaksnotat eller 'h' for å hente informasjon.\n")


if (menu=="a"):
    print("Du valgte s, programmet avslutter nå.\n")
    exit()

elif (menu=="s"):
    print("Du valgte s for å legge til et smaksnotat.\n")  
    brenneri = input("Skriv inn hvilket brenneri kaffen kommer fra: \n")
    kaffe_navn = input("Skriv inn navnet på kaffen \n")
    poeng = input("Hvor mange poeng vil du gi kaffen? (1-10) \n")
    smaksnotat = input("Skriv inn smaksnotat her: \n")
    today = date.today()
    cursor.execute(f"INSERT INTO Kaffesmaking VALUES({smaksnotat}, {poeng}, {today}, {brenneri}, {kaffe_navn}, epost )")
 
elif (menu=="h"):
    print("Du valgte h for å hente ut informasjon. \n")
    print("Hvilken informasjon vil du hente ut? \n")
    info = input("Skriv 'l' for å få en liste over hvilke brukere som har smakt flest unike kaffer hittil i år. Skriv 'p' for å få en liste over kaffer som gir mest for pengene. Skriv 'f' for å få alle kaffer som er beskrevet med 'floral'. Skriv 'v' for å få kaffer fra Rwanda eller Colombia som ikke er vaskede. \n")
    
    if(info=="l"):
        print("Liste over hvilke brukere som har smakt flest unike kaffer\n")
        cursor.execute("SELECT Fullt navn, COUNT(FerdigbrentKaffeID) AS 'cnt' FROM Bruker JOIN Kaffesmaking ON Bruker.epost = Kaffesmaking.epost GROUP BY Bruker.epost HAVING (SELECT MAX(FerdigbrentKaffeID))")
        rows = cursor.fetchall()
        print(rows)


    elif(info=="p"):
        print("Liste over kaffer som gir mest for pengene \n")
        cursor.execute()
        rows = cursor.fetchall()
        print(rows)


    elif(info=="f"):
        print("Liste over alle kaffer som er beskrevet med 'floral' \n")
        cursor.execute("SELECT Navn FROM FerdigbrentKaffe WHERE (Beskrivelse = 'floral')")
        rows = cursor.fetchall()
        print(rows)

    elif(info=="v"):
        print("Liste over kaffer fra Rwanda eller Colombia som ikke er vaskede \n")

else:
    print("Ugyldig verdi. Prøv igjen: \n")


