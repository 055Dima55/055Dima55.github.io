import random


password_length = int(input('Enter a number of at least 5: '))
list = (1, 2, 3, 4, 5, 6, 7, 8, 'A', 'a', 'B', 'b', 'C', 'c', 'Ц', 'Г', 'х', 'й', 'Т',)

our_pass = []
for i in range(0, password_length):
    our_pass.append(random.choice(list))
print(our_pass)
