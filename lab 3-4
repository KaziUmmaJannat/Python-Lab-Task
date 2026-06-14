sum_prime = 0

for num in range(2, 1000):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += num

print("Sum of all prime numbers below 1000 =", sum_prime)