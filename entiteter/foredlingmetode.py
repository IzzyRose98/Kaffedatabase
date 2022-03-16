class Foredlingsmetode:
    
    def __init__(self, navn, beskrivelse, ID):
      self.navn = navn
      self.beskrivelse = beskrivelse
      self.ID = ID
      
    @property
    def navn(self):
        return self.navn
    
    @property
    def beskrivelse(self):
        return self.beskrivelse
    
    @property
    def ID(self):
        return self.ID
