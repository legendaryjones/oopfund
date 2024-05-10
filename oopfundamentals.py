class Vehicle():
        def __init__(self, reg_num, vehicle_type, owner):
            self.registration_number = reg_num
            self.type = vehicle_type
            self.owner = owner
            # self.update_owner = []

# def update_owner(self):
     
#      print(f'Hello Im the new {self.owner} of {self.type} and my regisration number is {self.registration_number}')
#      self.owner.append(update_owner)

# car= Vehicle(reg_num= '12345', owner= 'mike')
# suv= Vehicle(reg_num= '6789', owner= 'josh' )
# motorcycle= Vehicle (reg_num='0123', owner='anthony')

# def update_owner():
#       print(f' changing the owner of )
     
        def update_owner(self, new_owner):
             self.owner= new_owner
             print (f'The Vehicle {self.type} registration is {self.registration_number} and the owner has been updated to {self.owner}') 

car= Vehicle(reg_num='12345',vehicle_type="car",owner='mike')
suv= Vehicle(reg_num=6789,vehicle_type="truck",owner='josh' )
motorcycle= Vehicle(reg_num=2222,vehicle_type='motorcycle',owner='anthony')
van= Vehicle(reg_num=3333, vehicle_type='van', owner='katrina')

car.update_owner('goku')
print(car.owner)

suv.update_owner('bruce')
print (suv.owner)

motorcycle.update_owner('dave')
print (suv.owner)

van.update_owner('sarah')
print (van.owner)



    
     

      

      
