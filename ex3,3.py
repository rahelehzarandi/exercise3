w1="FEMALE"
w2="female"
men1="MALE"
men2="male"
print("Please Enter biological gender (male/female :")
gender=str(input())
print("Plese Enter hemoglobin :")
hemologlobin=float(input())
if gender == w1 or gender == w2:
   if 117 <= hemologlobin <= 155:
    print("Hemoglobin value is normal for Female")
   else:
    print("Hemoglobin value is NOT normal for Female")
elif gender == men1 or gender == men2:
    if 134 <= hemologlobin <=167:
     print("Hemoglobin value is normal for male")
    else:
     print("Hemoglobin value is NOT normal for male")
else:
 print("Invalid")