# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)

def Hogwarts(score):
  score = 0
  x = input("Select a Category?: ")
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
    #if y == 500: 
def geography(score):
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
Hogwarts(score)      
