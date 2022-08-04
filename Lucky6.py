import random
import time


def lucky6():

    print("Brojevi u igri moraju biti izmedju 1 i 48.")

    brojevi = (input("Unesite 6 brojeva, tako da ih razdvojite razmakom.\n")).split(" ") 
    brojevi = [int(i) for i in brojevi]

    uplata = int(input("Unesite vasu uplatu: "))

    kvote = [10000, 7500, 5000, 2500, 1000, 500, 300, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    br_izvucenih = 0
    pauza = 3
    pogodjeni = []
    pozicija = 0
    
    rand_izvuceni = random.sample(range(1, 48), 35)
	
    if len(brojevi) == 6:

        for broj in rand_izvuceni:

        	br_izvucenih += 1
        	print(f"Broj {br_izvucenih}: {broj}")
        	time.sleep(pauza)
        	
        neki_pogodak = any(x in brojevi for x in rand_izvuceni)    

        for broj in rand_izvuceni:
            
            if broj in brojevi:

                pogodjeni.append(broj)

            pozicija += 1            
            
            if len(pogodjeni) == 6:

                kvota = int(kvote[pozicija - 5])
                dobitak = uplata * kvota
                print("Cestitamo!")
                print(f"Vas ukupni dobitak je: {dobitak} !")
                break    
            
        if neki_pogodak:
        
            print(f"Ostvarili ste {len(pogodjeni)} pogodaka/tka i to brojeve: {sorted(pogodjeni)} , pokusajte ponovo.")   

        else:
        
            print("Bas nista niste pogodili, mozda ova igra nije za vas.")   

    else:    
    
        print("Morate uneti tacno 6 brojeva!")         

if __name__ == "__main__":

    lucky6()
