
class Vehicle:
    def __init__(self, reg_num, type, owner,update_owner, new_owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
            self.update_owner=update_owner
            self.new_owner=new_owner
    print( """
Make YOUR Selection!
      1. Register Vehicle
      2. Update Owner
      3. EXIT THIS SYSTEM
"""
    )
    
reg_num=input( " Enter Registration number: ")
Owner=  input("Enter current owner's name: ")
print(f"\nThe owner is {Owner}, for car registration title {reg_num}.")

def update_owner(owners):
        if not owners in update_owner:
             print(" No owner found....")
             print(" Please enter updated name")     
update_owner1=input(" Would you like to update the owner for this vehicle? Enter a new owners NAME or type No to Exit this system! ")  
new_reg=update_owner1

if update_owner1=="No":
      print(" Exit the system!!!")
elif update_owner1=="Yes":
      update_owner
else:
      print(f"{new_reg} is the updated owner for vehicle {reg_num}.")

    
    
    


                    