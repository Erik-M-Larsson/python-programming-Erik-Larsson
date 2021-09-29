# Main

# Importera funktioner
import lab2_fun as fun


# ********** Grundupgift **********
print("Grunduppgift\n")

# Sökvägar till filer
path_pichu = "files/pichu.txt"
path_pikachu = "files/pikachu.txt"
path_test = "files/test_points.txt"

# Läs in textfiler med data
punkter_pichu = poke_lasin(path_pichu)
punkter_pikachu = poke_lasin(path_pikachu)
punkter_test = testpunkter_lasin(path_test)

# Plotta alla punkter i en figur
plot_alla(punkter_pichu, punkter_pikachu, punkter_test)

# Avgör vilken pokemon varje testpunkt motsvarar. Jmf med 1 närmaste punkt    
poke_valj(punkter_test, punkter_pichu + punkter_pikachu, 1)



# ********** Uppgift 1 och 2 **********
print("\n\nUppgift 1 och 2\n")

# Antal närmaste punkter att jämföra med
n=5 # <------------------------------ Testa gärna n = 4 och mata in bredd = 20 och höjd = 36  :)

# Ta in data från användaren
testpunkt = mata_in_punkt()

# Avgör vilken pokemon det är
poke_valj([testpunkt], punkter_pichu + punkter_pikachu, n) 

# Plotta punkter
plot_alla(punkter_pichu, punkter_pikachu, [testpunkt] )



# ********** Uppgift 3 och 4 **********
print("\n\nUppgift 1 och 2\n")

# 90 är träningsdata (45 Pikachu, 45 Pichu)
# 10 är testdata (5 Pikachu, 5 Pichu)
andel_traningsdata = 0.90

# Antal närmaste punkter att jämföra med
n=5

# Dela upp listorna med data till träningsdata och testdata
[pichu_data, pichu_test] = delaupp_data(punkter_pichu, andel_traningsdata)
[pikachu_data, pikachu_test] = delaupp_data(punkter_pikachu, andel_traningsdata)

punkter_data = pichu_data + pikachu_data
punkter_test = pichu_test + pikachu_test

# Plotta alla punkter i en figur
plot_alla(pichu_data, pikachu_data, punkter_test)

# Avgör vilken pokemon det är
pokemons = poke_valj(punkter_test, punkter_data, n)


# Uppgift 4

# Noggrannhet
print(f"Andel korrekt klassificerade pokemons är {accuracy(pokemons,  punkter_test)}.")