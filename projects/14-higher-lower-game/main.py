# Higher Lower Game

# import libraries and files
from random import randint
from replit import clear
import art
import game_data

# define global constants
DATA_LENGTH = len(game_data.data)

# get random index from 0 to DATA_LENGTH - 1
def get_random_index():
    return randint(0, DATA_LENGTH - 1)

# get random index except the provided index
def get_index_except(except_index=[]):
    # get random index
    index = get_random_index()

    # loop until new index is found
    while index in except_index:
        index = get_random_index()

    return index

# print item contents
def show_item(index, item):
    print("❓ Compare {}: {}, {} from {}".format(index, item['name'], item['description'], item['country']))

# ask player of their chosen item
def ask_choice():
    # ask player
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # prompt again if choice is not A or B
    while choice not in ['A', 'B']:
        choice = input("Try again. Who has more followers? Type 'A' or 'B': ").upper()

    # get the other choice
    if choice == 'A':
        not_chosen = 'B'
    else:
        not_chosen = 'A'

    return (choice, not_chosen)

def show_result(is_correct, items, score):
    if is_correct:
        print("✅ You're right! 😄 {} ({}M) vs. {} ({}M) Current score: {}\n".format(\
                    items['A']['name'], items['A']['follower_count'],\
                    items['B']['name'], items['B']['follower_count'],\
                    score))
    else:
        print("\n❌ You lost! 😭 {} ({}M) vs. {} ({}M) Final score: {}".format(\
                    items['A']['name'], items['A']['follower_count'],\
                    items['B']['name'], items['B']['follower_count'],\
                    score))

# run main
def main():
    # define local variables
    is_alive = True
    score = 0
    items = {}
    winning_index = None
    prev_indices = []

    # loop game until over
    while is_alive:
        # clear screen then print logo
        clear()
        print(art.logo)

        if score > 0 and items != {}:
            show_result(True, items, score)

        # get random index (must be different)
        if winning_index is None:
            index_a = get_index_except(prev_indices)
        else:
            index_a = winning_index

        index_b = get_index_except(prev_indices)

        # set up items for display and comparison
        items = {'A': game_data.data[index_a], 'B': game_data.data[index_b]}

        # show information of the 2 random items
        show_item('A', items['A'])
        print(art.vs)
        show_item('B', items['B'])
        print()

        # ask player
        chosen, not_chosen = ask_choice()

        # check if player continues or not
        if items[chosen]['follower_count'] > items[not_chosen]['follower_count']:
            # player continues with additional score
            score += 1

            # carry over winning item to next round
            if items[chosen]['name'] == items['A']['name']:
                winning_index = index_a
            else:
                winning_index = index_b
        else:
            # player loses
            is_alive = False

        # do not use previous choices
        prev_indices = [index_a, index_b]
    else:
        show_result(False, items, score)

if __name__ == "__main__":
    main()
