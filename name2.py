name = input("Enter a name: ").lower().strip().title()

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor!")
    case "abbas":
        print()

    case _: #برای else
        print("Who?! ")