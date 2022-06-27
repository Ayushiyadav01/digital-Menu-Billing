yes="y"
bill=0
print("**************************WElCOME TO AMIKHYASHI**************************")
while yes=='y':

  
  print("\n\n** Menu  (press alphabet you want to order :)")
  order=input("(a) Samosa  - 40 \n(b) Pau bhaji  - 60 \n(c) Vada pau  - 20 \n(d) Chole bhature  - 120 \n(e) Sandwich  - 45 \n\n Enter your order : ")

  if order=='a':
    bill=bill+40
    print(f"\n\n\n**Your Order Details...**\n**You orderd samosa** \n**Amount your have to pay '{bill}' Rs**")
 
  elif order=='b':
    bill=bill+60
    print(f"\n\n\n**Your Order Details...**\n**You orderd pau bhaji** \n**Amount your have to pay '{bill}' Rs**")

  elif order=='c':
    bill=bill+20
    print(f"\n\n\n**Your Order Details...**\n**You orderd vada pau** \n**Amount your have to pay '{bill}' Rs** ")

  elif order=='d':
    bill=bill+120
    print(f"\n\n\n**Your Order Details...**\n**You orderd chole bhature** \n**Amount your have to pay '{bill}' Rs**")

  elif order=='e':
    bill=bill+45
    print(f"\n\n\n**Your Order Details...**\n**You orderd sandwich** \n**Amount your have to pay '{bill}' Rs**")

  else:
    print("Enter valid choise")
  
  yes=input("\nDo you want to continue (Y/N)")
  if yes=='y':
    continue
  else :
   print(f"\n\nYour Total amount is {bill} ")
   print("\n\n **THANK YOU, VISIT AGAIN**")
   break

    