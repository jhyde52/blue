# A procedure, add_page_to_index, that takes three inputs:
#   - index
#   - url (String)
#   - content (String)
# It should update the index to include all of the word occurences found in the
# page content by adding the url to the word's associated url list.
import re

index = []
word_urls=[]
words=[]

def clean_str(string):
	string = re.sub(r'<.*?>', ' ', string)
	string = re.sub(r'[^\s@]+@[^\s\.@]+\.[^\s@]+', '#EMAIL#', string)
	string = re.sub(r'(http[s]?://|www\.){1,2}[^\s]+', '#URL#', string)
	string = re.sub(r'[^a-z\-#]', ' ', string.lower())
	string = re.sub(r'\s+[#\-]*\s+', ' ', string)
	return string


def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])


def add_page_to_index(index,url,content):
	clean_content=clean_str(content)
	words=clean_content.split()
	for word in words:
		add_to_index(index,word,url)
	



add_page_to_index(index,'fake.text',"This is not, (a) test")
add_page_to_index(index,'real.text', 'This is not a test')
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
