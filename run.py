import scrapper

raw_movies_info = scrapper.get_movies_info_raw()

"""
soup = BeautifulSoup(raw_movies_info, 'html')
for link in soup.find_all('a'):
    print(link.get('href'))
#print(soup)
"""