print("Este programa te indica si el número que introduces es primo.")
n = int(input("Introduce un número: "))
for i in range(1,n):
    if n//i == 0:
        print("Su número no es primo :c")
        break
    
