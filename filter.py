def is_palindrome(n):
    if n is not None:
        temp1 = repr(n)
        temp2 = temp1[::-1]
        return temp2 == temp1
		
output = filter(is_palindrome, range(10, 1000))
print(list(output))


def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, range(16))))