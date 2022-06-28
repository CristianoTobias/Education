frase = str(input("Type a phrase: ")).strip().upper()
print(f"The first letter A apears {frase.count('A')} times in the phrase.")
print(f"The first letter A apears at {frase.find('A') + 1} position.")
print(f"The last letter A apears at {frase.rfind('A') + 1} position.")

