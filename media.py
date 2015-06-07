class Media():

	""" Super class for movie and serie """

	def __init__(self, id, title, storyline, poster_image, trailer_youtube, imdbRating, genre, stars, year, duration, type):
		this                    = self;
		this.id                 = id;
		this.title              = title;
		this.duration           = duration;
		this.storyline          = storyline;
		this.poster_image_url   = poster_image;
		this.trailer_youtube_id = trailer_youtube;
		this.imdbRating         = imdbRating;
		this.genre              = genre;
		this.stars              = stars;
		this.year               = year;
		this.type               = type;
		this.viewed             = False;		

	def toggle_viewed(self):
		self.viewed = not self.viewed;


	def validateRatings(self, rated):
		ratingsList = self.VALID_RATINGS;

		for index, rating in enumerate(ratingsList):
			if rating == rated:
				return rating

		return "N/A"