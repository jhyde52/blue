# Procedure, add_to_index, that takes 3 inputs:
# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already in the index, add the url
# to the list of urls associated with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
   for key, url_list in index:
   	if key == keyword:
   		if url not in url_list:
	   		url_list.append(url)
	   	return
   index.append([keyword,[url]])



add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


# Return tells the procedure to stop running and return the 
# contents of the return statement in this case nothing