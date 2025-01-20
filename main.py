import random
import os
import time

def viewFile(file): # Création d'une fonction universelle pour ouvrir et lire un fichier ex: viewFile("nom")
    with open(file + '.txt', 'r') as f:
        data = f.read()
    return data

def randomLines(file, q): #
    l = []
    data = open(file + '.txt').read().splitlines()
    while q > 0:
        l.append(random.choice(data)) 
        q -= 1
    return l


score = 0

print(r"""
  __ _  ___ _ __ ___  
 / _` |/ __| '_ ` _ \ 
| (_| | (__| | | | | |
 \__, |\___|_| |_| |_|
    |_|               
""")

print("vous souhaitez tirer comnbien de question ?")

reponse_input = int(input())

tab = randomLines('data', reponse_input)


for i in tab:
    os.system('cls' if os.name == 'nt' else 'clear')

    # on split la question 
    question = i.split('?')[0] + '?'  # Récupérer la question jusqu'au ?
    propositions = i.split('?')[1].split(';;')[0]  # Récupérer les propositions entre ? et ;;
    reponse = i.split(';;')[1]  # Récupérer la bonne réponse apres ;;
    

    # Affichage de la question, ainsi que les propositions 
    print(f"score : {score}")
    print(question)
    print(propositions)
    
    # Demander la réponse
    u = input("Votre réponse : ").strip()
    
    # Comparaison
    if u == reponse:
        print("Gagné ! 🎉")
        score += 1
        time.sleep(3)
    else: 
        print("Perdu !  La bonne réponse était : " + reponse)
        time.sleep(3)

print(f"score final : {score} / {reponse_input} questions")
