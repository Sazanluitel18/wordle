import random
import sys


def main():
    # Get a random word.
    answer = getRandomWord()
    print(answer)

    # PUT YOUR CODE HERE.
    user_answer = ""
    count = 0
    while user_answer != answer:
        if count == 5:
            print(f"Sorry! You choosed wrong word!The correct one was : {answer}")
            break

        user_answer = str(input("Enter a 5 letter guess?: "))
        if len(user_answer) != 5:
            print("Please enter only 5 letter words")
            continue
        printGuessColors(user_answer, answer)
        count += 1
    else:
        print(f"You guessed correct word! You took {count} attempt!")

    # Start by asking the user for their initial guess
    # Ask them to "Enter a 5 letter guess?"
    # Start with section 3 in the starter doc.


# A helper method that prints the guess with the
# correct colors to the console.
# Example usage:
# printGuessColors("broke", "broke") should print the five lines:
#
# b - Green
# r - Green
# o - Green
# k - Green
# e - Green
def printGuessColors(guess, answer):
    for index in range(len(guess)):
        color = letterColor(index, guess, answer)
        print(f"{guess[index]} - {color}")


# A helper method that determines the color
# of the letter in the guess. This function
# should return "Green", "Red", or "Yellow"
def letterColor(index, guess, answer):
    guess = guess.upper()
    answer = answer.upper()
    if guess[index] == answer[index]:
        return "\033[32mGreen\033[0m"
    elif guess[index] in answer:
        return "\033[33mYellow\033[0m"
    elif guess[index] != answer[index]:
        return "\033[31mRed\033[0m"


# A method that gets a random word from a file.
# You should not change this function.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
