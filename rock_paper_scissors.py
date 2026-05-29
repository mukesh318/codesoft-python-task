# ============================================
# CodSoft Internship - Task 4: Rock Paper Scissors
# ============================================

import random

CHOICES = ["rock", "paper", "scissors"]

EMOJIS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "user" if wins[user] == computer else "computer"

def display_result(user_choice, comp_choice, result, scores):
    print("\n" + "=" * 40)
    print(f"  You:      {EMOJIS[user_choice]}  {user_choice.upper()}")
    print(f"  Computer: {EMOJIS[comp_choice]}  {comp_choice.upper()}")
    print("-" * 40)

    if result == "tie":
        print("  🤝 TIE! Barabar hai!")
    elif result == "user":
        print("  🎉 TUM JEET GAYE!")
    else:
        print("  💻 COMPUTER JEET GAYA!")

    print("-" * 40)
    print(f"  📊 Score — You: {scores['user']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")
    print("=" * 40)

def main():
    print("=" * 40)
    print("  ✂️  CodSoft - Rock Paper Scissors  ")
    print("=" * 40)
    print("\nInstructions:")
    print("  🪨 Rock   beats  ✂️  Scissors")
    print("  ✂️  Scissors beats  📄 Paper")
    print("  📄 Paper  beats  🪨 Rock")

    scores = {"user": 0, "computer": 0, "tie": 0}
    round_num = 0

    while True:
        round_num += 1
        print(f"\n🎮 Round {round_num}")
        print("Choose: (r)ock | (p)aper | (s)cissors | (q)uit")

        user_input = input("Your choice: ").strip().lower()

        if user_input == "q":
            break

        # Accept full word or first letter
        mapping = {"r": "rock", "p": "paper", "s": "scissors",
                   "rock": "rock", "paper": "paper", "scissors": "scissors"}

        if user_input not in mapping:
            print("❌ Invalid! r/p/s ya rock/paper/scissors likho.")
            round_num -= 1
            continue

        user_choice = mapping[user_input]
        comp_choice = random.choice(CHOICES)

        result = get_winner(user_choice, comp_choice)
        scores[result] += 1

        display_result(user_choice, comp_choice, result, scores)

        play_again = input("\nAur khelna hai? (y/n): ").strip().lower()
        if play_again != "y":
            break

    # Final summary
    total = scores["user"] + scores["computer"] + scores["tie"]
    print("\n" + "=" * 40)
    print("        🏆 FINAL RESULTS")
    print("=" * 40)
    print(f"  Total Rounds : {total}")
    print(f"  You Won      : {scores['user']}")
    print(f"  Computer Won : {scores['computer']}")
    print(f"  Ties         : {scores['tie']}")

    if scores["user"] > scores["computer"]:
        print("\n  🎉 Overall Winner: TUM!")
    elif scores["computer"] > scores["user"]:
        print("\n  💻 Overall Winner: COMPUTER!")
    else:
        print("\n  🤝 Overall: Barabar!")
    print("=" * 40)
    print("👋 Thanks for playing!")

if __name__ == "__main__":
    main()
