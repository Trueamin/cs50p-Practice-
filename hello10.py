def main():                                     
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to):
    print(f"Hello, {to}")

main()