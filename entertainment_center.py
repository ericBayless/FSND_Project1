import fresh_tomatoes
import media

# instantiate movie objects
hero = media.Movie("Hero",
		 "A defense officer, Nameless, was summoned by the King of Qin regarding his success of terminating three warriors.",
		 "http://ia.media-imdb.com/images/M/MV5BMTk5NjQyMzIwM15BMl5BanBnXkFtZTcwODQyNjYyMQ@@._V1_SX640_SY720_.jpg",
		 "http://www.youtube.com/watch?v=afCgVKLB-28")

drunken_master = media.Movie("The Legend of Drunken Master",
			     "A young martial artist is caught between respecting his pacifist father's wishes or stopping a group of disrespectful foreigners from stealing precious artifacts.",
			     "http://ecx.images-amazon.com/images/I/51tif%2BP-fRL.jpg",
			     "http://www.youtube.com/watch?v=Ep8K1Scl4MY")

kill_bill = media.Movie("Kill Bill",
		      "The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
		      "http://ia.media-imdb.com/images/M/MV5BMTU1NDg1Mzg4M15BMl5BanBnXkFtZTYwMDExOTc3._V1_SX640_SY720_.jpg",
		      "http://www.youtube.com/watch?v=ot6C1ZKyiME")

little_miss_sunshine = media.Movie("Little Miss Sunshine",
                                                                   "A family determined to get their young daughter into the finals of a beauty pageant take a cross-country trip in their VW bus.",
                                                                   "http://ia.media-imdb.com/images/M/MV5BMTgzNTgzODU0NV5BMl5BanBnXkFtZTcwMjEyMjMzMQ@@._V1_SX640_SY720_.jpg",
                                                                    "http://www.youtube.com/watch?v=S_hdphne0Xs")

goonies = media.Movie("The Goonies",
                                            "In order to save their home from foreclosure, a group of misfits set out to find a pirate's ancient treasure.",
                                            "http://ia.media-imdb.com/images/M/MV5BMTY1Mzk3MTg0M15BMl5BanBnXkFtZTcwOTQzODYyMQ@@._V1_SX640_SY720_.jpg",
                                            "www.youtube.com/watch?v=dfRacCoDD0k")

ip_man = media.Movie("Ip Man",
                                           "A semi-biographical account of Yip Man, the successful martial arts master who taught the Chinese martial art of Wing Chun to the world.",
                                           "http://ia.media-imdb.com/images/M/MV5BMjE0NDUzMDcyOF5BMl5BanBnXkFtZTcwNzAxMTA2Mw@@._V1_SX640_SY720_.jpg",
                                           "www.youtube.com/watch?v=1AJxXQ7xojE")

# create and open html page
movies = [hero,drunken_master, kill_bill, little_miss_sunshine, goonies, ip_man]
fresh_tomatoes.open_movies_page(movies)
