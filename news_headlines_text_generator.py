# News Headlines Text Generator

# Lauren Gray
# 7/23/2019

# Instructions:
# Execute in command line by running the following:
# `python news_headlines_text_generator.py ["seed text"] [number of words to generate]`
	# Example: `python news_headlines_text_generator.py "Donald Trump" 4`


# Imports
from pickle import load
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model


def get_seed_text():
    """
    Asks user for seed text from which to generate a news headline.

    Returns:
        seed_text - seed text to be used as model input
        next_words_int - the number of words in the sequence the model will generate
    """
    print('Hello! Let\'s generate a news headline!')
    # TO DO: get user inxput for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    seed_text = input('Please specify the seed text (e.g., Donald Trump).\n').title()

    while True:  
	    next_words_str = input('Please specify the number of words to generate following your seed text (e.g., 4).\n')
	    try:
	    	next_words_int = int(next_words_str)
	    	break
	    except ValueError:
	    	print("Oops! {} is not a valid answer. Please type an integer value.\n".format(next_words_str))

 
    return seed_text, next_words_int


def generate_text(seed_text, next_words):
	"""
	This function takes seed text and number of subsequent words (based on user input) as input. 
	It then cleans, tokenizes, and pads the seed text, when is then used as model input to make predictions. 
	Predicted tokens are matched with the corresponding word in the word dictionary, and those words are
	appended to the seed text in chronological order, forming a news headline. 

    Returns:
        seed_text.title() - the generated news headline
    """

	model = load_model('model_1.hdf5')
	max_sequence_len = 28

	# Tokenize the input string
	with open("tokenizer.pkl", "rb") as f:
		tokenizer = load(f)

	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([seed_text])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
		predicted = model.predict_classes(token_list, verbose=0)

		output_word = ""
		for word,index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		seed_text += " " + output_word

	return seed_text.title()


def main():
    while True:
    	seed_text, num_words = get_seed_text()
    	print(generate_text(seed_text, num_words))

    	restart = input('\nWould you like to restart? Enter yes or no.\n')
    	if restart.lower() == 'yes':
    		continue
    	if restart.lower() == 'no':
    		break


if __name__ == "__main__":
    main()