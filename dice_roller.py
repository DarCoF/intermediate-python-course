import random

def main():
  dice_rolls = 4
  dice_sum = 0
  for i in range(0, dice_rolls):
  	roll = random.randint(1, 6)
  	dice_sum += roll
  	if roll == 1:
  		print(f'You rolled a {roll} Daaaamn!')
  	elif roll == 2:
  		print(f'You rolled a {roll} Far far away!')
  	elif roll==3:
  		print(f'You rolled a {roll} Rotate Cat Smile!')
  	elif roll==4 or roll==5:
  		print(f'You rolled a {roll} Close to the bullseye!')
  	else:
  		print(f'You rolled a {roll} Critical Success!')

  print(f'You have rolled a total number of {dice_sum}')

if __name__== "__main__":
  main()