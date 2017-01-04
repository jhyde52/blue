import fresh_tomatoes
import media
#this media is my file called media.py
#the class is Movie
#we are calling the function init to create memory for the instance toy story inside the class movie
#the init method is similar to a constructor
hotel_rwanda = media.Movie("Hotel Rwanda", "The true story of one man and his courage in the midst of genocide.", "http://ecx.images-amazon.com/images/I/51Li0IdYVaL._SX940_.jpg", "https://www.youtube.com/watch?v=4dd8rX5Dy_Q")
#print hotel_rwanda.storyline
blue_is_warmest = media.Movie("Blue is the Warmest Color", "A French teen forms a deep emotional and sexual connection with an older art student she met in a lesbian bar.", "http://images-cdn.moviepilot.com/image/upload/c_fill,h_1231,w_1000/t_mp_quality/uploads_4e425ed3-6514-413d-a3e2-ad5914189094-blue-is-the-warmest-color-poster-hd-wallpaper-jpg-21415.jpg", "https://www.youtube.com/watch?v=Y2OLRrocn3s")
#print blue_is_warmest.storyline
#blue_is_warmest.show_trailer()
#the function open_movies_page takes a list or array so I need to make one:
those_who_tell = media.Movie("For Those Who Can Tell No Tales","An Australian tourist discovers the silent legacy of wartime atrocities when she arrives in a seemingly idyllic little town on the border of Bosnia and Serbia.", "http://pics.filmaffinity.com/For_Those_Who_Can_Tell_No_Tales-489411730-large.jpg","https://www.youtube.com/watch?v=DmTnWUeowPc")
gimme_the_loot = media.Movie("Gimme The Loot","When their latest work is buffed by a rival crew, two determined graffiti writers embark on an elaborate plan to bomb the ultimate location: the New York Mets' Home Run Apple.", "http://ia.media-imdb.com/images/M/MV5BNTMyNTY1NTQ2OF5BMl5BanBnXkFtZTcwOTU3ODQxOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=FyBGkojSUvE")
movies = [hotel_rwanda, blue_is_warmest, those_who_tell,gimme_the_loot]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

#i added movies the list as the ARGUMENT for the function open_movies
#instance method a function that is defined within a class and is associated with an instance is an instance method
#here I want to call the function (an instance method) I defined in the media file

#Definitions:
#We defined a CLASS called Movie in the other file. This is like a blueprint. It can have data (title, storyline) and also methods (show trailer)
#here we defined INSTANCES of the class -blue is the warmest, hotel rwanda
#when we create an instance, the class's CONSTRUCTOR gets called (the init method inside the class, this initializes the data)
#constructor uses the keyword self-self is the instance in question ie hotel rwanda
#the variables like title, storyline are INSTANCE VARIABLES and can be accessed using the self keyword inside the class (self.title) and by the instance name outside the class (hotel_rwanda.title)
#functions inside the class associated with an instance are INSTANCE METHODS and have the first argument as self -these are init and show_trailer in this case
#CLASS VARIABLES sometimes we want to use a variable for all the instances like movie ratings
#In python, all classes come with some pre-existing variables
#module, classname, pre-existing variable, doc
#import turtle
#turtle.Turtle.__doc__
#---that prints out the documentation that we put in the media.py file with triple quotes (triple quotes all it to be multiple lines)

#make sure fresh_tomatoes is in the same folder with media and entertainment_center

