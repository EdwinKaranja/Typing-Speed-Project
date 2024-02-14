
import random
import time


with open("scratch.txt") as file:
    data = file.read()
data = data.split("\n")

quote = (data[random.randint(0, (len(data)-1))])
while quote == '':
    quote = (data[random.randint(0, (len(data)-1))])



quote_word_list = quote.split()
quote_length = len(quote.split())


def score_card():
    start = input("Please select Y to start the game. \n")
    if start.lower() == 'y':
        print(quote)
        start_time = time.time()
        result = input("You can now Start, the clock is ticking. \n")

        result_word_list = result.split()
        end_time = time.time()
        similar_words = []
        for i in result_word_list:
            if i in quote_word_list:
                similar_words.append(i)

        similarity_index = len(similar_words)/quote_length
        minutes_taken = (end_time - start_time)/60
        typing_speed = len(similar_words)/minutes_taken

        print(f"Your typing speed is {round(typing_speed*similarity_index, 2)} words per minute.")


score_card()