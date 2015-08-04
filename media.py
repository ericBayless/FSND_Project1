import webbrowser

class Movie():
        """ This class provides a way to store movie related information.

        Attributes:
                VALID_RATINGS:  A list containging the valid ratings for a  movie.
                title:  The movie title
                storyline:  The movie description
                poster_image_url:  URL to the movie poster
                trailer_youtube_url:  URL to the youtube trailer
                runtime:  The movie runtime
                rating:  The movie rating.  Should be set using VALID_RATINGS.
        """

        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                              movie_runtime, movie_rating):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.runtime = movie_runtime
                self.rating = movie_rating

        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
