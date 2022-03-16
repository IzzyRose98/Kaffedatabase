class Foredlingsmetode:
    
    def __init__(self, name, beskrivelse, ID):
      self.name = name
      self.beskrivelse = beskrivelse
      self.ID = ID
      
    @property
    def name(self):
        return self.name
    
    @property
    def beskrivelse(self):
        return self.beskrivelse
    
    @property
    def ID(self):
        return self.ID