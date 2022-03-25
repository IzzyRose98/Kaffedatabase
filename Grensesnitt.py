
import sqlite3
from datetime import date

con = sqlite3.connect("KaffeDatabase.db") 
cursor = con.cursor()


def registrer():
    epost = input("Skriv inn eposten din: ")
    cursor.execute("SELECT * FROM Bruker WHERE epost = ?", (epost,))
    data = cursor.fetchall()
    if (len(data) == 0):
        passord = input("Skriv inn passord: ")
        navn = input("Skriv inn fullt navn: ")
        cursor.execute("INSERT INTO Bruker VALUES(?, ?, ?)", (epost, passord, navn,))
        con.commit()

    else:
        passord = input("Bruker er allerede registrert. Skriv inn ditt passord: ")
        cursor.execute("SELECT passord FROM Bruker WHERE epost = ? AND passord = ?", (epost, passord,))
        riktigPassord = cursor.fetchall()

        while(len(riktigPassord)==0):
            passord = input("Passordet er feil. Prøv igjen. ")
            cursor.execute("SELECT passord FROM Bruker WHERE epost = ? AND passord = ?", (epost, passord,))
            riktigPassord = cursor.fetchall()
 
        print("Du er nå logget inn! ")
            
    return epost

        
def run(brukerPK):
    menu = input("Skriv inn 'a' for å avslutte, 's' for å legge inn smaksnotat eller 'h' for å hente informasjon.\n")

    while(menu != 'a'):

        menu = input("Skriv inn 'a' for å avslutte,\n's' for å legge inn smaksnotat eller \n'h' for å hente informasjon.\n")

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
            today = date.today()
            
            
            #rows = cursor.fetchall()
            #print(rows)
            cursor.execute(f"INSERT INTO Kaffesmaking VALUES(?,?,?,?,?,?,?)",(None, smaksnotat, poeng, today, id_ferdigbrentkaffe, brukerPK, id_brenneri,) )
            con.commit()


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
                cursor.execute("SELECT Navn FROM FerdigbrentKaffe WHERE Beskrivelse LIKE '%floral%'")
                rows = cursor.fetchall()
                print(rows)
                cursor.execute("SELECT FerdigbrentKaffeID FROM Kaffesmaking WHERE Notat LIKE '%floral%'")
                data = cursor.fetchall()
                for rows in data:
                    id_kaffe = rows[0]
                    cursor.execute("SELECT Navn FROM FerdigbrentKaffe WHERE FerdigbrentKaffeID = ?", (id_kaffe,))
                    data = cursor.fetchall()
                    print(data)
                    


            elif(info=="v"):
                print("Liste over kaffer fra Rwanda eller Colombia som ikke er vaskede \n")

        else:
            print("Ugyldig verdi. Prøv igjen: \n")


def main():
    epost = registrer()
    run(epost)
    print("Programmet er avsluttet \n")
main() 