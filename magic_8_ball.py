import random

# this assigns a name to the name variable, a question to the question variable and sets the answer variable to an empty string, which will be later populated with different values
name = "Carl"
question = "Will I win the lottery?"
answer = ""

# this outputs a random number using the random library
random_number = random.randint(1, 12)

print(random_number)

# this set of if statements assigns a different answer to each number stored in the random_number variable
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Interesting."
elif random_number == 11:
  answer = "Not available right now."
elif random_number == 12:
  answer = "I wouldn't ask for the answer."
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

# this if statement makes sure there is a name
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

# this if statement makes sure a question is asked
if question == "":
  print("You have not asked a question. Please do it now.")
else: 
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)


