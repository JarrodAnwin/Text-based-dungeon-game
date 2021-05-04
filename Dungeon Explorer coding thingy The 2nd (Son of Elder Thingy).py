scene = 0

#The following segment of code defines the players name and making sure they want to play.

if scene == 0:
  print("What's your name?")
  playerName = input()
  print(" ")
  gameStart = "Are you ready to play?(y/n)"
  print(" ")
  print(playerName + ", " + gameStart)
  readyToPlay = input()

  if readyToPlay == "y":
    scene = scene + 1
  
  elif readyToPlay == "n":
    scene = 1234
  
  else:
    print("Not Recognized")
    exit()

#The following segment of code defines what happens in scene one, scene one takes place in a room that the player wakes up in and lasts untill they are either eaten or manage to leave.

if scene == 1:

  Scene1Question1 = " wakes in a darkened room. Do you turn on (l)ight? or crawl to the (d)oor?"
  print(" ")
  print(playerName + Scene1Question1)
  scene1Choice1 = input()

  if scene1Choice1 == "l":
    print(" ")
    print("The monster is awakened by the light. It sees you. It eats you. GAME OVER")
    scene = 0
  
  elif scene1Choice1 == "d":
    print(" ")
    print("You manage to get to the door of this mysterious room")
    Scene1Question2 = "Do you open the door?(y/n)"
    print(" ")
    print(Scene1Question2)
    scene1Choice2 = input()

    if scene1Choice2 == "y":
      print(" ")
      print("The door is unlocked and opens silently as you slip through the gap, closing the door behind you.")
      scene = scene + 1

    elif scene1Choice2 == "n":
      print(" ")
      print("Your shuffeling about has woken the monster sleeping in the corner of the room, it raises its head and stares directly at you.")
      scene = scene + .1

    else:
      print("")
      print("Not Recognized")
      exit()
  
  else:
    print(" ")
    print("Not Recognized")
    exit()
  
  if scene == 1.1:
    print(" ")
    scene1Question3 = "Do you stare back at it(s)?, or open the door and hurry though(d)?"
    print(scene1Question3)
    scene1Choice3 = input()

    if scene1Choice3 == "s":
      print(" ")
      print("By staring back at the the monster the only thing you have managed to acheive is angering the monster, it now aproaches, looking to eat you")
      scene = scene +.1

    elif scene1Choice3 == "d":
      print(" ")
      print("You quickly turn around and hurry through the door closing it behind you.")
      scene = scene +.9

    else:
      print(" ")
      print("Not Recognized")
      exit()

  if scene == 1.2:
    print(" ")
    
#The following segment of code defines what happens in scene two, scene two takes place in the hallway that the player enters when they manage to leave the room, it will last untill the player leaves the hallway.

if scene == 2:

  scene2Question1 = "You look at the hallway you have just entered, door to the room you just left at your back, and think about what to do next."