def main():
    x = int(input("Number: "))

    z = amghezi(x)

    if z:
        print("Even")
    else :
        print("Odd")
def amghezi(number):
    if number % 2 == 0:
        return True 
    else :
        return False

main()