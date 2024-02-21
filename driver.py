class Driver:
    def __init__(self,name="Kathryn",dl_class="MC"):
        self.name = name
        self.dl_class = dl_class
        self.miles = 0
        
    def description(self):
        print(f""" 
        Name: {self.name}
        License Class: {self.dl_class}
        Miles Driven: {self.miles}
        """)
        
    @staticmethod
    def are_cool():
        print("meh")
        
    def log_miles(self,miles):
        self.miles=self.miles+miles