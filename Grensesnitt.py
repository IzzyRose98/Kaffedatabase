
from genericpath import exists
import sqlite3
from datetime import date


con = sqlite3.connect("Kaffe.db") 
cursor = con.cursor()

def registrer():
    epost = input("Skriv inn eposten din")
    cursor.execute("SELECT epost FROM Bruker WHERE epost = ?", (epost))
    data = cursor.fetchall()
    if (len(data) == 0):
        passord = input("Skriv inn passord")
        navn = input("Skriv inn fullt navn")
        cursor.execute("INSERT INTO Bruker VALUES({epost}, {passord}, {navn})")

    else:
        passord = input("Bruker er allerede registrert. Skriv inn ditt passord.")
        riktigPassord = cursor.execute("SELECT passord FROM Bruker WHERE epost = ?", (epost))
        while (passord != riktigPassord):
            passord = input("Passordet er feil. Prøv igjen. ")

        print("Du er nå logget inn!")
        


    return epost

        
def run(brukerPK):        
    
    menu = input("Skriv inn 'a' for å avslutte, 's' for å legge inn smaksnotat eller 'h' for å hente informasjon.\n")
    
    while(menu != 'a'):
    
        menu = input("Skriv inn 'a' for å avslutte,\n's' for å legge inn smaksnotat eller \n'h' for å hente informasjon.\n")
    
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
            cursor.execute(f"INSERT INTO Kaffesmaking VALUES({smaksnotat}, {poeng}, {today}, {brenneri}, {kaffe_navn}, {brukerPK} )")

        
        elif (menu=="h"):
            print("Du valgte h for å hente ut informasjon. \n")
            print("Hvilken informasjon vil du hente ut? \n")
            info = input("Skriv 'l' for å få en liste over hvilke brukere som har smakt flest unike kaffer hittil i år. Skriv 'p' for å få en liste over kaffer som gir mest for pengene. Skriv 'f' for å få alle kaffer som er beskrevet med 'floral'. Skriv 'v' for å få kaffer fra Rwanda eller Colombia som ikke er vaskede. \n")
            
            if(info=="l"):
                print("Liste over hvilke brukere som har smakt flest unike kaffer\n")
                cursor.execute("SELECT * FROM Bruker")
                rows = cursor.fetchall()
                print("All rows in the table person:")
                print(rows)

            elif(info=="p"):
                print("Liste over kaffer som gir mest for pengene \n")

            elif(info=="f"):
                print("Liste over alle kaffer som er beskrevet med 'floral' \n")

            elif(info=="v"):
                print("Liste over kaffer fra Rwanda eller Colombia som ikke er vaskede \n")

        else:
            print("Ugyldig verdi. Prøv igjen: \n")


def main():
    epost = registrer()
    run(epost)
    print("Programmet er avsluttet \n")
main()