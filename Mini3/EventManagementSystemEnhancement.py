print("Welcome to the seminar register")
guests=["Chris", "David", "Tia"]
others=[]
self_reg=1


class Event:
       def __init__(self, name, date,):
            self.name = name
            self.date = date
            
            
def name(self,name):
            self.name =name



while True:
  

  date=input("Enter the date of the event: ")
  name=input("Enter Your Name: ")
  add_participant=input("Enter the name of the additional participant you would like to add: ")
  check=input(" Would you like to add another new participant name? Type Yes or No: ")
  if check =="Yes":
        get_participant_count=others.count(others)
        add_participant=input("Enter the name of the participant: ")
        others.append(add_participant)
        check1=input(" Would you like to add another new participant name? Type Yes or No: ")
        new_add=1
        if check1=="Yes":
              add_participant=input("Enter the name of the participant: ")
              others.append(add_participant)
              new_add1=2
        check2=input(" Would you like to add another new participant name? Type Yes or No: ")
        if check2=="Yes":
            add_participant=input("Enter the name of the participant: ")
            others.append(add_participant)
            get_other=others.append(add_participant)
            new_add2=3
            print(f" Thanks so much {name}, for registering for participant registration. You registered {others}. The total amount of other participants you registered today is: {new_add2}")
  elif check=="No":
        print(f" The date of the event is {date}. Your name is {name}. You registered {others}. The total amount of other participants you registered today is: {new_add}") 
  elif check1=="No":
        print(f" The date of the event is {date}. Your name is {name}. You registered  {others}. The total amount of other participants you registered today is: {new_add} " ) 
  elif check2=="No":
        print(f" The date of the event is {date}. Your name is {name}. You registered  {others}. The total amount of other participants you registered today is: {new_add}" ) 
  
        