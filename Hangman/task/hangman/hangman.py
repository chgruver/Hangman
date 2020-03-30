from random import choice

print("H A N G M A N")
word_choice = ["python", "java", "kotlin", "javascript"]
while True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == "play":
        secret_word = choice(word_choice)
        word_set = set(secret_word)
        hint = "-" * len(secret_word)
        temp = ""
        guess_set = set()
        lives = 8
        while lives > 0:
            print(f"\n{hint}")
            guess = input("Input a letter: ")
            if len(guess) == 1:
                if guess in word_set:
                    for char in range(len(secret_word)):
                        if guess == secret_word[char]:
                            temp += guess
                        elif hint[char] != "-":
                            temp += hint[char]
                        else:
                            temp += "-"
                    hint = temp
                    temp = ""
                    word_set.remove(guess)
                elif guess in guess_set:
                    print("You already typed this letter")
                elif guess not in "abcdefghijklmnopqrstuvwxyz":
                    print("It is not an ASCII lowercase letter")
                else:
                    print("No such letter in the word")
                    lives -= 1
                guess_set.add(guess)
                if hint == secret_word:
                    print("You guessed the word!\nYou survived!")
                    break
            else:
                print("You should print a single letter")
        else:
            print("You are hanged!")
    elif play == "exit":
        break
    else:
        continue
