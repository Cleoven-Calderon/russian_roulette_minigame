import random

score = 0

for i in range(5):
    random_pick = random.choice(['1', '2'])
    print(random_pick)
    if random_pick == '1':
        print('YES')
        score += 1

print(f'Your final score is: {score}')
