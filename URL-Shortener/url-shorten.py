import pyshorteners
long_url = 'https://www.askpython.com/python/examples/url-shortener'
type_tiny = pyshorteners.Shortener()
print(type_tiny.available_shorteners)
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url)