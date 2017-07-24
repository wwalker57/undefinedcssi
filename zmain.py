# imports
import logging
import os
import jinja2
import json
import urllib2
import urllib
import webapp2

# load jinja2 environment
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
    os.path.dirname(__file__) + '/templates'))

# main class
class MainPage(webapp2.RequestHandler):
    def get(self):
        # saves q as search term
        search_term = self.request.get('q')

        # saves main.html as template for this class
        template = env.get_template('main.html')
        my_vars = { 'q': search_term }
        self.response.out.write(template.render(my_vars))

# handlers
app = webapp2.WSGIApplication([
    ('/', MainPage)
])
