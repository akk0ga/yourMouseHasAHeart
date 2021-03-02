# filename
log = 'log.txt'
average_log = 'average_log.txt'

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
        if 'average :' in line:
            break
        if not 'mouse position :' in line:
            datas.append(line)
    data.close()

# convert string to int
for value in datas:
    datas[i] = int(value.rstrip())
    i += 1
    total += 1

# calc the average
for value in datas:
    moyenne += abs(value)
total = moyenne // total

print(f'la moyenne est de : {total}')

# add the average in the file
with open(average_log, 'a') as log:
    log.write(f'{total}\n')
    log.close()
