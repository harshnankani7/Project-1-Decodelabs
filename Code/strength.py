password = input("Enter your password: ")

if len(password) < 8:
    print("Password Strength: WEAK")
else:
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if has_upper and has_digit and has_symbol:
        print("Password Strength: STRONG")
    elif has_upper or has_digit or has_symbol:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: WEAK")