from vvvCipherUtil import cipher


shifting: str = input("Please provide a positive or negative number for shifting:\n")
if shifting.isalpha():
    print("You haven't provided a valid number.")
else:
    text: str = input('Please provide a text which should be shifted:\n')
    print(f'Your shifted text:\n{cipher(text, int(shifting))}')
