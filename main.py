import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # a form for crossing off movies
        crossoff_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross off
                <input type="text" name="crossed-off-movie"/>
                from my watchlist.
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """

        page_content = edit_header + add_form + crossoff_form
        content = page_header + page_content + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")
        if new_movie != (""):
            escaped_new_movie = cgi.escape(new_movie)
        # build response content
            new_movie_element = "<strong>" + new_movie + "</strong>"
            sentence = new_movie_element + " has been added to your Watchlist!"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
        else:
            returned_sentence = "Oops! You forgot to enter a movie..."
            content = page_header + "<p>" + returned_sentence + "</p>" + page_footer
            self.response.write(content)


class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross-off
    """

    def post(self):
        # look inside the request to figure out what the user typed
        #rejected_list = ["Star Wars", "Minions", "Freaky Friday", "My Favorite Martian"]
        crossed_off_movie = self.request.get("crossed-off-movie")
        rejected_movies = ["Star Wars", "Minions", "Freaky Friday", "My Favorite Martian"]

        if crossed_off_movie == rejected_movies:
            terrible_movie_element = "<strong>" + crossed_off_movie + "</strong>"
            terrible_movie_confirmation = "Trust me, you don't want to add" + terrible_movie_element + " to your Watchlist."
            terrible_movie_content = page_header + "<p>" + terrible_movie_confirmation + "</p>" + page_footer
            self.response.write(terrible_movie_content)
            # build response content
        else:
            crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
            confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
            content = page_header + "<p>" + confirmation + "</p>" + page_footer
            self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)
], debug=True)
