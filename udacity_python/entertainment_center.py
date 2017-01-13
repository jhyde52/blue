import fresh_tomatoes
import media
#this media is my file called media.py
#the class is Movie
#we are calling the function init to create memory for the instance toy story inside the class movie
#the init method is similar to a constructor
hotel_rwanda = media.Movie("Hotel Rwanda", "The true story of one man and his courage in the midst of genocide.", "https://en.wikipedia.org/wiki/Hotel_Rwanda#/media/File:Hotel_Rwanda_movie.jpg", "https://www.youtube.com/watch?v=4dd8rX5Dy_Q")
#print hotel_rwanda.storyline
blue_is_warmest = media.Movie("Blue is the Warmest Color", "A French teen forms a deep emotional and sexual connection with an older art student she met in a lesbian bar.", "http://images-cdn.moviepilot.com/image/upload/c_fill,h_1231,w_1000/t_mp_quality/uploads_4e425ed3-6514-413d-a3e2-ad5914189094-blue-is-the-warmest-color-poster-hd-wallpaper-jpg-21415.jpg", "https://www.youtube.com/watch?v=Y2OLRrocn3s")
#print blue_is_warmest.storyline
#blue_is_warmest.show_trailer()
#the function open_movies_page takes a list or array so I need to make one:
back_to_the_future = media.Movie("Back to the Future","A teenager (Michael J. Foxx) time travels to the past and gets hit on by his mom.", "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg','https://www.youtube.com/watch?v=qvsgGtivCgs")
iron_man = media.Movie("Iron Man","A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), builds an armored suit and uses it to combat crime and terrorism.", "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG","https://www.youtube.com/watch?v=8OCJRbzdzaU")
movies = [hotel_rwanda, blue_is_warmest, back_to_the_future, iron_man]
fresh_tomatoes.open_movies_page(movies)

#i added movies the list as the ARGUMENT for the function open_movies
#instance method a function that is defined within a class and is associated with an instance is an instance method
#here I want to call the function (an instance method) I defined in the media file

#We defined a CLASS called Movie in the other file. This is like a blueprint. It can have data (title, storyline) and also methods (show trailer)
#here we defined INSTANCES of the class -blue is the warmest, hotel rwanda
#when we create an instance, the class's CONSTRUCTOR gets called (the init method inside the class, this initializes the data)
#constructor uses the keyword self-self is the instance in question ie hotel rwanda
#the variables like title, storyline are INSTANCE VARIABLES and can be accessed using the self keyword inside the class (self.title) and by the instance name outside the class (hotel_rwanda.title)
#functions inside the class associated with an instance are INSTANCE METHODS and have the first argument as self -these are init and show_trailer in this case

#make sure fresh_tomatoes is in the same folder with media and entertainment_center
