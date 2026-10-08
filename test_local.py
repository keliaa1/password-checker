from src.kelissword.operations import evaluate_password

def run_tests():
    test_passwords = [
        "123",               # Very Weak (Only numbers, short)
        "password",          # Weak (Only lowercase, length >= 8)
        "Password123",       # Good (Uppercase, lowercase, numbers, length >= 8)
        "P@ssw0rd2026!!",    # Very Strong (All checks passed)
    ]

    print("--- Password Strength Tests ---")
    for pwd in test_passwords:
        result = evaluate_password(pwd)
        print(f"Password: '{pwd}'")
        print(f" -> Score:  {result['score']}/5")
        print(f" -> Rating: {result['rating']}\n")

if __name__ == "__main__":
    run_tests()
