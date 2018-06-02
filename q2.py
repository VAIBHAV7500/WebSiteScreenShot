import selenium.webdriver as webdriver
import contextlib
import sys
from PIL import Image
print('Enter the website: ')
web= sys.stdin.readline()
print('Enter the width for resolution(width*height): ')
basewidth = int(sys.stdin.readline())
@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()
with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(10)
    driver.get(web)
    driver.get_screenshot_as_file('screenshot.png') 
    
    
img = Image.open('screenshot.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('screenshot.png') 
