import random as rd

words = [
    "umbrella",
    "computer",
    "elephant",
    "guitar",
    "bicycle",
    "dragon",
    "book",
    "moon",
    "pizza",
    "ocean",
    "fire",
    "mountain",
    "star",
    "camera",
    "robot"
]

word = rd.choice(words)
total_chances = 7
gussed_word = "-"*len(word)

while total_chances != 0:
    print(gussed_word)
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                gussed_word = gussed_word[:i]+letter+gussed_word[i+1:] 
                print(gussed_word)
            
        if gussed_word == word:
            print("Congrulations you won!!!")
            break

    else:
        total_chances -= 1
        print("Incorrect guesss")
        print("The remaining chances are: ", total_chances)

else:
    print("Game Over")
    print("You loose")
    print("All the chances are exhausted")
    print("the correct word is", word)

