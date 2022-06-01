meny = [1, 'Vaffler', 15, 2, 'Sjokoekake', 20, 3, 'Hamburger', 149, 4, 'Rekesalat', 89, 5, 'Kaffe', 15, 6, 'Brus', 25]

bestilling = []

def main():

    print("Bestille servering via app ")

    while True:

        for v in range(0,len(meny),3):

            print(f'{meny[v]}: {meny[v+1]} \t kr: {meny[v+2]}')

        vare = int(input("Hvilken vare ønsker du? (0 for å sende bestilling)"))

        if vare <= len(meny)/3:

            bestilling.append(meny[(3*vare)-3])

            bestilling.append(meny[(3*vare)-2])

            bestilling.append(meny[(3*vare)-1])

            print("Du har bestilt:")
       
        for v in range (0,len(meny),3):
            if meny[v] == vare:
                print (bestilling)
            else:
                pass
        
        totalpris = 0

        for v in range(0,len(bestilling),3):

            totalpris += bestilling[v+2]

        print("Totalprisen er kr: ", totalpris)

        valg = input("ønsker du og betale? ") 
        if valg == "ja":
            print("takk for din bestilling")
            break

main()