from kelissword.operations import evaluate_password

# Test a password
result = evaluate_password("kelia")

print(f"Score: {result['score']}/5")
print(f"Rating: {result['rating']}")