import random

# Initial joke collection
jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

def print_random_joke():
    """Print a random joke from the collection."""
    joke = random.choice(jokes)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()
