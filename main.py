import random

items=['mango','guava','apple','orange','pineapple','lemon','cherry','watermelon','lychee','jackfruit','grapes','banana','pears','carrot','blueberry']
rand_item = items[random.randrange(len(items))]
print("Lets play")
print("Guess the word! HINT: The word is a fruit")
for i in range(len(rand_item)):
  print("_",end=" ")

#print(rand_item)
str = ["_" for j in range(len(rand_item))]
new =""
#for j in range(len(rand_item)):
# str[j] = " "


#chances loop
for k in range(len(rand_item)+2):
  print()
  if(new==rand_item):
    break
  else:
    print("Enter a letter to guess the word:",end=" ")
    x = input()
    new = ""
    #loop for getting and storing prediction
    for i in range(len(rand_item)):
      if(x==rand_item[i]):
        str[i]=x
        print(str[i],end=" ")
        for j in str: 
          new = new+j
      else:   
        print(str[i],end=" ")
      
 # print("New is ",new)




#print(str)
if(rand_item==new):
  print()
  print("congrats! You won the game")
else:
  print() 
  print("Oops! You lost")
  print("The word was %s"%rand_item)

