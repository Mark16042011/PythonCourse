bank = {}
file1 = open("input", 'r')
file2 = open('output', 'w')
for item in file1:
    item = item.split()
    operation = item[0]
    if operation == "DEPOSIT":
        name = item[1]
        summ = int(item[2])
        if name in bank.keys():
            bank[name] += summ
        else:
            bank[name] = summ
    elif operation == "WITHDRAW":
        name = item[1]
        summ = int(item[2])
        if name in bank.keys():
            bank[name] -= summ
    elif operation == "BALANCE":
        name = item[1]
        if name in bank.keys():
            bank[name] += 0
            file2.write(f'{bank[name]}\n')
        else:
            file2.write('ERROR')
    elif operation == "TRANSFER":
        name1 = item[1]
        name2 = item[2]
        summ = int(item[3])
        if name1 and name2 in bank.keys():
            bank[name1] -= summ
            bank[name2] += summ
        else:
            if name1 not in bank.keys():
                bank[name1] = 0
            if name2 not in bank.keys():
                bank[name2] = summ
    elif operation == 'INCOME':
        for j in bank:
            if bank[j] >= 0:
                bank[j] *= 1.05
print(file2)
file1.close()
file2.close()