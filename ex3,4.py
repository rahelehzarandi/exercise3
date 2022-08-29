print("Enter the year:")
leapyear=int(input())
if leapyear % 4 == 0:
  if leapyear % 100 == 0:
      if leapyear % 400 == 0:
          print("leap year")
      else:
           print("NOT leap year")
  else:
      print("leap year")
else:
 print("NOT leap year")