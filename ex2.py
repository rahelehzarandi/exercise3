print("Enter the cabin class : Lux,A,B,C :")
cabinclass=input()
if cabinclass == 'LUX' or cabinclass == 'lux':
    print("upper-deck cabin with a balcony")
elif cabinclass == 'A' or cabinclass == 'a':
    print("above the car deck, equipped with a window.")
elif cabinclass == 'B' or cabinclass == 'b':
    print("windowless cabin above the car deck")
elif cabinclass == 'C' or cabinclass == 'c':
    print("windowless cabin below the car deck.")
else:
    print("error!!! Invalid cabin class!!!")