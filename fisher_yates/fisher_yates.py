import os
import random

def fisher_yates_shuffle(deck):
    n = len(deck)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

# Crear el arreglo de cartas de poker
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [rank + ' of ' + suit for suit in suits for rank in ranks]

# Generar una semilla aleatoria utilizando la entropía del sistema
seed = int.from_bytes(os.urandom(4), byteorder='big')

# Establecer la semilla del generador de números aleatorios
random.seed(seed)

# Barajear el arreglo de cartas
fisher_yates_shuffle(deck)

# Imprimir las cartas barajeadas
for card in deck:
    print(card)
