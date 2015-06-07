import media;
_media = media.Media;

class Movie(_media):

	"""Movie class"""

	VALID_RATINGS = ["G","PG","PG-13","R"];

	def __init__(self, id, title, storyline, poster_image, trailer_youtube, imdbRating, rated, genre, stars, director, year, duration, type):
		_media.__init__(self, id, title, storyline, poster_image, trailer_youtube, imdbRating, genre, stars, year, duration, type);
		this          = self;
		this.rated    = self.validateRatings(rated);
		this.director = director;