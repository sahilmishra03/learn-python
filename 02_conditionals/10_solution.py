# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
petType = "Cat"
petAge = 13
if(petType=="Dog"and petAge<2):
    print("Puppy food")
elif(petType=="Cat"and petAge>5):
    print("Senior Cat food")