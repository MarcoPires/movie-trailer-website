import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Movie Trailer Website</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link href="css/flat-ui.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -14px;
            right: -10px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            $('.movie-tile').show();
          });
        });

        // show/hide movie-title more details
        $(document).on('mouseenter', '.movie-tile', function (event) {
          $(this).find(".popover").addClass("show");
        });
        $(document).on('mouseleave ', '.movie-tile', function (event) {
          $(this).find(".popover").removeClass("show");
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <span class="fui-cross-circle"></span>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Static navbar -->
    <div class="navbar navbar-inverse navbar-static-top" role="navigation">
      <div class="container">
        <div class="navbar-header">

          <a class="navbar-brand" href="#">Trailer Website <span class="fui-youtube"></span> </a>

        </div>
        <ul class="nav navbar-nav navbar-left">
          <li class="active"><a href="#moviesTab" aria-controls="moviesTab" role="tab" data-toggle="tab">Movies</a></li>

          <li><a href="#seriesTab" aria-controls="moviesTab" role="tab" data-toggle="tab">Tv Shows</a></li>
        </ul>

        </div>
        </div>

    <!-- Main -->
    <div class="container thumbs-wrapper">
        <div class="row tab-content">

          <div role="tabpanel" class="tab-pane active" id="moviesTab">
            {movie_tiles}
          </div>
          <div role="tabpanel" class="tab-pane" id="seriesTab">
            {serie_tiles}
          </div>
        
        </div>
    </div>

  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-sm-6 col-md-4 col-sm-4 movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" >
  <!-- cover and main info -->
  <div class="thumbnail">
    <div class="poster">
      <img src="{poster_image_url}" alt="...">
      <span class="movie_ranking"><span class="text">Imdb ranking</span><span class="label label-default">{movie_ranking}</span></span>
    </div>
    
    
    <div class="caption">
      <h5>{movie_title}</h5>
      <p>{movie_storyline}</p>
    </div>
  </div>

  <!-- more details -->
  <div class="popover {popover_position}" role="tooltip">
    <div class="arrows"></div>
    <h3 class="popover-title">More details</h3>
    <div class="popover-content">
      
      <ul>

        <li>
          <div class="todo-icon fui-calendar-solid"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Year
            </h4>
            {year}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-user"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Director
            </h4>
            {director}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-star-2"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Stars
            </h4>
            {stars}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-clip"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Genre
            </h4>
            {genre}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-time"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Duration
            </h4>
            {duration}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-tag"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Rated
            </h4>
            {rated}
          </div>
        </li>

      </ul>

    </div>
  </div>
</div>
'''

# A single movie entry html template
serie_tile_content = '''
<div class="col-sm-6 col-md-4 col-sm-4 movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" >
  <!-- cover and main info -->
  <div class="thumbnail">
    <div class="poster">
      <img src="{poster_image_url}" alt="...">
      <span class="movie_ranking"><span class="text">Imdb ranking</span><span class="label label-default">{movie_ranking}</span></span>
    </div>
    
    
    <div class="caption">
      <h5>{movie_title}</h5>
      <p>{movie_storyline}</p>
    </div>
  </div>

  <!-- more details -->
  <div class="popover {popover_position}" role="tooltip">
    <div class="arrows"></div>
    <h3 class="popover-title">More details</h3>
    <div class="popover-content">
      
      <ul>

        <li>
          <div class="todo-icon fui-calendar-solid"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Year
            </h4>
            {year}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-star-2"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Stars
            </h4>
            {stars}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-clip"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Genre
            </h4>
            {genre}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-time"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Duration
            </h4>
            {duration} per episode
          </div>
        </li>
        <li>
          <div class="todo-icon fui-tag"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Rated
            </h4>
            {rated}
          </div>
        </li>
        <li>
          <div class="todo-icon fui-folder"></div>
          <div class="todo-content">
            <h4 class="todo-name">
              Seasons
            </h4>
            {seasons}
          </div>
        </li>

      </ul>

    </div>
  </div>
</div>
'''

def create_movie_tiles_content(videos):
    # The HTML content for this section of the page
    content         = ''
    #thums number per line
    index           = 0
    #popover position relative to .movie-title
    popoverPosition = 'left'

    for video in videos:
  
      #if third thumb, the popover goes right
      index = index + 1
      if index > 2:
        popoverPosition = 'right'

      # Append the tile for the movie with its content filled in
      if video.type == "movie":
        
        # template for movies
        content += movie_tile_content.format(
            movie_id           = video.id,
            movie_title        = video.title,
            movie_storyline    = video.storyline,
            poster_image_url   = video.poster_image_url,
            trailer_youtube_id = video.trailer_youtube_id,
            movie_ranking      = video.imdbRating,
            rated              = video.rated,
            genre              = video.genre,
            stars              = video.stars.replace(",","<br/>"),
            director           = video.director,
            year               = video.year,
            duration           = video.duration,
            popover_position   = popoverPosition
        )
      else:
        # template for sereis
        content += serie_tile_content.format(
            movie_id           = video.id,
            movie_title        = video.title,
            movie_storyline    = video.storyline,
            poster_image_url   = video.poster_image_url,
            trailer_youtube_id = video.trailer_youtube_id,
            movie_ranking      = video.imdbRating,
            rated              = video.rated,
            genre              = video.genre,
            stars              = video.stars.replace(",","<br/>"),
            year               = video.year,
            duration           = video.duration,
            seasons            = video.seasonsNumb,
            popover_position   = popoverPosition
        )
      
      # Add the extra clearfix for only the required viewpor
      
      if index > 2:
        content += '<div class="clearfix visible-xs-block"></div>'
        index = 0
        popoverPosition = 'left'

    return content

def open_movies_page(movies,series):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(
      movie_tiles=create_movie_tiles_content(movies),
      serie_tiles=create_movie_tiles_content(series)
    )

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  if __name__ == "__main__":
    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible