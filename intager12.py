def main():
    x = int(input("Number: "))


    if amghezi(x):
        print("Even")
    else :
        print("Odd")

def amghezi(number):
    return True if number % 2 == 0 else False

main()