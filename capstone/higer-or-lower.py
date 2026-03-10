import random
import json 
import copy
file_path = 'capstone/game_data.json'
with open(file_path, 'r') as file:
    DATA = json.load(file)
    data = copy.deepcopy(DATA)

def higher_or_lower():
    print("Welcome to Higher or Lower Game!")
    print("Compare the followers of two accounts and guess which one has more followers on Instagram.")
    score = 0
    game_over = False

    (compareA, compareB) = random.sample(data, k=1)[0], random.sample(data, k=1)[0]
    # remove guessed accounts from the data to avoid repetition
    data.remove(compareA)
    data.remove(compareB)

    while not game_over:
        print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}\n\n")
        print("VS\n\n")
        print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}\n\n")
        response = input("Who has more followers? Type 'A' or 'B':").lower()

        correct = 'a' if compareA['follower_count'] > compareB['follower_count'] else 'b'
        print(compareA['follower_count'], compareB['follower_count'])
        if response == correct:
            compareA = compareB
            compareB = random.sample(data, k=1)[0]
            data.remove(compareB)
            score = score + 1
        else:
            print(f"you failed {score}")
            game_over = True
            




higher_or_lower()