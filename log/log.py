# filename
log = 'log.txt'

# stock value from the file
datas = []

# iterate the datas
i = 0

# to calc the moyenne
moyenne = 0
total = 0

# stock value in the datas
with open(log, 'r') as data:
    # read the line to display only values get
    for line in data:
        if not 'mouse position :' in line:
            datas.append(line)
    data.close()

# convert string to int
for value in datas:
    datas[i] = int(value.rstrip())
    i += 1
    total += 1

for value in datas:
    moyenne += abs(value)

total = moyenne // total

print(f'la moyenne est de : {total}')
