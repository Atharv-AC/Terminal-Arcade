import random

AUTHOR = "Divija2612"

def run():
    print(f"🍦 Welcome to Ice Cream Machine by {AUTHOR}!")
    print("Fulfill customer orders by choosing the correct ingredients.\n")

    ingredients = [
        "Chocolate",
        "Vanilla",
        "Banana",
        "Cookie",
        "Strawberry",
        "Caramel",
        "Mint",
        "Mango"
    ]

    orders = {
    "I'm craving a tropical fruit combo.": ["Banana", "Mango"],
    "Give me the classic chocolate and vanilla flavor.": ["Chocolate", "Vanilla"],
    "I want something cool with mint and vanilla.": ["Mint", "Vanilla"],
    "Can I get a cookie caramel dessert?": ["Cookie", "Caramel"],
    "I'd love a strawberry vanilla favorite.": ["Strawberry", "Vanilla"],
    "Make me a rich chocolate cookie delight.": ["Chocolate", "Cookie"],
    "I'm in the mood for a fruity strawberry mango blend.": ["Mango", "Strawberry"],
    "Give me a refreshing mint chocolate flavor.": ["Chocolate", "Mint"]
}

    score = 0
    rounds_played = 0

    while True:
        rounds_played += 1

        description, correct_ingredients = random.choice(
            list(orders.items())
        )

        print(f"\n--- Round {rounds_played} ---")
        print("\n🧑 Customer says:")
        print(f'"{description}!"')

        print("\nAvailable ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")

        choice1 = input("\nChoose ingredient 1: ").strip().title()
        choice2 = input("Choose ingredient 2: ").strip().title()

        player_choice = {choice1, choice2}
        correct_choice = set(correct_ingredients)

        if player_choice == correct_choice:
            print("✅ Perfect order! Customer is happy!")
            score += 1
        else:
            print("❌ That's not what the customer wanted.")
            print(
                f"Correct ingredients were: "
                f"{correct_ingredients[0]} + {correct_ingredients[1]}"
            )

        print(f"⭐ Score: {score}/{rounds_played}")

        play_again = input(
            "\nWould you like to serve another customer? (y/n): "
        ).strip().lower()

        if play_again != "y":
            break

    print("\n🏆 Game Over!")
    print(f"Final Score: {score}/{rounds_played}")

    if rounds_played > 0:
        success_rate = (score / rounds_played) * 100

        if success_rate == 100:
            print("🌟 Master Ice Cream Maker!")
        elif success_rate >= 60:
            print("😄 Great job serving customers!")
        else:
            print("🍦 Keep practicing your flavor combinations!")