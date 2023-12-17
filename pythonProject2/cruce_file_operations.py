import ast
import os
import re
import random
from constants import CARDS


def change_file(cards_in_hand, first_card, my_turn):
    filename = 'cruce.in'

    # Read the content of the file
    with open(filename, 'r') as file:
        lines = file.readlines()


    for i in range(len(lines)):
        if 'is_first' in lines[i] and not my_turn:
            lines[i] = f'is_first({first_card}).\n'
            break
        elif 'is_first' in lines[i] and my_turn:
            lines[i] = f'%is_first({first_card}).\n'
            break

        for i in range(len(lines)):
            if '-i_place' in lines[i] and my_turn:
                lines[i]='i_place.\n'
                break
            elif 'i_place' in lines[i] and not my_turn:
                lines[i] = '-i_place.\n'
                break

    index = 0

    for i in range(len(lines)):
        if i>=902:
            if index!=len(cards_in_hand):
                lines[i] = f'your_hand({cards_in_hand[index]}).\n'
                index += 1
            elif i> (902+index-1) and i<908:
                if 'your_hand' in lines[i]:
                    lines[i]=''
    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)


def function():
    to_return = []

    commands = ["./Prover9Mace4/bin/mace4 -c -f cruce.in | ./Prover9Mace4/bin/interpformat > cruce.out"]
    for arg in commands:
        if os.system(arg) != 0:
            print("Failed to execute command " + arg)
            exit(-1)

    # Specify the path to your cruce.out file
    file_path = 'cruce.out'

    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Define a regular expression pattern to match the desired line
    your_hand = re.compile(r'relation\(your_hand\(_\), \[(.*?)\]\)')
    cards_to_place = re.compile(r'relation\(unlocked\(_\), \[(.*?)\]\)')
    cards_tromf = re.compile(r'relation\(tromf\(_\), \[(.*?)\]\)')
    cards_first_card = re.compile(r'relation\(is_first\(_\), \[(.*?)\]\)')
    # Find all matches in the file content
    matches = your_hand.findall(file_content)
    match_to_place = cards_to_place.findall(file_content)
    match_tromf = cards_tromf.findall(file_content)
    match_first_card = cards_first_card.findall(file_content)
    carti = ["10 de bata", "2 de bata", "4 de bata", "3 de bata", "9 de bata", "as de bata", "10 de verde",
             "2 de verde", "4 de verde", "3 de verde", "9 de verde", "as de verde", "10 de ghinda", "2 de ghinda",
             "4 de ghinda", "3 de ghinda", "9 de ghinda", "as de ghinda", "10 de rosu", "2 de rosu", "4 de rosu",
             "3 de rosu", "9 de rosu", "as de rosu"]

    # Print the result
    if matches:
        content_inside_brackets = matches[0]
        content_inside_brackets_to_place = match_to_place[0]
        content_inside_brackets_tromf = match_tromf[0]
        content_inside_brackets_first_card = match_first_card[0]
        # Safely evaluate the content inside brackets as a Python literal
        your_hand_array = ast.literal_eval(content_inside_brackets)
        to_place = ast.literal_eval(content_inside_brackets_to_place)
        tromf = ast.literal_eval(content_inside_brackets_tromf)
        first_card = ast.literal_eval(content_inside_brackets_first_card)
        # Print the result
        print("\n")
        print("Tromful este:")
        if tromf[0] == 1:
            print("Bata \n")
        if tromf[6] == 1:
            print("Verde\n")
        if tromf[12] == 1:
            print("Ghinda\n")
        if tromf[18] == 1:
            print("Rosu\n")
        count = 1
        print(your_hand_array)
        for i in range(0, 23):
            if first_card[i] == 1:
                print("Prima carte jos este:")
                print(carti[i])

        print("\nCartile din mana:")
        for i in range(0, 24):

            if your_hand_array[i] != 0:
                print(i)
                print(carti[i])
                if to_place[i] == 0:
                    print(str(count) + ". " + carti[i] + " (nu poti pune cartea runda asta)")
                    to_return.append((carti[i], False))
                    count += 1
                else:
                    print(str(count) + ". " + carti[i] + " (cartea asta poate fi pusa)")
                    count += 1
                    to_return.append((carti[i], True))

    else:
        print("No matching line found.")
    print(to_return)



cards_in_hand = ["bc10", "bc2","rc10","fc4","rc3"]
change_file(cards_in_hand, "gc3", False)
function()