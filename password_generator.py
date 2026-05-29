# ============================================
# CodSoft Internship - Task 3: Password Generator
# ============================================

import random
import string
import pyperclip

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    # Ensure at least one char from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    score = 0
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1

    if score <= 2:
        return "🔴 Weak"
    elif score <= 4:
        return "🟡 Medium"
    else:
        return "🟢 Strong"

def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ["y", "n"]:
            return ans == "y"
        print("❌ Sirf 'y' ya 'n' likho!")

def main():
    print("=" * 45)
    print("   🔐 CodSoft - Password Generator App   ")
    print("=" * 45)

    while True:
        print("\n📌 Password Settings:")

        # Get length
        while True:
            try:
                length = int(input("Password ki length kitni chahiye? (min 4): "))
                if length >= 4:
                    break
                print("❌ Minimum 4 characters chahiye!")
            except ValueError:
                print("❌ Valid number likho!")

        # Character options
        use_upper   = get_yes_no("Uppercase letters include karo? (A-Z)")
        use_lower   = get_yes_no("Lowercase letters include karo? (a-z)")
        use_digits  = get_yes_no("Numbers include karo? (0-9)")
        use_symbols = get_yes_no("Symbols include karo? (!@#$...)")

        if not any([use_upper, use_lower, use_digits, use_symbols]):
            print("❌ Kam se kam ek option select karo!")
            continue

        # Generate multiple options
        print(f"\n🔑 Generated Passwords ({length} characters):")
        print("-" * 45)
        passwords = []
        for i in range(5):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            strength = check_strength(pwd)
            print(f"{i+1}. {pwd}  [{strength}]")
            passwords.append(pwd)
        print("-" * 45)

        # Let user pick one
        try:
            pick = int(input("\nKaunsa password use karna hai? (1-5, 0 = naya generate karo): "))
            if 1 <= pick <= 5:
                chosen = passwords[pick - 1]
                print(f"\n✅ Chosen Password: {chosen}")
                print(f"💪 Strength: {check_strength(chosen)}")

                # Try clipboard copy
                try:
                    pyperclip.copy(chosen)
                    print("📋 Password clipboard mein copy ho gaya!")
                except Exception:
                    print("📋 (Clipboard copy ke liye 'pip install pyperclip' karo)")

        except (ValueError, IndexError):
            pass

        again = input("\nAur password generate karna hai? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Password Generator band ho gaya!")
            break

if __name__ == "__main__":
    main()
