import random

def main():
  dice_rolls = 4
  dice_sum = 0
  for i in range(0, dice_rolls):
  	roll = random.randint(1, 6)
  	dice_sum += roll
  	print(f'You rolled a {roll}')
  print(f'You have rolled a total number of {dice_sum}')

if __name__== "__main__":
  main()