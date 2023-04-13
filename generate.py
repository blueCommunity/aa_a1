import random

if __name__ == '__main__':
    i = 5
    with open('sample' + str(i) + '.txt', 'w') as file:
        cols = random.sample(range(i), i)
        rows = random.sample(range(i), i)
    
        for i in range(i):
            file.write(str(rows[i]) + " " + str(cols[i]) + " 1\n")
