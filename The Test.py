import string
import time
import os
import random
values = dict()
def inputtxt():
    last=""
    first=input("")
    if last==first:
        last=""
        first="NULL"
    else:
        last=first
        main(first)
def test1():
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    letters = list(string.ascii_lowercase)
    numbers =list(range(1,27))
    values2 = dict(zip(numbers,letters))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    passlist = list(password)
    templet = []
    codeval = list(password)
    tempnum = []
    passwordclue = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    passwordclue = list(passwordclue)
    passwordclue = list(passwordclue)
    for x in range(len(password)):
      tempnum.append(values[codeval[x]]-values[passwordclue[x]])
    for x in range(len(password)):
     print(passwordclue[x],":",tempnum[x])
    guesses = 0
    print("Solve the puzzle:")
    while guesses <= 2:
       guesses = guesses + 1
       passwordguess = input("")
       if passwordguess == password:
          print("Correct answer")
          time.sleep(3)
          test1compl()
       elif  passwordguess == "help":
           print("a = 1")
           print("b = 2")
           print("c = 3")
           print("d = 4")
           print("e = 5")
           print("f = 6")
           print("g = 7")
           print("h = 8")
           print("i = 9")
           print("j = 10")
           print("k = 11")
           print("l = 12")
           print("m = 13")
           print("n = 14")
           print("o = 15")
           print("p = 16")
           print("q = 17")
           print("r = 18")
           print("s = 19")
           print("t = 20")
           print("u = 21")
           print("v = 22")
           print("w = 23")
           print("x = 24")
           print("y = 25")
           print("z = 26")
       elif passwordguess =="key":
           print("The key is:")
           print("a: 4=e")
           print("f: -3=c")
       elif passwordguess =="answer":
          print("Correct answer")
          time.sleep(3)
          test1compl()
       elif passwordguess =="restart":
           main(passwordguess)
       elif (guesses > 0 and guesses < 3):
          print("Incorrect", 3 - guesses, "attempts remaining.")
       elif guesses == 3:
          os.system('cls')
          print("The password was", password)
          print("Error code: id10t - self destruct sequence initiated!")
          time.sleep(5)
          for i in range(5 ,0,-1):
           print(i)
           time.sleep(1)
          os.system('cls')
          print("Goodbye")
          time.sleep(1)
          os.system('cls')
          answer =inputtxt()
          main(answer)
def begin(restarts):
    if restarts ==0:
        print("Welcome, you have been selected...")
        time.sleep(3)
        os.system('cls')
        print("No!")
        time.sleep(1)
        os.system('cls')
        print("Thank  you for being our 'willing' volunteer to partake in")
        print("this social 'experiment'.")
        time.sleep(6)
        print("Now... you have 3 tests before that test your...")
        time.sleep(3)
        print("'Ineligence'")
        time.sleep(4)
        os.system('cls')
        print("You will need to solve all of them to be granted your Free... ice cream!")
        time.sleep(6)
        print("Humans like ice cream? ")
        time.sleep(2)
        os.system('cls')
        print("RIGHT?")
        time.sleep(3)
        os.system('cls')
        print("Alright!!! Enough talking your first test will begin in 3 secondsd.")
        time.sleep(3)
        os.system('cls')
        test1()
        answer =inputtxt()
        main(answer)
    elif restarts==1:
        os.system('cls')
        print("Wait!? What is this? Did you think that you could restart The test?")
        time.sleep(6)
        print("Thats cheating!")
        time.sleep(3)
        os.system('cls')
        print("What should we have expected from you to do when we said you could")
        print("restart the level")
        time.sleep(5)
        print("But you must have known what was going to happen to you if you failed...")
        time.sleep(5)
        os.system('cls')
        print("Alright!!! Enough talking... agian your first test will begin in 3 seconds.")
        time.sleep(3)
        test1()
        answer=inputtxt()
        main(answer)
    else:
        test1()
        answer=inputtxt()
        main(answer)
def test1compl():
    os.system('cls')
    print("Congradulations! You have finished your first test.")
    time.sleep(5)
    os.system('cls')
    print("Time to increase the difficulty a little!")
    time.sleep(5)
    os.system('cls')
    print("Your second test begins...")
    time.sleep(3)
    test2()
    answer=inputtxt()
    main(answer)
def test2compl():
    os.system('cls')
    print("Congradulations! You have finished your second test.")
    time.sleep(5)
    os.system('cls')
    print("Time to increase the difficulty a little!")
    time.sleep(5)
    os.system('cls')
    print("Your final test begins...")
    time.sleep(3)
    test2()
    answer=inputtxt()
    main(answer)
def test2():
    letters = list(string.ascii_lowercase)
    numbers =list(range(1,27))
    values1 = dict(zip(letters,numbers))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    #Password calculations
    tempnum = []
    codeval = list(password)
    for x in range(len(password)):
        tempnum.append(values1[codeval[x]])
    #hint calculation part 1
    #stores each letter as a corrisponding number
    def thecypher(tempnum):
        row1 = tempnum
        print(row1[0],"  + ????   ",row1[2],"  + ????    ",row1[4],"  + ????    ",row1[6], "  + ????")
        row2 = []
        row2.append(row1[0]+row1[1])
        row2.append(row1[2]+row1[3])
        row2.append(row1[4]+row1[5])
        row2.append(row1[6]+row1[7])
        print ("   ", row2[0],"    +     ????            ",row2[2],"    +      ????")
        row3 = []
        row3.append(row2[0]+row2[1])
        row3.append(row2[2]+row2[3])
        print ("          ", row3[0],"          +              ???? ")
        row4 = sum(row3)
        print("                      ",row4)
