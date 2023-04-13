import random
import math

if __name__ == '__main__':
    i =  5000
    row = int(math.sqrt(i))
    temp = range(int(math.sqrt(i)))
    with open('sample' + str(i) + '.txt', 'w') as file:
        cols = random.sample(temp, row)
        rows = random.sample(temp, row)
    
        for x in (temp):
            for y in (temp):
                file.write(str(rows[x]) + " " + str(cols[y]) + " 1\n")
