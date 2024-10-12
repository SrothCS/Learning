print("Welcome to Sroth  pizza calculator!")
category=input(f"What flavor would you like? Cheese or Peporni. Type C or P ")
size=input(f"what size would you like , Type S, M or L ")
extratopping=input(f"C for Cappicum, P for pinneple ")
total_cost=0
if category=='C':
    total_cost+=15
else:
    total_cost+=18
if size=='S':
    total_cost+=0
elif size=='M':
     total_cost+=2
else: 
    total_cost+=3
print(total_cost)
