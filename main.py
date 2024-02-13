#TODO: 1. Finding a block of text
#TODO: 2. Getting rules for score (Accuracy and speed)


import requests
import random
import time

parameters =  {'X-RapidAPI-Key': 'f4461d01e7msheb8c8b5b8e1783ep18e571jsnd397eb155791'}

block = requests.get(url = "webknox-jokes.p.rapidapi.com", params = parameters)


quote = "A green hoarde jumped over the fence to everyone's amazement."
result = "A gereen hoad ujumped over the fence to everyone's amansxwe"

start_time = time.time()
#Ways to compare include index by index score, similarity score, word accuracy,

quote_word_list = quote.split()

quote_length = len(quote.split())
print(quote_length)
result_word_list = result.split()



def score_card():
    #Check how many of the words in the result are in the original file.
    #Accuracy score should be used to adjust for score.
    similar_words = []
    for i in result_word_list:
        if i in quote_word_list:
            similar_words.extend(i)

    similarity_index = len(similar_words)/quote_length
    return similarity_index

you = score_card()


test = input("Let us see how much you wait!")
print(f"You took {time.time() - start_time} seconds")