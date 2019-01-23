from selenium import webdriver

# Starting a Selenium "webdriver" to pop up a real Firefox browser window
browser = webdriver.Firefox()
# Using it to open up a web page which we’re expecting to be served from the local PC
browser.get('http://localhost:8000')

# Checking (making a test assertion) that the page has the word "Django" in its title
assert 'Django' in browser.title

