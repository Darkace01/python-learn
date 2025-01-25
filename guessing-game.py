secret_word = "giraffe"
guess = ""
guess_count = 1
guess_limit = 3
out_of_guesses = False

guess = input("Enter guess: ")
while guess != secret_word and not(out_of_guesses):
    print("You have " + str(guess_limit - guess_count) + " guesses left.")
    if guess_count < guess_limit:
        guess = input("Try again 🫣: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Oh oh 🥲, You lose!")
else:
    print("You win!")