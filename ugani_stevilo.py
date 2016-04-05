x = int(raw_input("Uganite zmagovalno stevilko: "))
while True:

    if x > 33:
       print ("Vnesena stevilka je previsoka!")
       x=int(raw_input("Vnesi drugo stevilko "))

    elif x < 33:
        print ("Vnesena stevilka je prenizka!")
        x=int(raw_input("Vnesi drugo stevilko "))

    elif x == 33:
        break

print("Cestitamo!!! Uganili se pravilno stevilko")
