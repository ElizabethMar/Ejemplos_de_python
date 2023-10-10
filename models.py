class User:    
    name = None     
    email=None    
    def __init__(self,name,email):    
         self.name=name    

         self.email=email    
    def send_email  (self):     
        if self.email is not None:     
            print("sending email:" + self.email)     
        else:     
            print ("error")    
    def __str__(self):   
        return "user:" + self.email    

class Student(User):   
    def is_approved (self): 
        return self.score>=8 
    def __repr__(self): 
        return f"Student(name='{self.name}',email='{self.email}',id='{self.id}',score='{self.score}')" 
    id=None   
    def __init__(self,   
       name=None,   
       email=None ,   
       id= None,  
       score=None        
    ):   
     self.id=id  
     self.score=score  
    def __str__(self):   
        return "Student:" + str (self.id)+"," +self.email   
        super (). __init__(name,email)   
        self.id=uuid. uuid4()   
