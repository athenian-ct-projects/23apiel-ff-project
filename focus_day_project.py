# Project Description

#Focus Day: Harry Potter Day

#Written by: Annabel Piel 

#Graduating Year: 2023

#Add info about game here: I have created a Jeopardy game for Harry Potter Day this will test how well you know the Harry Potter universe:
#1.	Split the group into 2 teams.
#2.	Have one group answer the 1st question, “Are you group 1 or 2?”
#3.	Then you will be asked to select a category you have 3 options: Hogwarts, Geography, and Random Facts
#4.	After you will be asked to select an amount of points: 100, 200, 300, 400, and 500.
#5.	Then answer the question that corresponds to the number you picked.
#6.	Repeat the last 3 steps for group two, then repeat the last 3 steps for group 1, and ect.  
#7.	Once you have answered a question both teams can’t answer the question again. 
#8.	At the end of the game look at the 2 final scores and determine the winner you will only be able to play for 20 rounds.
# *you must also use correct spelling and capitalization for the code to work


# this function conains 5 questions about Hogwarts for group 1
def Hogwarts(score):  
  #This input asks the player how many points they want to get if they get the question right
    y = int(input("How many points?: "))
    #this conditional statement represent if you pick 100 points then a corresponding question will be asked
    if y == 100:
      z = int(input("How many houses are there in Hogwarts?: "))
      if z == 4:
        #if you get the question right 100 points will be added to your score
        score = score + 100
        print("Your score is", score, )  
      else:
        #if you get it wrong 0 points will be added
        score = score + 0
        print("Your score is", score, ) 
        #this conditional statement represent if you pick 200 points then a corresponding question will be asked
    if y == 200:
      e = int(input("What year was Hogwarts founded?: "))
      if e == 900:
        #if you answer the question correctly then 200 points will be added
        score = score + 200
        print("Your score is", score, )
      else:
        #if you anser the question incorrectly then 0 points will be added
        score = score + 0
        print("Your score is", score, ) 
        #this conditional statement represent if you pick 300 points then a corresponding question will be asked
    if y == 300:
      w = input("Which ghost haunts Gryffindor?: ")
      if w == "Nearly Headless Nick":
        #if you answer the question correctly then 300 points will be added
        score = score + 300
        print("Your score is", score, )
      else:
        #if you anser the question incorrectly then 0 points will be added
        score = score + 0
        print("Your score is", score, )  
        #this conditional statement represent if you pick 400 points then a corresponding question will be asked
    if y == 400:
      o = input("Who did Salazar Slytherin not want to attend Hogwarts?: ")
      if o == "Muggles":
        #if you answer the question correctly then 400 points will be added
        score = score + 400
        print("Your score is", score, )
      else:
        #if you anser the question incorrectly then 0 points will be added
        score = score + 0
        print("Your score is", score, )
        #this conditional statement represent if you pick 400 points then a corresponding question will be asked 
    if y == 500: 
      d = int (input("How many stair cases does Hogwarts have?: "))
      if d == 140:
        #if you answer the question correctly then 500 points will be added
        score = score + 500
        print("Your score is", score, )
      else:
        #if you anser the question incorrectly then 0 points will be added
        score = score + 0
        print("Your score is", score, )         
    return score
# this function conains 5 questions about harry potter geography for group 1
def Geography(score):
    s = int(input("How many points?: "))
    if s == 100:
      q = input("Which country does Harry Potter take place?: ")
      if q == "England":
        score = score +100
        print("Your score is", score,)
      else: 
        score = score + 0
        print("Your score is", score, ) 
      if s == 200:
        f = input("What is the name of the prison that Sirius Black escaped from?: ")
        if f == "Azkaban":
          score = score + 200
          print("Your score is", score, )
        else:
          score = score + 0
          print("Your score is", score, )  
      if s == 300:
        r = input("Where do students of Hogwarts get their supplies for the upcoming school year?: ")
        if r == "Diagon Alley":
          score = score + 300
          print("Your score is", score, ) 
        else:
          score = score + 0
          print("Your score is", score, )
      if s == 400:
        e = input("What was the name of the tree Harry and Ron crashed their car into?: ")
        if e == "The Whomping Willow":
          score = score + 400
          print("Your score is", score, )
        else:
          score = score + 0
          print("Your score is", score, )
      if s == 500:
        h = input("What is the Dursely's address? ")
        if h == "4 Privet Drive":
          score = score + 500
          print("Your score is", score, )
        else:
          score = score + 0
          print("Your score is", score, ) 
        
      return score
# this function conains 5 questions about Random Harry Potter Facts for group 1
def Random_Facts(score):
    q = int(input("How many points?: "))
    if q == 100:
      w = input("What does Dumbledore mean in Old English?: ")
      if w == "Bumblebee":
        score = score + 100
        print("Your score is", score, )
      else: 
        score = score + 0
        print("Your score is", score, )
    if q == 200:
      o = input("What is the name of Hagrid's dog?: ")
      if o == "Fang":
        score = score + 200
        print("Your score is", score, )
      else:
        score = score + 0
        print("Your score is", score, ) 
    if q == 300:
      g = input("What is Tom Riddle's middle name?: ")
      if g == "Marvolo":
        score = score + 300
        print("Your score is", score, ) 
      else:
        score = score + 0
        print("Your score is", score, )
    if q == 400:
      t = input("What position did Harry Potter play on the Quidditch team?: ")
      if t == "Seeker":
        score = score + 400
        print("Your score is", score, )
      else:
        score = score + 0
        print("Your score is", score, )
    if q == 500:
        l = input("What is the name of people who can talk to snakes?: ")
        if l == "Parseltongue":
          score = score + 500
          print("Your score is", score, )
        else:
          score = score + 0
          print("Your score is", score, )
    return score
