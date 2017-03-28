import webapp2


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

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.
       remove_form = """
       <form action="/remove" method="post">
           <label>
               I want to remove
               <input type="text" name="removed-movie"/>
               to my watchlist.
           </label>
           <input type="submit" value="Remove It"/>
       </form>
       """

        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)


       content = page_header + edit_header + add_form + remove_form + page_footer
       self.response.write(content)


class AddMovie(webapp2.RequestHandler):
   """ Handles requests coming in to '/add'
       e.g. www.flicklist.com/add
   """

   def post(self):
        # look inside the request to figure out what the user typed
       new_movie = self.request.get("new-movie")

        # build response content
       new_movie_element = "<strong>" + new_movie + "</strong>"
       new_movie_sentence = new_movie_element + " has been added to your Watchlist!"

       content = page_header + "<p>" + new_movie_sentence + "</p>" + page_footer
       self.response.write(content)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
   """ Handles requests coming in to '/remove'
       e.g. www.flicklist.com/remove
   """

   def post(self):
       removed_movie = self.request.get("removed-movie")

       removed_movie_element = "<strong>" + removed_movie + "</strong>"
       removed_movie_sentence = removed_movie_element + " has been removed from your Watchlist!"

       content2 = page_header + "<p>" + removed_movie_sentence + "</p>" + page_footer
       self.response.write(content2)

# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/remove', CrossOffMovie)
], debug=True)
