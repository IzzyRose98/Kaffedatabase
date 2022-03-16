class kaffesmaking:
    
    def __init__(self, notat, poeng, smaksdato, ID):
      self.notat = notat
      self.poeng = poeng
      self.smaksdato = smaksdato
      self.ID = ID
      
    @property
    def notat(self):
        return self.notat
    
    @property
    def poeng(self):
        return self.poeng
    
    @property
    def smaksdato(self):
        return self.smaksdato()
    
    @property
    def ID(self):
        return self.ID