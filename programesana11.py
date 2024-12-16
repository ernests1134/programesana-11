#2uzdevums
n = int(input("ievadi skaitli:"))
summa= 0
for i in range (1,1+n):
    summa += i
    print("skaitļu suma no 1 līdz n ir", summa)
    #3uzdevums
    n = int(input("ievadi skaitli:"))
    faktorials = 1
    for i in range (1,1 +n):
        faktorials *= i
        print("skaitļu faktorials ir no 1 līdz n ir:", faktorials)
        
        #4uzdevums
        n = int(input("ievadi skaitli:"))
        for i in range(n, -1, -1):
            print(i)
            
            
        #5uzdevums
lenght = int(input("Lenght:"))
for i in range(lenght, 0, -1):
   print("*" * i)

#6uzdevums
import random
min_skaitlis = 0
max_skaitlis = 100
iedomata_skaitlis = random.randit(min_skaitlis, max_skaitlis)
print(f"Ludzu uzminet skaitli intervala no {min_skaitlis}")
minesanas_reizes = 0 
while True:
    lietotaja_ievade = int(input("ievadi savu minējumu:"))
    minesanas_reizes += 1 
    if lietotaja_ievade < iedomata_skaitlis:
        print("Lielaks!")
    elif lietotaja_ievade < iedomata_skaitlis:
        print("Mazāks!")
    else:
        print(f"Uzminets! Skaitlis ir {iedomata_skaitlis}.")
        break
    print(f"Skatijāt minesanu {minesanas_reizes} reizes.")
          
    