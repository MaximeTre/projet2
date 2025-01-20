# Quiz Terminal Python

Un jeu de quiz simple en terminal utilisant des fichiers texte comme source de données. Les questions sont choisies aléatoirement, et le joueur doit répondre correctement pour accumuler des points.

---

## Table des matières

1. [À propos](#à-propos)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Format du fichier de données](#format-du-fichier-de-données)
6. [Contributions](#contributions)
7. [Licence](#licence)

---

## À propos

Ce projet est une application Python qui génère un quiz interactif à partir d'un fichier texte contenant des questions et des réponses. Il permet de tester ses connaissances de manière ludique directement dans le terminal.

---

## Fonctionnalités

- Lecture des questions à partir d'un fichier texte (`data.txt`).
- Sélection aléatoire des questions.
- Gestion des scores avec affichage en temps réel.
- Interface simple et intuitive dans le terminal.
- Compatibilité multiplateforme (Windows, macOS, Linux).

---

## Installation

### Prérequis

- Python 3.x
- Un fichier `data.txt` contenant les questions et les réponses (voir le [format](#format-du-fichier-de-données)).

### Étapes

1. Clonez le dépôt ou copiez les fichiers dans un dossier local :
   ```bash
   git clone https://github.com/votre_nom/quiz-terminal.git
   cd quiz-terminal
    ```
2. (Facultatif) Créez et activez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate      # Sur macOS/Linux
venv\Scripts\activate         # Sur Windows
```

4. Assurez-vous que le fichier data.txt est présent dans le même dossier que le script.

## Utilisation

1. Exécutez le script Python :

    ```bash
        python main.py
    ```

2. Entrez le nombre de questions que vous souhaitez répondre.
3. Répondez aux questions affichées. Votre score sera mis à jour en temps réel.
4. À la fin du quiz, votre score final sera affiché.

## Format du fichier de données

Le fichier data.txt doit contenir les questions et réponses au format suivant :

    ```bash
        Question 1 ? Propositions (séparées par des virgules) ;; Réponse correcte
        Question 2 ? Propositions (séparées par des virgules) ;; Réponse correcte
        ...
    ```

### Exemples

    ```bash
        Quelle est la capitale de la France ? Paris, Londres, Madrid ;; Paris
        Quelle est la couleur du ciel par temps clair ? Bleu, Rouge, Vert ;; Bleu
    ```

---

# Contributions

Les contributions sont les bienvenues ! Si vous souhaitez ajouter des fonctionnalités ou corriger des bugs, suivez ces étapes :

1. Forkez ce dépôt.

2. Créez une nouvelle branche pour vos modifications :

    ```bash
        git checkout -b ma-nouvelle-fonctionnalite
    ```

3. Apportez vos modifications et committez-les :

    ```bash
        git commit -m "Ajout de ma nouvelle fonctionnalité"
    ```

Poussez vos modifications vers votre fork :

    ```bash
        git push origin ma-nouvelle-fonctionnalite
    ```

Ouvrez une Pull Request pour révision.
