import random

#input for how many names you would like to create
ec2_amount = int(input("How many EC2 instances do you want names for? "))
department_name = input("What is your department name? ")
characters = ['&', '*', '$', '?', '@', '^', '%', '_', '#', '!!']

count = ec2_amount  # set it to variable count. This is the number of times to print names
for i in range(count):
  numbers = random.randrange(100)
  shuffle_name = department_name + random.choice(characters) + str(numbers)
  print( f"{shuffle_name}")