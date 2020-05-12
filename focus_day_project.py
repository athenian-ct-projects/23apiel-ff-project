# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)

x = input("Select a Category?: ")
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
def Geography(score):
  if x == "Geography":
    s = int(input("How many points?: "))
    if s == 100:
        q = input("Which country does Harry Potter take place?: ")
        if q == "England":
          score = score +100
          print("Your score is", score, )
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
      j = input("Name one of the other schools that participated in the triwizard tournament?: "
      if j == "Beauxbatons Academy of Magic" or "Durmstrang Institute":
        score = score + 400
        print("Your score is", score, )
      else:
        score = score + 0
        print("Your score is", score, ) 
         
    





score = 0
Hogwarts(score)      
Geography(score)
    
#https://screenrant.com/harry-potter-interesting-wizarding-schools-facts/
