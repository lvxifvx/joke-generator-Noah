import random

# Dictionnaire de blagues par catégorie
jokes = {
    "PROGRAMMATION": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "There are only 10 types of people in the world: those who understand binary, and those who don’t.",
    ],
    "GENERAL": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    ]
}

def print_random_joke(category=None):
    """Affiche une blague aléatoire. Si une catégorie est donnée, elle est utilisée."""
    if category and category.upper() in jokes:
        joke = random.choice(jokes[category.upper()])
        print(f"[{category.upper()}] {joke}")
    else:
        cat = random.choice(list(jokes.keys()))
        joke = random.choice(jokes[cat])
        print(f"[{cat}] {joke}")

