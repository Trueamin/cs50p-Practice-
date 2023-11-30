def main():                                     
    name = int(input("Enter your number:  "))
    abbas = square(name)
    print(abbas)

def square(num):
    num = num * num
    return num

main()