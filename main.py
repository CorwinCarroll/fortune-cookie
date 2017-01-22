#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
	fortunes = [
	"Train yourself to let go of everything you fear to lose",
	"Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
	"Always pass on what you have learned.",
	"You must unlearn what you have learned.",
	"Many of the truths that we cling to depend on our point of view.",
	"Do or do not. There is no try."
	]

	return(random.choice(fortunes))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	header = "<h1>Fortunes From Cookies</h1>"

    	fortune = "<strong>" + getRandomFortune() + "</strong>"
    	fortune_paragraph = "<p>Your fortune: " + fortune + " </p>"

    	lucky_number = "<strong>" + str(random.randint(1, 9999)) + "</strong>"
    	number_paragraph = "<p>Your lucky number: " + lucky_number  + " </p>"

    	more_cookies_button = "<p><a href='.'><button>More Cookie Knowledge!</button></a></p>"

    	content = header + fortune_paragraph + number_paragraph + more_cookies_button


        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


        # movie = self.getRandomMovie()

        # # build the response string
        # content = "<h1>Movie of the Day</h1>"
        # content += "<p>" + movie + "</p>"

        # # TODO: pick a different random movie, and display it under
        # # the heading "<h1>Tommorrow's Movie</h1>"

        # self.response.write(content)