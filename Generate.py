import random

a = []
note = [0, 1]
for i in range(10):
    a.append([random.choice(note), random.choice(note), random.choice(note), random.choice(note)])
print(a)
