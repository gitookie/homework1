import random
with open('data.txt', 'w') as file_object:
    for i in range(100000):
        if i < 99999:
            file_object.write(str(random.randint(1, 100)) + '\n')
        else:
            file_object.write(str(random.randint(1, 100)))