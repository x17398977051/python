import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    movie_list = []

    for i in range(0, 10):
        link = f'https://movie.douban.com/top250?start={str(i * 25)}'
        r = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        titles = soup.find_all('div', class_="hd")
        for each in titles:
            movie = each.span.text.strip()
            movie_list.append(movie)


    return movie_list

movies = get_movies()
print(movies)

