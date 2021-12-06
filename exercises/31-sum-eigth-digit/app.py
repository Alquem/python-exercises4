every_digit_is_even = []
for num in range(1000, 3000+1):
    if (num//1000) % 2 == 0 and (num//100) % 2 == 0 and (num//10) % 2 == 0 and (num//1) % 2 == 0:
        every_digit_is_even.append(str(num))

print(",".join(every_digit_is_even))