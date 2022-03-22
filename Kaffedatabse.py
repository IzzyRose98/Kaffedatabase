import sqlite3

con = sqlite3.connect("KaffeDatabase.db")
cursor = con.cursor()
cursor.execute('CREATE TABLE Bruker (Epost TEXT PRIMARY KEY NOT NULL UNIQUE, Passord TEXT NOT NULL, Fullt navn TEXT NOT NULL)')
cursor.execute('CREATE TABLE Lokasjon (LokasjonsID INTEGER PRIMARY KEY NOT NULL UNIQUE, Land TEXT NOT NULL, Region TEXT NOT NULL)')
cursor.execute('CREATE TABLE Gård (GårdsID INTEGER PRIMARY KEY NOT NULL UNIQUE, Moh INTEGER)')
cursor.execute('CREATE TABLE Foredlingsmetode (ForedlingsmetodeID INTEGER PRIMARY KEY NOT NULL UNIQUE, Navn TEXT, Beskrivelse TEXT)')
cursor.execute('CREATE TABLE Kaffeparti (KaffepartiID INTEGER PRIMARY KEY NOT NULL UNIQUE, Innhøstingsår INTEGER, Betalt INTEGER, GårdsID INTEGER NOT NULL, ForedlingsmetodeID INTEGER NOT NULL, FOREIGN KEY(GårdsID) REFERENCES Gård(GårdsID), FOREIGN KEY (ForedlingsmetodeID) REFERENCES Foredlingsmetode(ForedlingsmetodeID))')
cursor.execute('CREATE TABLE FerdigbrentKaffe (FerdigbrentkaffeID INTEGER PRIMARY KEY NOT NULL UNIQUE, Dato INTEGER, Navn TEXT, Beskrivelse TEXT, Kilopris INTEGER, Brenningsgrad TEXT, KaffepartiID INTEGER NOT NULL, FOREIGN KEY(KaffepartiID) REFERENCES Kaffeparti(KaffepartiID))')
cursor.execute('CREATE TABLE Kaffesmaking (KaffesmakingID INTEGER PRIMARY KEY NOT NULL UNIQUE, Notat TEXT, Poeng INTEGER, Smaksdato INTEGER, FerdigbrentKaffeID INTEGER NOT NULL, Epost TEXT, FOREIGN KEY(FerdigbrentKaffeID) REFERENCES FerdigbrentKaffe(FerdigbrentKaffeID), FOREIGN KEY(Epost) REFERENCES Bruker(Epost))')
cursor.execute('CREATE TABLE Brenneri (BrenneriID INTEGER PRIMARY KEY, Navn TEXT )')
cursor.execute('CREATE TABLE Kaffebønner (Art TEXT PRIMARY KEY NOT NULL UNIQUE)')
cursor.execute('CREATE TABLE Dyrking (id INTEGER PRIMARY KEY NOT NULL UNIQUE, Art TEXT NOT NULL, GårdsID INTEGER NOT NULL)')
cursor.execute('CREATE TABLE InnholdKaffeParti (id INTEGER PRIMARY KEY NOT NULL UNIQUE, Art TEXT NOT NULL, KaffepartiID INTEGER NOT NULL)')
con.commit()
con.close()

