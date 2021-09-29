# Funktioner till lab 2

# Importera 
import matplotlib.pyplot as plt
import random as rnd



def poke_lasin(poke_path: str) -> list:
    """Laser in textfil medn pokemondata. 
    Returnerar lista med data [[bredd, höjd, pokemon] ... ]"""
    
    # Läser in filen och tilldelar innehållet till raa_data
    with open(poke_path,'r') as f: 
        ra_data = f.readlines()
    
    # Läs in vilken pokemon det är från namnet på textfilen
    pokemon = poke_path[ poke_path.rfind('/') + 1 : -4 ] 

    # Rensa data
    rensad_data = [] # Initera tom lista
    for rad in ra_data[1:]: # ra_data[0] inhåller överskrifter som vi inte vill ha med
        
        rad = rad.split(sep=", ") # Dela upp strängen per ", "
        rensad_data.append([float(rad[0][1:]), float(rad[1][:-2]), pokemon]) # Rensa bort onödiga tecken och typomvandla till flyttal. Lägg till i rensad_data.        

    return(rensad_data)



def testpunkter_lasin(testp_path: str) -> list:
    """Laser in textfil med testpunkter. 
    Returnerar lista med data [[bredd, höjd, "test"] ... ]"""
    
    # Läser in filen och tilldelar innehållet till ra_data
    with open(testp_path,'r') as f:    
        ra_data = f.readline()

    # Rensa data
    rensad_data = ra_data[1:-1].split(sep = "), (")    # Delar upp strängen per data par och tar bort parenteser.
    
    for i,p in enumerate(rensad_data): 
        p = p.split(sep=",")                                                    # Dela upp strängen per ", "
        rensad_data[i] = ([float(p[0].strip()), float(p[1].strip()), "test"])   # Rensa bort blanksteg och typomvandla till flyttal.        
    
    return(rensad_data)



# Bygger löst på den här sidan https://stackoverflow.com/questions/35286540/display-an-image-with-python
def visa_avatar(pokemon: str) -> None:
    '''Visar en avatar för en pokemon'''
    
    pokemons = {"pichu":"files/Pichu.png", "pikachu" : "files/Pikachu.png", "okänd" : "files/Okand.jpg"} # Dictionary med namn på pokemon och sökväg till bild. Kanske overkill för två men funktionen skulle gå att utöka för alla pokemons.

    path = pokemons[pokemon]    # välj sökväg för vald pokemon

    plt.figure(figsize=(5,5))   # Sätt storlek på figuren
    plt.axis("off")             # Stäng av axlarna i figuren
    plt.title(pokemon.title())
    bild = plt.imread(path)     # Läs in och tillela bilden till bild
    plt.imshow(bild)            # Lägg till bild i figur

    plt.show() # Gör figuren synlig



def plot_punkter(data : list, fmt: str, etikett: str) -> None:
    '''Plottar alla punkter i data = [[x1, y1], ... [xn, yn]] 
    med punktens formatering enligt fmt'''
    
    bredd = [] 
    hojd = []

    # Skapa listor som fungerar i plot så legend fungerar
    for p in data:
        bredd.append(p[0])
        hojd.append(p[1])

    # Plotta punkter    
    plt.plot(bredd, hojd, fmt, label= etikett)
        


def plot_alla(punkter_pichu: list, punkter_pikachu: list, punkter_test: list) -> None:
    '''Plottar alla data- och testpunkter i en figur'''
    
    plt.figure(dpi=150) # För att få en större figur.
    
    # Anropa plot_punkter() för att plotta varje dataset
    # TODO: om mn gör en loop på de här plottarna funkar det för n olika pokemons. Lös: label = "test"
    plot_punkter( punkter_pichu, "r*", punkter_pichu[0][2]) 
    plot_punkter( punkter_pikachu, "bo", punkter_pikachu[0][2] )
    plot_punkter( punkter_test, "cd", "test")
    
    # Fixa till figuren 
    plt.title("Bredd och höjd för varje pokemon")
    plt.xlabel("Bredd [cm]")
    plt.ylabel("Höjd [cm]")
    plt.gca().set_aspect("equal") # Sätt förhållande mellan x- och y-axel lika. Löst baserat på https://www.pythonpool.com/matplotlib-aspect-ratio/
    plt.legend(bbox_to_anchor = (1.05, 1)) # Legend utanför figuren

    plt.show()

    print("\n")