#prints out the hint, the numbers on each line will add up to the value of row4
#each pair (number 1 and 2, 3 & 4, etc, add up to a number on the level above them) this value is placed between them on the next line
#each level needs to be solved in order to calculate the level below
    thecypher(tempnum)
    guesses = 0
    while guesses <= 2:
       guesses = guesses + 1
       passwordguess = input("")
       if passwordguess == password:
          print("Correct answer")
       elif passwordguess =="restart":
           main(passwordguess)
           test2compl()
       elif  passwordguess == "help":
           print("Like in the last test the password uses the alphabet.")
           print("The final number is the sum of all!")
       elif  passwordguess == "key":
           print("a = 1")
           print("b = 2")
           print("c = 3")
           print("d = 4")
           print("e = 5")
           print("f = 6")
           print("g = 7")
           print("h = 8")
           print("i = 9")
           print("j = 10")
           print("k = 11")
           print("l = 12")
           print("m = 13")
           print("n = 14")
           print("o = 15")
           print("p = 16")
           print("q = 17")
           print("r = 18")
           print("s = 19")
           print("t = 20")
           print("u = 21")
           print("v = 22")
           print("w = 23")
           print("x = 24")
           print("y = 25")
           print("z = 26")
       elif (guesses > 0 and guesses < 3):
          print("Incorrect", 3 - guesses, "attempts remaining.")
       elif guesses == 3:
          print("The password was", password, "better luck next time.")
          print("Error code: id10t - self destruct sequence initiated!")
          time.sleep(5)
          for i in range(5 ,0,-1):
           print(i)
           time.sleep(1)
          os.system('cls')
          print("Goodbye")
          time.sleep(1)
          os.system('cls')
#same guessing code as the last puzzle, like i litterally just copied the code... we should probably store it in a function or something in the final big version of the game
#debug shit-- uncomment if you wanna check anything specific out if the code isn't working properly
##print (password)
##print (tempnum)
##print (row1)
##print (row2)
##print (row3)
def test3():
    hours = random.randint(1,12)
    shours = str(hours).zfill(2)
    minutes = random.randint(1,59)
    sminutes = str(minutes).zfill(2)
    seconds = random.randint(1,59)
    sseconds = str(seconds).zfill(2)
    bs = random.randint(1,2)
    print("The following is written on the wall:")
    if bs == 1:
        print("Sdrawkcab")
    elif bs == 2:
        print("Frontwards")
    losestatement = "The safe exploads, you have lost. Better luck next time."
    print("The clock reads:",shours,":",sminutes,":",sseconds,"\nThere is a safe in the corner.\nYou instinctively walk to the safe. You spin it right 3 times and go to the first number.")
    def safe(hours, minutes, seconds,bs):
        if bs == 1:
            num1 = seconds
            num2 = minutes
            num3 = hours
        elif bs == 2:
            num1 = hours
            num2 = minutes
            num3 = seconds
        losestatement = "The safe exploads, you have lost. Better luck next time."
        ans1=int(input(""))
        if ans1 == num1:
            print("You make one complete left turn and go to the second number.")
            ans2 = int(input(""))
            if ans2 == num2:
                print("You turn it right to the final number.")
                ans3 = int(input(""))
                if ans3 == num3:
                    print ("The safe opens revealing a bomb. There are three exposed wires. The safe has writing on the back of the door. Cut in the following order: h, m, s")
                else:
                    print(losestatement)
                    time.sleep(5)
                    quit
            else:
                print(losestatement)
                time.sleep(5)
                quit
        elif ans1 != num1:
            print (losestatement)
            time.sleep(5)
            quit
    def gettime():
        print()
    def bomb(hours, minutes, seconds):
        lives = 1
        wires = 3
        dead = False
        if minutes%3 == 0:
            wire1 = 3
        else:
            wire1 = minutes%3
        if seconds%2 == 0:
            wire2 = 2
        else:
            wire2 = 1
        wire3 = 1
        wirestocut = [wire1,wire2,wire3]
        currentwire = 0
        print(hours,minutes,seconds)
        print (wirestocut)
        while wires != 0 and lives == 1:
            print("There are", wires, "remaining. Which of the remaining wires should you cut?")
            cut = int(input(""))
            if cut == wirestocut[currentwire]:
                print("A green light turns on")
                currentwire = currentwire + 1
                if wires ==3:
                    print("The bomb starts to tick.")
                elif wires==2:print("The bomb ticks faster.")
                wires = wires - 1
                if wires==0:
                    print("All three lights are green")
                    print("The bomb stops ticking")
            else:
                wires = wires - wires
                lives = lives - 1
                print (losestatement)
        if wires == 0 and lives != 0:
            print("The bomb has successfully been defused.")
    print(hours,minutes,seconds)
    safe(hours, minutes, seconds,bs)
    bomb(seconds, hours, minutes)

restarts=0
def main (answer):
        if answer=="start":
            restarts=0
            os.system('cls')
            begin(restarts)
        elif answer=="quit":
            quit
        elif answer=="restart":
            restarts=1
            begin(restarts)
        elif answer=="help":
            print("Type 'start' to begin, 'quit' to quit the game and")
            print(" 'restart' to restart.")
            answer =inputtxt()
            main(answer)
        elif answer=="test1":
            test1()
            answer=input("")
            main(answer)
        elif answer=="test2":
            test2()
            answer=input("")
            main(answer)
        elif answer=="test3":
            test3()
            answer=input("")
            main(answer)
        else:
            print("invalid entry type 'help'")
            answer =inputtxt()
            main(answer)

answer =inputtxt()
main(answer)
