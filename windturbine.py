class OffshoreWindTurbine: 
    def __init__(self, company, model, foundation, capacity): 
        self.company = company 
        self.model = model 
        self.foundation = foundation 
        self.capacity = capacity 

        self.water_depth = None 

    def __str__(self): 
        return f"Model {self.model} by {self.company} with {self.foundation} foundation and {self.capacity} MW capacity" 
    
    def is_suitable_for_depth(self, depth): 
        if self.foundation == "monopile" and depth <= 30: 
            return True 
        elif self.foundation == "jacket" and depth <= 50: 
            return True 
        elif self.foundation == "floating" and depth > 50: 
            return True 
        else: 
            return False    