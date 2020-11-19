#search engine using google API
from googlesearch import search



def stockSearch(stock, queryNum=30):
	stock = stock + " price"

	results = []
	articles = ["barrons", "cnn", "wsj", "cnbc", "yahoo", "businessinsider",
					"fox", "nytimes", "newyorktimes", "nyse", "reuters", "investing", 
					"marketwatch", "forbes"]


	for res in search(stock, tld="co.in", lang="en", num=queryNum, stop=queryNum, pause=2.0):
		results.append(res)

	filtered = []
	for name in articles:
		for index in range(len(results)):
			if name in results[index]:
				filtered.append(results[index])
	
	return filtered



def printArticles(li):
	for i in li:
		print((i+1) + ": " + li[i])

