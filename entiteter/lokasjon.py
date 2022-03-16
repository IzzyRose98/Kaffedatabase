class Lokasjon:
    
    def __init__(self, ID, region, land):
        self.ID = ID
        self.region = region
        self.land = land
      
    @property
    def region(self):
        return self.region
    
    @property
    def land(self):
        return self.land
    
    def __str__(self) -> str:
        return 'Land: ' + self.land + 'Region: ' + self.region