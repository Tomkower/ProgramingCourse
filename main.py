import math

# Programo do obliczania równania kwadratowego.
print("Program oblicza rozwiązanie rónania kwadratowego ax^2+bx+c=0.")

# Jeżeli a>0 program będzie kontynuowany.
while True:
    print("Wprowadź liczbę a równania kwardatowego:")
    a = int(input())
    if (a == 0):
        print("Liczba a=0. Program zakończył swoje działanie.")
        break
    else:
        print("Wprowadź liczbę b równania kwardatowego:")
        b = int(input())
        print("Wprowadź liczbę c równania kwardatowego:")
        c = int(input())

        delta = b**2 - 4*a*c
        print("Delta równania kwadratwego wynosi ",delta)
        if (delta > 0):
            print("Równanie kwadratowe ma dwa rozwiązania.")
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print("x1 =",x1," oraz x2 =",x2,".")
        elif (delta == 0):
            print("Równanie kwadratowe ma jedno rozwiązanie.")
            x1 = (-b)/(2*a)
            print("x1 =",x1,".")
        else:
            print("Równanie kwadratowe nie ma rozwiązania.")

