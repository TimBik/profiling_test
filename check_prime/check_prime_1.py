import math


def check_prime(number: int) -> bool:
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / 2).is_integer():
            return False
    return True


ten_seven = int(1e7)

print(check_prime(ten_seven))
# check_prime(10,000,000) = False
print(check_prime(ten_seven + 19))
# check_prime(10,000,019) = True
