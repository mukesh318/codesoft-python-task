# ============================================
# CodSoft Internship - Task 2: Calculator
# ============================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Zero se divide nahi kar sakte!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "❌ Error: Zero se modulus nahi kar sakte!"
    return a % b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Valid number likho!")

def main():
    print("=" * 40)
    print("   🧮 CodSoft - Calculator App   ")
    print("=" * 40)

    while True:
        print("\n📌 Operations:")
        print("1. Addition      (+)")
        print("2. Subtraction   (-)")
        print("3. Multiplication(*)")
        print("4. Division      (/)")
        print("5. Modulus       (%)")
        print("6. Power         (^)")
        print("7. Exit")

        choice = input("\nOperation choose karo (1-7): ").strip()

        if choice == "7":
            print("👋 Calculator band ho gaya!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice! 1-7 ke beech choose karo.")
            continue

        num1 = get_number("Pehla number: ")
        num2 = get_number("Doosra number: ")

        operations = {
            "1": (add, "+"),
            "2": (subtract, "-"),
            "3": (multiply, "*"),
            "4": (divide, "/"),
            "5": (modulus, "%"),
            "6": (power, "^"),
        }

        func, symbol = operations[choice]
        result = func(num1, num2)

        if isinstance(result, str):
            print(result)
        else:
            # Show clean output (no decimal if whole number)
            if result == int(result):
                result = int(result)
            print(f"\n✅ {num1} {symbol} {num2} = {result}")

        again = input("\nAur calculation karni hai? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Calculator band ho gaya!")
            break

if __name__ == "__main__":
    main()
