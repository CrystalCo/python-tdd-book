from selenium import webdriver

        ## Starting a Selenium "webdriver" to pop up a real Firefox browser window
# browser = webdriver.Firefox()
        ## Using it to open up a web page which we’re expecting to be served from the local PC
# browser.get('http://localhost:8000')

        ## Checking (making a test assertion) that the page has the word "Django" in its title
# assert 'Django' in browser.title

browser = webdriver.Firefox()

# User checks out homepage
self.browser.get('http://localhost:8000')

# User notices title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box 

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
