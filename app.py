import movie;
import serie;
import fresh_tomatoes;
import getMovies;


#get index template
ft          = fresh_tomatoes;

#get movies and series data
data_path   = "data/media.json"
#load json
data        = getMovies.load(data_path,'true')
#movies list
movies_data = data["movies"]
#series list
series_data = data["series"]

#empty list for movies instances
movies      = [];
#empty list for series instances
series 		= [];

#youtube API access data
youtube_api_public_key = "&key=AIzaSyDERiZWjj-YehoyrRPBHdM5CqKCMA7dcv8"
youtube_api_url        = "https://www.googleapis.com/youtube/v3/search?part=id"

#run movies list and create instances of movie class
for index, movie_item in enumerate(movies_data):
	movies.append(
		movie.Movie(
			index,
			movie_item["Title"], 
			movie_item["Plot"], 
			movie_item["Poster"], 
			#find movie trailer with youtube API
			getMovies.load(youtube_api_url + "&q=" + movie_item["Title"] + " trailer" + youtube_api_public_key,'false')['items'][0]['id']['videoId'],
			movie_item["imdbRating"],
			movie_item["Rated"],
			movie_item["Genre"],
			movie_item["Actors"],
			movie_item["Director"],
			movie_item["Year"],
			movie_item["Runtime"],
			movie_item["Type"],
		)
	)

#run movies list and create instances of series class
for index, serie_item in enumerate(series_data):
	series.append(
		serie.Serie(
			index,
			serie_item["Title"], 
			serie_item["Plot"], 
			serie_item["Poster"], 
			#find movie trailer with youtube API
			getMovies.load(youtube_api_url + "&q=" + serie_item["Title"] + " trailer" + youtube_api_public_key,'false')['items'][0]['id']['videoId'],
			serie_item["imdbRating"],
			serie_item["Rated"],
			serie_item["Genre"],
			serie_item["Actors"],
			str(serie_item["Year"].encode('utf8')),
			serie_item["Runtime"],
			serie_item["Type"],
			serie_item["Seasons"],
		)
	)

#build template
ft.open_movies_page(movies, series);