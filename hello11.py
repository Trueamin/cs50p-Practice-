def main():                                     
    name = input("What's your name? ").strip().title()
    hello()

def hello(to="world"):
    print(f"Hello, {to}")

main()