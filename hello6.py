name = input("What's your nam? ")
name = name.strip() #حذف فضاهای ماقبل و مابعد (space ها)
name = name.title() #بزرگ کردن حرف اول اسم ها 
# ترتیب خط های 2 و 3 مهم هستند در زمان
print(f"Hello, {name}. How are you? ")