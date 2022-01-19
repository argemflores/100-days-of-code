rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint

# list allowed hand choices
hand = [rock, paper, scissors]

# ask player for their hand
player = int(input('What do you choose? 0 = Rock 🪨 1 = Paper 📃 2 = Scissors ✂️\n'))

# generate a random hand for the computer
computer = randint(0, 2)

# invalid player choice
if player not in [0, 1, 2]:
    print('❌ Invalid hand!')
else:
    if player == 0 and computer == 2:
        # rock beats scissors; player wins
        decision = 'You win! 👍'
    elif computer == 0 and player == 2:
        # rock beats scissors; computer wins
        decision = 'You lose! 👎'
    elif player > computer:
        # paper beats rock, scissors beats paper; player wins
        decision = 'You win! 👍'
    elif player < computer:
        # paper beats rock, scissors beats paper; computer wins
        decision = 'You lose! 👎'
    elif player == computer:
        # same hand choices; draw
        decision = 'Draw! ✋'

    # print hand choices and decision
    print('Player', hand[player])
    print('Computer', hand[computer])

    print(decision)
