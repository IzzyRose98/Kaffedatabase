class Gard:
    
    def __init__(self, navn, moh, ID):
      self.navn = navn
      self.moh = moh
      self.ID = ID
    
    @property
    def navn(self):
        return self.navn
    
    @property
    def moh(self):
        return self.moh
    
    def __str__(self) -> str:
        return 'Gårdsnavn: '+ self.navn + 'Høyde over havet' + self.moh