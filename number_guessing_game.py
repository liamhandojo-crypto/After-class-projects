# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print("NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()


while count<max_attempts and guess!=secret:
    guess=int(input("Guess the secret number: "))
    count=count+1
    if guess==secret:
        print("You guessed the secret number!\nThe number was",secret)
    else:
        if guess<secret:
            diff=secret-guess
        else:
            diff=guess-secret

        if diff>=20:
            print("🧊Ice cold! Your number is very far away.")
        elif diff>=10:
            print("🥶Cold! Your number is near but not quite there.")
        elif diff>=5:
            print("🌡️Warm! Your number is near.")
        else:
            print("🔥Hot! Your number is very near!")


        remaining=max_attempts-count
        if remaining>0:
            print("Lives left:",end="")
            for i in range(remaining):
                print("❤️ ",end="")
            print()
            print()

if guess!=secret:
    print("Game over! You used all 5 attempts.\nThe secret number was",secret)
