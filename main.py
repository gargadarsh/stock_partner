#main.py
from search_eng import stockSearch, printArticles

'''
if we do our own NLP implementation then im thinking we do a workflow like:
	- parse text into list of words 
		-corner cases: translating apostrophes, punctuations

	-assign weight values to punctuations and certain key words
		- maybe use neural network implementation??

	-get rid of words like "and", "or" maybe cuz they neutral

	-take avg of weights

	-Problems: there's no way we can assign weights to every key word cuz there are 
				way too many words that can factor in so idk


'''


def NLP():
	pass


def parser(str):
	pass



def main(stock):
	articles = []
	text = []

	articles = stockSearch(stock)
	#---- extract words from each article and place in list----#

	#----- apply NLP or sum -----#


	#----- average NLP responses ----#
	




main()