# this function conains 5 questions about Hogwarts for group 2
def Hogwarts2(score2):
    y = int(input("How many points?: "))
    if y == 100:
      z = int(input("How many houses are there in Hogwarts?: "))
      if z == 4:
        score2 = score2 + 100
        print("Your score is", score2, )  
      else:
        score2 = score2 + 0
        print("Your score is", score2, ) 
    if y == 200:
      e = int(input("What year was Hogwarts founded?: "))
      if e == 900:
        score2 = score2 + 200
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, ) 
    if y == 300:
      w = input("Which ghost haunts Gryffindor?: ")
      if w == "Nearly Headless Nick":
        score2 = score2 + 300
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, )  
    if y == 400:
      o = input("Who did Salazar Slytherin not want to attend Hogwarts?: ")
      if o == "Muggles":
        score2 = score2 + 400
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, ) 
      if y == 500: 
        d = int (input("How many stair cases does Hogwarts have?: "))
        if d == 140:
          score2 = score2 + 500
          print("Your score is", score2, )
        else:
          score2 = score2 + 0
          print("Your score is", score2, )
    return score2
# this function conains 5 questions about harry potter geography for group 2
def Geography2(score2):
    s = int(input("How many points?: "))
    if s == 100:
      q = input("Which country does Harry Potter take place?: ")
      if q == "England":
        score2 = score2 +100
        print("Your score is", score2,)
      else: 
        score = score + 0
        print("Your score is", score2, ) 
    if s == 200:
      f = input("What is the name of the prison that Sirius Black escaped from?: ")
      if f == "Azkaban":
        score2 = score2 + 200
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, )  
    if s == 300:
      r = input("Where do students of Hogwarts get their supplies for the upcoming school year?: ")
      if r == "Diagon Alley":
        score2 = score2 + 300
        print("Your score is", score2, ) 
      else:
        score2 = score2 + 0
        print("Your score is", score2, )
    if s == 400:
      e = input("What was the name of the tree Harry and Ron crashed their car into?: ")
      if e == "The Whomping Willow":
        score2 = score2 + 400
        print("Your score is", score2, )
      else:
          score2 = score2 + 0
          print("Your score is", score2, )
    if s == 500:
      h = input("What is the Dursely's address? ")
      if h == "4 Privet Drive":
        score2 = score2 + 500
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, ) 
    return score2
# this function conains 5 questions about Random Harry Potter Facts for group 2
def Random_Facts2(score2):
    q = int(input("How many points?: "))
    #if you pick 100 from the Random Facts category you will be asked a question if you get it right then you will get 100 points if you get it wrong then you will get no points this is the same for each number of points the only differnece is that you can get more
    if q == 100:
      w = input("What does Dumbledore mean in Old English?: ")
      if w == "Bumblebee":
        score2 = score2 + 100
        print("Your score is", score2, )
      else: 
        score2 = score2 + 0
        print("Your score is", score2, )
    if q == 200:
      o = input("What is the name of Hagrid's dog?: ")
      if o == "Fang":
        score2 = score2 + 200
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, ) 
    if q == 300:
      g = input("What is Tom Riddle's middle name?: ")
      if g == "Marvolo":
        print("Your score is", score2, ) 
      else:
        score2 = score2 + 0
        print("Your score is", score2, )
    if q == 400:
      t = input("What position did Harry Potter play on the Quidditch team?: ")
      if t == "Seeker":
        score2 = score2 + 400
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, )
    if q == 500:
      l = input("What is the name of people who can talk to snakes?: ")
      if l == "Parseltongue":
        score2 = score2 + 500
        print("Your score is", score2, )
      else:
        score2 = score2 + 0
        print("Your score is", score2, )
    return score2


#this part let's the code know that score and score2 start of with he value of 0
score = 0
score2 = 0
#score = score + score
#score2 = score2 + score2
#the for statement will make the code run 10 times 
#n=4
for n in range(10):
  #this input determines if you are team 1 or 2 depending on your team it will take you to your code
  u = int(input("Are you group 1 or 2?: "))
  if u == 1:  
    #the while statement means as long as team 1's score is greater or equal to zero and less than 2500 the code underneath will run
    while score >= 0 and score < 2500:
      #this input asks you which category you want to select and will take you to the correpsonding function
      x = input("Which category do you want to select?")
      if x == "Hogwarts":
        #this line adds up team 1's score
        score = Hogwarts(score)
        break
      if x == "Geography":
        #this line adds up team 1's score
        score = Geography(score)
        break
      if x == "Random Facts":
        #this line adds up team 1's score
        score = Random_Facts(score)
        break
          
  else:
    #the while statement means as long as team 1's score is greater or equal to zero and less than 2500 the code underneath will run
    while score >= 0 and score < 2500:
      t = input("Which category do you want to select? ")
      if t == "Hogwarts":
        #this line adds up team 2's score
        score2 = Hogwarts2(score2)
        #print(score2)
        break
      if t == "Geography":
        #this line adds up team 2's score
        score2 = Geography2(score2)
        #print(score2)
        break
      if t == "Random Facts": 
        #this line adds up team 2's score
        score2 = Random_Facts2(score2)
        #print(score2)
        break








#https://screenrant.com/harry-potter-interesting-wizarding-schools-facts/
#https://www.cambridge-news.co.uk/news/uk-world-news/40-harry-potter-quiz-questions-18163224
#https://www.insider.com/harry-potter-little-known-facts-2019-1#to-prevent-early-leaks-of-harry-potter-and-the-deathly-hallows-the-series-publisher-bloomsbury-gave-the-seventh-and-final-book-some-quirky-codenames-17
