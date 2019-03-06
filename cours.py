#Assignement de variables
# a = 1                     Type = INT
# a = 1-1+1                 Type = INT
# a = sin(0)                Type = INT
# a = "ce string vaut 1"    Type = STRING
# a = 1.0                   Type = FLOAT
# a = True                  Type = BOOL
# a = False                 Type = FALSE

# Operateurs :
# + addition
# - soustraction
# / division
# // division euclidienne
# % modulo
# ** puissance
# = égalité
# != inégalité

a = 5
b = 2 
c = a + b 
print(c) #Output le résultat de l'addition de 5 et 2 soit 5
c = a-b 
print(c) #Output le résultat de la soustraction de 5 par 2 soit 3.
c = a // b 
print(c) #Output le résultat de la division euclidienne de 5 par 2 soit 2
c = a % b 
print(c) #Output le reste de la division euclidienne de 5 par 2 soit 1
c = a ** b 
print(c) #Output le reste de 5 à la puissance 2 soit 25

#Fonctions:
# print(variable) : Permet d'imprimer sur la console une variable.
# input(Texte a afficher) : permet de demander à l'utilisateur une variable :
# \n sert a sauter une ligne : c'est la commande newline

a = input("Quel nombre choissisez vous ? \n ")

print("Vous avez choisi le nombre " + a)

#Exercices : 
#EX 1:
#Créer un nouveau programme en python nommé addition : demandez un input de des nombres, les additionner et imprimer le résultat.
#Ajouter l'addition, la soustraction et la multiplication au programme.
#EX 2:
#Demander à l'utilisateur son prénom et afficher un message de bienvenue contenant son prénom.
#EX 3:
#Demander à l'utilisateur le nombre de parts de pizzas d'une pizza et le nombre de personnes avec qui la partager. Imprimer combien de parts par personnes
# et combien de parts il restera.