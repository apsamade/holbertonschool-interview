# Lockboxes

## Description
Ce projet contient un algorithme qui détermine si toutes les boîtes verrouillées peuvent être ouvertes.

## Problème
Vous avez `n` boîtes numérotées de `0` à `n-1`. Chaque boîte peut contenir des clés pour ouvrir d'autres boîtes. La boîte 0 est déjà déverrouillée. Le but est de déterminer si toutes les boîtes peuvent être ouvertes.

## Fonction
```python
def canUnlockAll(boxes)
```

### Paramètres
- `boxes` : liste de listes contenant les clés

### Retour
- `True` si toutes les boîtes peuvent être ouvertes
- `False` sinon

## Utilisation
```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True
```

## Fichiers
- `0-lockboxes.py` : contient la fonction `canUnlockAll`
- `main_0.py` : fichier de test

## Environnement
- Ubuntu 14.04 LTS
- Python 3.4.3
- Style PEP 8