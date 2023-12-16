import random

filename = 'cruce.in'


cards=["bc10","bc2","bc3","bc4","bc9","bca","fc10","fc2","fc3","fc4","fc9","fca","gc10","gc2","gc3","gc4","gc9","gca","rc10","rc2","rc3","rc4","rc9","rca"]
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