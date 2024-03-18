#szukanie elementu x

tab = [1, 2, 3, 2, -7, 44, 5, 1, 0, -3]
def szukaj(tabl, left, right, x):
    if left>right:
        print(f"Element {x} nie został odnaleziony")
    else:
        if(tab[left]==x):
            print("Znaleziono poszukiwany element")
        else:
            szukaj(tab, left+1,right,x)
            
            
print("Tablica: ", tab)
szukaj(tab, 0, len(tab)-1, 7)
print("\n")
szukaj(tab, 0, len(tab)-1, 5)



#silnia
def silnia(x):
    if(x==0):
        return 1
    else:
        return x*silnia(x-1)
    
for i in range(5, 11):
    print(f"silnia({i})={silnia(i)}")
    
    
print()

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 8, 1):
    print(fib(i))
