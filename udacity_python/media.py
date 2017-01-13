import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image = poster_image
		self.trailer_youtube_url = trailer_youtube
#new function/method we call show_trailer, takes the first argument of self
#we use a preexisting function webbrowser open and that just needs a url which is stored in our variable self.trailer_youtube_url
	def	show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
#once I get these 4 pieces of info I can initialize these 4 variables
#init always takes SELF which is the object being created ie hotel rwanda