print("1 signifies stone")
print("2 signifies paper")
print("3 signifies scissor")
def stonepaperscissorcut(num):
  import random
  comp_out = random.randint(1,3)
  print("Computer's output: ", comp_out)
  if num == comp_out:
    print("It's a draw, try again")
  elif num == 1 and comp_out == 2:
    print("You lost the game!")
  elif num == 1 and comp_out == 3:
    print("You won the game!")
  elif num == 2 and comp_out == 1:
    print("You won the game!")
  elif num == 2 and comp_out == 3:
    print("You lost the game!")
  elif num == 3 and comp_out == 1:
    print("You lost the game!")
  elif num == 3 and comp_out == 2:
    print("You won the game!")
  else:
    print("Wrong Input!")
stonepaperscissorcut(3)
