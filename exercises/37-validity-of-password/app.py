from string import digits
from string import ascii_uppercase
from string import ascii_lowercase

passwords = (input()).split(",")
symbols = "$#@"
password_length = 0
valid_passwords = []

for password in passwords:
    password_length = len(password)
    digit_count = 0
    lower_char_count = 0
    upper_char_count = 0
    symbol_char_count = 0
    if 4 < password_length < 13:
        for char in password:            
            if char == " ":
                break
            elif char in symbols:
                if symbol_char_count > 0:
                    continue
                symbol_char_count += 1
            elif char in digits:
                if digit_count > 0:
                    continue
                digit_count += 1
            elif char in ascii_uppercase:
                if upper_char_count > 0:
                    continue
                upper_char_count += 1
            elif char in ascii_lowercase:
                if lower_char_count > 0:
                    continue
                lower_char_count += 1
            
        if symbol_char_count >= 1 and digit_count >= 1 and upper_char_count >= 1 and lower_char_count >= 1:
            valid_passwords.append(password)
print(",".join(valid_passwords))
