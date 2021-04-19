n = input("Input a length for the tie:")
n = int(n)
for i in range(n):
    string = '*' * i
    string += '  ' * (n - i)
    string += '*' * i
    print(string)
for i in range(n):
    string = '*' * (n - i)
    string += '  ' * i
    string += '*' * (n - i)
    print(string)
