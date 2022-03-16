class FerdigbrentKaffe:
    
    def __init__(self, dato, kaffenavn, beskrivelse, kilopris, brenningsgrad, ID):
        self.dato = dato
        self.kaffenavn = kaffenavn
        self.beskrivelse = beskrivelse
        self.kilopris = kilopris
        self.brenningsgrad = brenningsgrad
        self.ID = ID
      
    @property
    def kaffenavn(self):
        return self.kaffenavn
    
    @property
    def beskrivelse(self):
        return self.beskrivelse

    @property
    def kilopris(self):
        return self.kilopris

    @property
    def brenningsgrad(self):
        return self.brenningsgrad
    
    @property
    def ID(self):
        return self.ID
