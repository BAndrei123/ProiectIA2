import random
from constants import cards

filename = 'cruce.in'


random_card = random.choice(cards)
# Read the content of the file
with open(filename, 'r') as file:
    lines = file.readlines()

# Modify the specific line
for i in range(len(lines)):
    if 'is_first' in lines[i]:
        lines[i] = f'is_first({random_card}).\n'
        break

# Write the updated content back to the file
with open(filename, 'w') as file:
    file.writelines(lines)