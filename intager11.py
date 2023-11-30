def main():
    x = int(input("Number: "))

    if amghezi(x):
        print("Even")
    else :
        print("Odd")
def amghezi(number):
    if number % 2 == 0:
        return True 
    else :
        return False


main()