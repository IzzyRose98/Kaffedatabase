from copyreg import constructor
from webbrowser import get


class Bruker:
        
    def __init__(self, navn, passord, epost):
      self.navn = navn
      self.passord = passord
      self.epost = epost
        
    @property
    def navn(self):
        return self.navn
    
    @property
    def epost(self):
        return self.epost
    
    @property
    def passord(self):
        return self.passord
    
    def __str__(self) -> str:
        return 'Bruker: ' + self.navn + 'epost: ' + self.epost + 'passord: ***'
    