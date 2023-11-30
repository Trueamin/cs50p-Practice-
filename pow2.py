def main():                                     
    name = int(input("Enter your number:  "))

    print(square(name))

def square(num):
    num = num * num
    return num

main()