class kaffeparti:
    
    def __init__(self, innhostningsar, betalt, ID):
      self.name = innhostningsar
      self.beskrivelse = betalt
      self.ID = ID
      
    @property
    def innhostningsar(self):
        return self.innhostningsar
    
    @property
    def betalt(self):
        return self.betalt + self
    
    @property
    def ID(self):
        return self.ID