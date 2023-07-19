# projet7_algoInvest_bk148
 
# Résolution de problèmes avec l'algorithme python.

## Objectifs:

- Étant donné un csv avec 20 actions, créez un fichier `brutforce.py` qui contient un algorithme brutforce qui teste toutes les actions possibles qui correspondent au budget de 500,00 et qui ont le meilleur profit
- Étant donné 2 fichiers csv avec 1000 actions chacun, créez un fichier `optimized.py` avec un algorithme qui optimise la solution bruforce.


## Commencer:
**Remarque** : Assurez-vous d'avoir python, environnement virtuel et git sur votre machine :
- `python -V` : commande pour vérifier la version python si elle est installée
- vérifiez que vous avez le module venv : `python -m venv --help` sinon veuillez vérifier https://www.python.org/downloads/. Vous pouvez également utiliser n'importe quel autre environnement virtuel pour exécuter le programme (** si vous avez choisi d'utiliser un autre environnement virtuel, les commandes suivantes ne conviennent pas pour exécuter le programme **)
- `git --version` : pour vérifier votre version de git si elle est installée ou vous pouvez la télécharger sur https://git-scm.com/downloads
 1. Cloner le dépôt sur le terminal ou en invite de commande : `git clone https://github.com/jheslian/projet7-algo.git`
 2. Créer un environnement virtuel avec "venv"
- `cd projet7-algo` : pour accéder au dossier
- python -m venv ***nom de l'environnement*** : pour créer l'environnement virtuel - exemple : `python -m venv env`
3. Activez l'environnement virtuel :
pour unix ou macos :
- source ***nom d'environnement***/bin/activate - ex : `source env/bin/activate` si "env" est utilisé comme nom d'environnement
Pour les fenêtres:
- ***nom de l'environnement***\Scripts\activate.bat - ex : `env\Scripts\activate.bat`
4. Installez les packages avec pip : `pip install -r requirements.txt`
6. Lancez le programme :
pour unix ou macos : `python3 algo\bruteforce`
pour Windows : `python3 algo\bruteforce, python3 algo\optimized` 


