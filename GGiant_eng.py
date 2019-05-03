#The gentle Giant








myname=input('I am the Narrator,\nWhat is your name?')
    
       
    
print('In this story, '+myname+' will travel the Giants Realm')
          
print('After an exhausting climb on the beanstalk you finnaly arive in "CloudCity"')

print('In front of you there is a Castel, on the left there is a hut and in the right is a forest')

print('To search the Castle, press "a"')

print ('To go to the hut,press "b"')

print('To search the woods, press "c"')

opt1=input()

if opt1=='a':
    print('You have chosen to go to the Castel... After climbing 20 giant steps, you are amazed of how big it is')

if opt1=='b':
    print('The hut is o lot bigger as you approach it and you are starting to wonder what size are its inhabitants')

if opt1=='c':
    print('When entering the forest, all sorts of unearthly sounds flood the atmosphere')

while opt1=='a':
    print('At the top are two massive doors, you could go in or just search the surroundings')
    opta2=input('Type "y" to enter the Castel, or "n" to snoop around')

    if opta2=='y':
        print('The richness of the castel shows up as you enter')
        opta3=input('Would you like to take a dive in a sea of gold coins and gems/(y/n)')

        if opta3=='y':
            print('As you swim along in the sea of riches you realize that it is much deeper than you expected and drown')
            print('Unhappy end #1')
            break

        if opta3=='n':
            print('You hear some loud steps coming. Do you run and hide? (y/n)')
            opta4=input()

        if opta4=='n':
            print('You freeze to death as a hungry giant heads twoards you...\nHe grabs you and swallows you whole.')
            print('Unhappy end #2')
            break

        if opta4=='y':
                print('You have managed to hide under a giant cloth and through a small hole you can see what is going on in the room')
                print('The steps are much closer now and the silouhette of a giant person is begining to emerge')
                opta5=input('Right about now from the dust of the cloth a sneazing sensation occurs. will you hold your nose?(y/n)')
        if opta5=='y':
            print('By holding your nose for this long you begin to have an urge for a breath of air.')
            print('You take a deep breath, but from the dust you cough loudly')
            print('The giant hears this and lifts the cloth and then eats you !!!\nUnhappy end #3')
            break

        if opta5=='n':
            print('You sneeze and the Giant notices you, lifts the cloth and eats you...\nUnhappy end #4')
            break
            

    if opta2=='n':
        print('Searching throughly the soroundings u notice a big chunk of cheese in what appears to be a kitcken')
        opta6=input('You relize that you haven\'t eaten since you left, \nwould you like to eat some cheese before you keep on searching?(y/n)')

    if opta6=='y':
        print('When picking up the cheese a trigger mechanism activated that ultimatly throws a spear in you\nTragic end #1')
        break
    
    if opta6=='nn':
        print('There is nothing left to discover around here, you can move on')
        continue

while opt1=='b':
    print("The hut's door is locked")
    optb2=input('Press "y" to knock on the door or "n" to search around')

    if optb2=='y':
        print("When you knock at the door a Giant Lady opens the door:\n Aaaawww, a small human, she sais, just what I need for my bean stew") 
        print("She grabs you by the legs and throws you into hot boiling water\nTragic ending #2" )
        break

    if optb2=='n':
        print("Searching aroud you spot a loose stone and under it a key")
        optb3=input("You open the door with the key and inside you see a giant goose. Do you want to investigate? y/n")

        if optb3=="y":
            print("Over the goose's nest there are several golden eggs.\nYou put them all in your bag and can't help it to \"Woohooo!!!\" ")
            optb4=input("Right in the next moment a Giant walks in, furious with rage.Do you try to run between his legs? y/n?")
        
        if optb3=="n":
            print("The narrator rarely intervenes in a story, \n Buuut....... \n Are you nuts? \n Why not investigate?\n That's it I'm taking you out of my story! \n The storyteller has deleted you from the story. Stupid end #1")
            break

        if optb4=="y":
            print("Because the giant is slow you manageto sneak between his legs just in time before he could grab you.")
            print("The goose sees also an opportunity in this and begins to take off for the door.")
            print("You grab hold of her feathers and guide her to safety.")
            print("Congrats You Have Won The Game, And The Goose With The Golden Eggs!!!")
            break

        if optb4=="n":
            print("You try to escape by running around the room but the Giant eventually grabs you and throws you into the giant hot bean stew.\nNeedless to say you suffer a Tragic end#3")
            break
    
while opt1=='c':
    print('As you go deeper into the forest it gets darker and darker...')
    print('You are frightened by a pair of lava like eyes, and run towards the hut')
    print("The hut's door is closed with a key.")
    optb2=input('Press "y" to knock on the door or "n" to search around')

    if optb2=='y':
        print("When you knock at the door a Giant Lady opens the door:\n Aaaawww, a small human, she sais, just what I need for my bean stew.")
        print("She grabs you by the legs and throws you into hot boiling water\nTragic ending #2" )
        break

    if optb2=='n':
        print("Searching aroud you spot a loose stone and under it a key.")
        optb3=input("You open the door with the key and inside you see a giant goose. Do you want to investigate? y/n")

        if optb3=="n":
            print("The narrator rarely intervenes in a story, \n Buuut....... \n Are you nuts? \n Why not investigate?\n That's it I'm taking you out of my story! \n The storyteller has deleted you from the story. Stupid end #1")
            break
            
        if optb3=="y":
            print("Over the goose's nest there are several golden eggs.\nYou put them all in your bag and can't help it to \"Woohooo!!!\"")
            optb4=input("Right in the next moment a Giant walks in, furious with rage.Do you try to run between his legs? y/n")

        if optb4=="y":
            print("Because the giant is slow you manageto sneak between his legs just in time before he could grab you.")
            print("The goose sees also an opportunity in this and begins to take off for the door.")
            print("You grab hold of her feathers and guide her to safety.")
            print("Congrats You Have Won The Game, And The Goose With The Golden Eggs!!!")
            
            break

        if optb4=="n":
            print("You try to escape by running around the room but the Giant eventually grabs you and throws you into the giant hot bean stew.\nNeedless to say you suffer a Tragic end#3")
            break
