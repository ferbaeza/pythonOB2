def check_prime(number):
    for n in range (1, number+1):
        if n>1:
            for i in range (2, n):  
                if (n % i) == 0:  
                    break  
            else:  
                print (n)  


def main():
    print("Ejercicio Tres")
    print("**************")
    number = int(input("Introduce un numero :  "))
    check_prime(number)


if __name__=="__main__":
    main()