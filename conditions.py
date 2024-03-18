# x = "hejka"
# tab = [1, 2, "Hejka"]
# if x.title() in tab:
#     print("jest")
# else:
#     print("nie ma")

# A = 20
# B = 20
# if A > B:
#     print("A jest większe od B")
# elif A == B:
#     print("A jest równe B")
# else:
#     print("Skończyły mi się pomysły")

# jezyki = ["C++", "Python", "Java"]
# for x in jezyki:
#     if x == "Python":
#         print("Znalazłem Pythona!")
#     else:
#         print(f"Znalazłem język {x}!")


# zadania

# zadanie 3/49


def euklides1():
    start = input("Podaj liczbę\n")
    n = int(start)
    flag = 0
    if n < 2:
        return False

    for o in range(2, n):
        if n % o != 0:
            flag = flag + 1
    if flag == n - 2:
        print("Liczba pierwsza")
    else:
        print("Liczba nie jest pierwsza")


# euklides1()


def euklides2(n):
    if n < 2:
        print("Liczba musi być większa od 1!")
        return False

    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            print("Liczba nie jest pierwsza")
            return False

    print("Liczba pierwsza")
    return True


# euklides2(2)

# Eratostenes


def sito(n):
    tp = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if tp[i] == True:
            for k in range(i * i, n + 1, i):
                tp[k] = False
        i = i + 1
    return tp


wyniki = sito(100)
print("\nMetoda SITA Eratostenesa")
for i in range(2, 100):
    if wyniki[i]:
        print(i, end=" ")