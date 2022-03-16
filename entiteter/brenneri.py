class Brenneri:
    
    def __init__(self, navn, ID):
      self.navn = navn
      self.ID = ID
      
    @property
    def navn(self):
        return self.navn
    
    @property
    def ID(self):
        return self.ID