#string reverse with list
string_a = "Data Structure"
reversed_string_a = string_a[::-1]
print(reversed_string_a)

print()

#string reverse with reversed() method
string_b = "Database"
reversed_string_b = "".join(reversed(string_b))
print(reversed_string_b)

print()

#string reverse with stack
def reverse_string(string_c):
    stack = []
    reversed_string_c = ""
    for c in string_c:
        stack.append(c)
    for c in range(len(stack)):
        reversed_string_c += stack.pop()
    return reversed_string_c

print(reverse_string("Python"))
