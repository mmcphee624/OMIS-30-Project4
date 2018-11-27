from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from lxml import html


my_url = 'https://www.offleaseonly.com/used-cars.htm'

#open connection and grab page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing: open page with soup
page_soup = soup(page_html, "html.parser")

# print(page_soup.h2)

# test_1 = page_soup.h6
# print('heres the whole thing \n\n', page_soup.prettify())

# test_2 = page_soup.find_all('div', attrs= {'class' : 'vehicle-title-wrap'})
# print(test_2.contents)

# test_3 = page_soup.find_all('span', attrs= {'class' : 'pricing-ourprice'})
# print(test_3.contents)





# test_5= (page_soup.find_all(string=re.compile("Kia")))
# print(test_5)


#TEST!!!!