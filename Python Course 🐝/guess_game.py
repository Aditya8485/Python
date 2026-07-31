secret_key = "Adi"
guess = ""
guess_count = 0
guess_limit = 3
ran_out_guesses = False




while guess != secret_key and not (ran_out_guesses):
    if guess_count < guess_limit:
        guess = input("Guess The Secret Key : ")
    guess_count += 1
else:
    ran_out_guesses = True
if ran_out_guesses:
    print("Ran out guesses , YOU LOSE!...")
else :
    print("YOU WIN!...")












