# This is a sample Python script.
import urllib.request

from bs4 import BeautifulSoup

response=urllib.request.urlopen("http://www.baidu.com/s?wd=java")
result = response.read().decode('utf-8')
soup = BeautifulSoup(result, "html.parser")
print(soup.prettify())

# This is a sample Python script.

# from PIL import Image
# import pytesseract

# text = pytesseract.image_to_string(Image.open('1.png'), lang='chi_sim')
# print(text);
