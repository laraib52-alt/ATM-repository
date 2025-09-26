balance=10000
def command():
  print("\nwelcome to laraib bank")
  print("1.check balance")
  print("2.withdraw")
  print("3.deposit")
  print("4.exit")
  return int(input("Enter a command number: "))
while True:
  user_choice=command()
  if user_choice==1:
     print("show balance",balance)
  elif user_choice==2:
     print("how much amount?")
     amount=int(input("how much amount?"))
     if amount<=10000:
      balance -= amount
      print("Withdrawn:", amount)
      print("New balance:", balance)    
     else:
      print("invalid amount")
  elif user_choice==3:
       amount = int(input("How much amount to deposit? "))
       balance += amount
       print("Deposited:", amount)
       print("New balance:", balance)
  elif user_choice==4:
   choice =input("do you want to exit?(yes/no)").lower()
   if choice== "yes":
      print("good bye")
      break
  else:
       print("invalid option")
    
  


  
