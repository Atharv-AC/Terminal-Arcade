from collections import Counter

AUTHOR = "Atharv-AC"

WORDS = [
    "python",
    "script",
    "terminal",
    "program",
    "variable",
    "function",
    "computer",
    "keyboard",
    "monitor",
    "internet",
    "database",
    "network",
    "binary",
    "system",
    "memory",
    "rocket",
    "planet",
    "garden",
    "castle",
    "bridge",
    "forest",
]


def get_best_letter(candidates, guessed):
    counter = Counter()

    for word in candidates:
        for letter in set(word):
            if letter not in guessed:
                counter[letter] += 1

    if not counter:
        return None

    return counter.most_common(1)[0][0]


def run():
    print(f"Game by {AUTHOR}")
    print("=== Reverse Hangman ===")
    print("Think of a secret word.")
    print("Answer only with y or n.\n")

    while True:
        try:
            length = int(input("Enter the length of your word: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    candidates = [word for word in WORDS if len(word) == length]

    if not candidates:
        print("Sorry, I don't know any words of that length.")
        return

    guessed = set()

    while len(candidates) > 1:
        letter = get_best_letter(candidates, guessed)

        if letter is None:
            break

        guessed.add(letter)

        answer = input(f"Is the letter '{letter}' in your word? (y/n): ").strip().lower()

        while answer not in ("y", "n"):
            answer = input("Please enter y or n: ").strip().lower()

        if answer == "y":
            candidates = [w for w in candidates if letter in w]
        else:
            candidates = [w for w in candidates if letter not in w]

        print(f"Possible words remaining: {len(candidates)}")

    print()

    if len(candidates) == 1:
        print(f"My guess is: {candidates[0]}")
    elif len(candidates) > 1:
        print("I couldn't narrow it down to one word.")
        print("Possible words:")
        for word in candidates[:10]:
            print("-", word)
    else:
        print("No matching word found.")