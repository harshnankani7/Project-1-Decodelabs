print("===================================")
print("      PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

score = 0

if length_ok:
    score += 1

if has_upper:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

print("\nPassword Analysis:")
print("-------------------")
print("Length >= 8:", length_ok)
print("Uppercase letter:", has_upper)
print("Number:", has_digit)
print("Symbol:", has_symbol)

if not length_ok:
    strength = "WEAK"
elif score == 4:
    strength = "STRONG"
elif score >= 2:
    strength = "MEDIUM"
else:
    strength = "WEAK"

print("\nPassword Strength:", strength)