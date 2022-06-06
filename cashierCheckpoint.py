import collections
import random

# put the people in line
line = collections.deque()

line.append('Carl')

customers = ['Lebron','Cindy','Carl','Mike','Megan','Sean','Josh','Stephany','Geno','Russell','Sara','Rachel','Jose','Roseita','Yu','Ivan']

for l in range(100):

    if len(line) > 6:
        print('the last person left the line. \n')

    lineActivity = random.randrange(0,2)

    if lineActivity == 0:
        if len(line) > 0:
            line.pop()
            print('the cashier rang someone up. \n')
    if lineActivity == 1 or lineActivity == 2:
        line.append(random.choice(customers))
        print('someone got in line. \n')

print(line)