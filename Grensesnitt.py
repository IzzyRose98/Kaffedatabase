
import sqlite3
from datetime import date
from traceback import print_tb
con = sqlite3.connect("KaffeDatabase.db") 
cursor = con.cursor()


def registrer():

    cursor.execute("SELECT * FROM Bruker")
    info = cursor.fetchall()
   
    epost = input("Skriv inn eposten din: ")
    listOfEmails = []

    for y in info:
        listOfEmails.append(y[0])
        
    if (epost in listOfEmails):
        passord = input("Bruker er allerede registrert. Skriv inn ditt passord: ")
        cursor.execute("SELECT passord FROM Bruker WHERE epost = ? AND passord = ?", (epost, passord,))
        riktigPassord = cursor.fetchall()

        while(len(riktigPassord)==0):
            passord = input("Passordet er feil. Prøv igjen. ")
            cursor.execute("SELECT passord FROM Bruker WHERE epost = ? AND passord = ?", (epost, passord,))
            riktigPassord = cursor.fetchall()
 
        print("Du er nå logget inn! ")
        return(epost)

    else:
        passord = input("Skriv inn passord: ")
        navn = input("Skriv inn fullt navn: ")
        cursor.execute("INSERT INTO Bruker VALUES(?, ?, ?)", (epost, passord, navn,))
        con.commit()

        print("Du er nå logget inn!")
        return(epost)

    
        
def run(epost):
    
    menu = "b"

    while(menu != 'a'):

        menu = input("Skriv inn 'a' for å avslutte,'s' for å legge inn smaksnotat eller 'h' for å hente informasjon.")

        if (menu=="a"):
            print("Du valgte a, programmet avslutter nå.\n")
            exit()

        elif (menu=="s"):
            print("Du valgte s for å legge til et smaksnotat.\n")  
            brenneri = input("Skriv inn hvilket brenneri kaffen kommer fra: \n")
            id_brenneri = None
            cursor.execute("SELECT * FROM Brenneri WHERE navn = ?", (brenneri,))
            data = cursor.fetchall()
            if (len(data) == 0):
                cursor.execute(f"INSERT INTO Brenneri VALUES(?, ?)",(None, brenneri) )
                con.commit()
                cursor.execute("SELECT * FROM Brenneri WHERE navn = ?", (brenneri,))
                data = cursor.fetchall()
                for row in data:
                    id_brenneri = row[0]

            else:
                cursor.execute("SELECT * FROM Brenneri WHERE navn = ?", (brenneri,))
                data = cursor.fetchall()
                for row in data:
                    id_brenneri = row[0]

                
            kaffe_navn = input("Skriv inn navnet på kaffen \n")
            id_ferdigbrentkaffe = None
            cursor.execute("SELECT * FROM FerdigbrentKaffe WHERE navn = ?", (kaffe_navn,))
            data = cursor.fetchall()
            if (len(data) == 0):
                cursor.execute(f"INSERT INTO FerdigbrentKaffe VALUES(?, ?, ?, ?, ?, ?, ? )",(None, None, kaffe_navn, None, None, None, 1, ) )
                con.commit()
                cursor.execute("SELECT * FROM FerdigbrentKaffe WHERE navn = ?", (kaffe_navn,))
                data = cursor.fetchall()
                for row in data:
                    id_ferdigbrentkaffe = row[0]
            else:
                cursor.execute("SELECT * FROM FerdigbrentKaffe WHERE navn = ?", (kaffe_navn,))
                data = cursor.fetchall()
                for row in data:
                    id_ferdigbrentkaffe = row[0]


            poeng = input("Hvor mange poeng vil du gi kaffen? (1-10) \n")
            smaksnotat = input("Skriv inn smaksnotat her: \n")
            print(epost[0])
            today = date.today()
            cursor.execute(f"INSERT INTO Kaffesmaking VALUES(?,?,?,?,?,?,?)",(None, smaksnotat, poeng, today, id_ferdigbrentkaffe, epost, id_brenneri,) )
            con.commit()


        elif (menu=="h"):

            print("Du valgte h for å hente ut informasjon. \n")
            print("Hvilken informasjon vil du hente ut? \n")
            info = input("Skriv 'l' for å få en liste over hvilke brukere som har smakt flest unike kaffer (sortert synkende).\nSkriv 'p' for å få en liste over kaffer som gir mest for pengene. \nSkriv 'f' for å få alle kaffer som er beskrevet med 'floral'. \nSkriv 'v' for å få kaffer fra Rwanda eller Colombia som ikke er vaskede. \n")

            if(info=="l"):
                print("Liste over hvilke brukere som har smakt flest unike kaffer\n")
                cursor.execute("SELECT navn FROM (SELECT Fullt navn, COUNT(FerdigbrentKaffeID) AS 'cnt' FROM Bruker JOIN Kaffesmaking ON Bruker.epost = Kaffesmaking.epost GROUP BY Bruker.epost HAVING (SELECT MAX(FerdigbrentKaffeID)))")
                rows = cursor.fetchall()
                print(rows)

            elif(info=="p"):
                print("Liste over kaffer som gir mest for pengene \n")
                cursor.execute("SELECT navn FROM (SELECT SUM(Poeng) AS 'poeng', COUNT(FerdigbrentKaffe.FerdigbrentKaffeID) AS 'ids', FerdigbrentKaffe.Navn AS 'navn', FerdigbrentKaffe.Kilopris AS 'pris', FerdigbrentKaffe.FerdigbrentKaffeID AS 'id' FROM (FerdigbrentKaffe JOIN Kaffesmaking ON FerdigbrentKaffe.FerdigbrentKaffeID = Kaffesmaking.FerdigbrentKaffeID) GROUP BY FerdigbrentKaffe.FerdigbrentKaffeID) ORDER BY (pris/(poeng/ids)) ASC")
                rows = cursor.fetchall()
                print(rows)

            elif(info=="f"):
                print("Liste over alle kaffer som er beskrevet med 'floral' \n")
                cursor.execute("SELECT Navn FROM FerdigbrentKaffe WHERE (Beskrivelse = 'floral')")
                rows = cursor.fetchall()
                print(rows)

            elif(info=="v"):
                print("Liste over kaffer fra Rwanda eller Colombia som ikke er vaskede \n")
                cursor.execute("SELECT FerdigbrentKaffe.Navn FROM (((FerdigbrentKaffe JOIN Kaffeparti ON FerdigbrentKaffe.KaffepartiID = Kaffeparti.KaffepartiID) JOIN Gård ON Kaffeparti.GårdsID = Gård.GårdsID) JOIN Lokasjon ON Gård.LokasjonsID = Lokasjon.LokasjonsID) JOIN Foredlingsmetode ON Kaffeparti.ForedlingsmetodeID = Foredlingsmetode.ForedlingsmetodeID WHERE (Lokasjon.Land = 'Rwanda' OR Lokasjon.Land = 'Colombia') AND (Foredlingsmetode.Beskrivelse != 'Vasket')")
                rows = cursor.fetchall()
                print(rows)

        else:
            print("Ugyldig verdi. Prøv igjen: \n")


def main():
    epost = registrer()
    run(epost)
    print("Programmet er avsluttet \n")
main() 