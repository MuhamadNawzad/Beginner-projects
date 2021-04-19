for i in range(1, 10):
    table_row = ''
    for j in range(1, 10):
        table_row += str(i) + "*" + str(j) + "=" + str(i * j) + '\t'
    print(table_row)
print()
for i in range(1, 10):
    table = []
    for j in range(1, 10):
        k = str(i) + '*' + str(j) + '=' + str(i * j)
        table.append(k)
    print(*table, sep='\t')
