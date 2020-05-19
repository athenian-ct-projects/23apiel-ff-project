# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)


u = int(input("Are you group 1 or 2?: "))
if u == 1:
  x = input("Which category do you want to select?")
  def Hogwarts(score):
      if x == "Hogwarts":
        y = int(input("How many points?: "))
        if y == 100:
          z = int(input("How many houses are there in Hogwarts?: "))
          if z == 4:
            score = score + 100
            print("Your score is", score, )  
          else:
            score = score + 0
            print("Your score is", score, ) 
        if y == 200:
          e = int(input("What year was Hogwarts founded?: "))
          if e == 900:
            score = score + 200
            print("Your score is", score, )
          else:
            score = score + 0
            print("Your score is", score, ) 
        if y == 300:
          w = input("Which ghost haunts Gryffindor?: ")
          if w == "Nearly Headless Nick":
            score = score + 300
            print("Your score is", score, )
          else:
            score = score + 0
            print("Your score is", score, )  
        if y == 400:
          o = input("Who did Salazar Slytherin not want to attend Hogwarts?: ")
          if o == "Muggles":
            score = score + 400
            print("Your score is", score, )
          else:
            score = score + 0
            print("Your score is", score, ) 
        if y == 500: 
          d = int (input("How many stair cases does Hogwarts have?: "))
          if d == 140:
            score = score + 500
            print("Your score is", score, )
          else:
            score = score + 0
            print("Your score is", score, )
      
      return score
  def Geography(score):
      if x == "Geography":
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
  def Random_Facts(score):
      if x == "Random Facts":
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
else: 
  x = input("Which category do you want to select?")
  def Hogwarts(score2):
      if x == "Hogwarts":
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
  def Geography(score2):
      if x == "Geography":
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
  def Random_Facts(score2):
      if x == "Random Facts":
        q = int(input("How many points?: "))
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



#u = int(input("Are you group 1 or 2?: "))

print(score2)
print(score)

score = 0
score2 = 0

score = Hogwarts(score)     
score = Geography(score) 
score = Random_Facts(score)
 
score2 = Hogwarts(score2)      
score2 = Geography(score2)
score2 = Random_Facts(score2)


#https://screenrant.com/harry-potter-interesting-wizarding-schools-facts/
#https://www.cambridge-news.co.uk/news/uk-world-news/40-harry-potter-quiz-questions-18163224
#https://www.insider.com/harry-potter-little-known-facts-2019-1#to-prevent-early-leaks-of-harry-potter-and-the-deathly-hallows-the-series-publisher-bloomsbury-gave-the-seventh-and-final-book-some-quirky-codenames-17
