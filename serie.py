import media;
_media = media.Media;

class Serie(_media):

	"""Serie class"""

	VALID_RATINGS = ["TV-Y","TV-Y7","TV-G","TV-PG", "TV-14", "TV-MA"];

	def __init__(self, id, title, storyline, poster_image, trailer_youtube, imdbRating, rated, genre, stars, year, duration, type, seasons):
		_media.__init__(self, id, title, storyline, poster_image, trailer_youtube, imdbRating, genre, stars, year, duration, type);
		this             = self;
		this.rated       = self.validateRatings(rated);
		this.seasonsNumb = seasons;