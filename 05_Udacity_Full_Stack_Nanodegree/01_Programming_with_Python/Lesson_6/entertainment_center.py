import fresh_tomatoes
import movie_website

toy_story = movie_website.Movie("Toy Story",
                                "A story of a boy and his toys that come to life",
                                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = movie_website.Movie("Avatar",
                             "A marine on an alien planet",
                             "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                             "http://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)

#avatar.show_trailer()

school_of_rock = movie_website.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = movie_website.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = movie_website.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = movie_website.Movie("Hunger Games", "A really real reality show",
                                   "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                                   "https://www.youtube.com/watch?v=p-5ANq4sAL0")

movies = [toy_story,avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#To view movie website (remove hashtags from next two lines)
#fresh_tomatoes.open_movies_page(movies)
#print(movie_website.Movie.VALID_RATINGS)                                  

# Python predefined class variables
print (movie_website.Movie.__doc__)
print(movie_website.Movie.__name__)
print(movie_website.Movie.__module__)
