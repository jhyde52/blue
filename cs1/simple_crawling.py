# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com/hello">')

#finds 89, the number of characters from the beginning of the string (indexed from 0)
start_link = page.find('<a href=')
print start_link

#find the first character after start link but it is a quote so we add one to get the first real character
start_quote = page.find('"', start_link)+1
print start_quote

#find the next quote after the position we found in start_quote
end_link = page.find('"', start_quote)
print end_link

url = page[start_quote:end_link]
print url		