def euklidiskt_avstaand(p1:list, p2:list) -> float:
    '''Beräknar det euklidiska avståndet mellan p1 och p2'''
        
    import math as ma
    
    return ma.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 )    



def avstaand_punkter(p_test: list, punkter: list, n: int = 1):  
    """Räknar ut de n närmaste punkterna til p_test i en lista med punkter"""
    avstaand =[]
    for p in punkter:
        avstaand.append( [euklidiskt_avstaand(p, p_test), p[2]]) #.title()] ) 
    avstaand.sort()       
    return avstaand[0:n]



def poke_valj(punkter_test: list, punkter_data: list, n: int) -> list:
    '''Funktion som avgör vilken pokemon för varje testpunk, 
    utifrån en lista med minsta avstånd med tillhörande klassificering'''
    
    pokemons = []

    # Loopa genom alla testpunkter
    for p_t in punkter_test: 

        # Hittar den närmast punkten bland alla givna punkter
        min_avstand = avstaand_punkter(p_t, punkter_data, n) 
        
        # Gör en lista med bara namnen (pichu, pikachu ...) på punkterna med minst avstånd 
        pokemon = []
        for a in min_avstand: 
            pokemon.append(a[1])

        # Räkna antalet av varje pokemon i listan
        poke_antal ={}
        for p in set(pokemon):
            poke_antal[ p ] = pokemon.count(p)

        # Ta fram pokemon med det högsta antalet förekomster
        pokemon = max(poke_antal,key=poke_antal.get)

        # Kontrollera att det inte finns flera pokemons som förekommer lika många ggr
        for a in poke_antal:
            if  a != pokemon and poke_antal[a] == poke_antal[pokemon]:
                print(f"Det är går inte att avgöra vilken pokémon det är.") 
                pokemon = "okänd"
                break
        
        # Skriv ut vilken punkt och vald pokemon
        print(f"Punkt: {p_t} \nKlassificering: {pokemon}") #" \nAvstånd till närmast punkt: {min_avstand[0][0]}\n\n")
    
        # Skriv ut minsta avstånden och vad de punkterna är klassade som
        print(f"De {len(min_avstand)} närmaste avstånden är: ")
        for a in min_avstand:
            print(f"{a}")
        
        print("\n\n")
        pokemons.append(pokemon)
        

    return pokemons



def  mata_in_punkt() -> list:
    '''Tar in en punkt från användaren. Returnerar en list [bredd, höjd, "test"]'''
    max_storlek = 50 # Vad är ett rimligt värde här egentligen?
    
    # För bred och höjd
    punkt = []
    for f in ("bredden", "höjden"):
        
        # Upprepa tills användaren anger ett godkänt tal
        while True:
            
            try:
                svar = float(input(f"Ange {f} för din pokemon: "))      # Ta input från användaren
                if svar <= 0:                                           # Måtten kan inte vara negativa 
                    raise ValueError(f"Måtten ska vara större än 0: '{svar}'")    
                elif svar > max_storlek:                                # Inga orimligt stora mått
                    raise ValueError(f"Så stor är inte pokemon: '{svar}'") 
            except ValueError as err:
                print(err)
            except:
                print("Övrigt fel")
            else:
                break # Inget fel -> godkänt tal

        punkt.append(svar)

    punkt.append("test")    # Lägg till typ av punkt

    return punkt



def delaupp_data(data_punkter: list, andel: float) -> list:
    '''Funktion som tar in en lista med datapunkter och delar upp den i test- och övningsdata. 
        Andel anger hur stor andel (0 till 1) som skall vara testdata'''

    # rnd.seed(6.28318530718) 

    rnd.shuffle(data_punkter) # Blanda listan (för att få ett randomiserat urval)
    cut =int(len(data_punkter) * andel) # Beräkna var listan ska klippas utifrån angiven andel testdata

    # Dela upp datan i två listor
    tranings_p = data_punkter[:cut]     
    test_p = data_punkter[cut :]

    return [tranings_p, test_p]


def accuracy(pokemons: list, punkter_test: list) -> float:
    """Beräkna nogrannheten för modellen. Utifrån modellens resultat och testdata"""
    # accuracy = (#TP + #TN) / Total - täljaren motsvarar alla rätt klassificerade pokemons
    
    # Beräkna antalet rätt svar
    antal_ratt = 0
    for i, p in enumerate(pokemons):
        if p == punkter_test[i][2]: # Jmf modellens svar med verkligt värde
            antal_ratt += 1 

    return antal_ratt/len(punkter_test)


