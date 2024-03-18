jezyki = ["C++", "Python", "Java", "Lisp"]
cyfry = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# for x in range(len(jezyki)):
#     print(jezyki[x], end=" ")

print()
for x in range(len(cyfry)):
    print(f"{cyfry[x]}", end=" ")

print()

print(*cyfry)
print()
print(cyfry)
print()
print(*cyfry, sep="-")
print()
for n in range(3, 5):
    print(n, end=" ")
print()
for n in range(5):
    print(n, end="")
print()

# pętla zagnieżdżona
for p in range(3):
    for q in range(4):
        if q == 2:
            print(f"wykryto q ={q}")
            break
        print(f"(p={p} q={q})", end=" ")
        
print()
        
for b in range(3):
    for c in range(3):
        
     print(b, c)
     
print()
     
     
for i in range(0,100,10):
   print(i, end=' ')
   
print('\n')
for i in range(100,80,-10):
    print(i, end=' ')
print('\n')

for c in "Figo":
    print(c, end='...')
    
print('\n')
#pętle while

i =1
tmp=0
while i<=100:
    tmp=tmp+i
    i+=1
print(f"Suma liczb od 1 do 99: {tmp}\n")

#symulacja pętli do...while

while True:
   print("Symulacja pętli do...while\n")
   warunek = input("Czy kontynuować? tak/nie\n")
   if warunek.lower() != 'tak':
       break


    