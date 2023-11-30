def hello():                                     #برای تعریف تابع در python از def استفاده میکنیم
    print("Hello, ", end = "")

name = input("What's your name? ").strip().title()
hello()
print(name)
