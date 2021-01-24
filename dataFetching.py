import requests
import re
from bs4 import BeautifulSoup


class DataFetching:
    def __init__(self):
        self.request = None
        self.src = None
        self.soup = None
        self.fighter_data = None

    def fetch_fighter_stats(self, url_link):
        self.request = requests.get(url_link)
        self.src = self.request.content
        self.soup = BeautifulSoup(self.src, 'lxml')

        """ Get the fighter's data"""
        search = self.soup.find_all("li")
        name_tag = self.soup.find_all("span", class_="b-content__title-highlight")
        name_parsed = str(name_tag)
        data = str(search)
        regex = re.compile("Orthodox|Southpaw|Switch|[A-Z][a-z]+ \d+, \d+|\d+.+")
        regex2 = re.compile("[A-Z][a-z]+ [A-Z][a-z]+")
        matches2 = regex2.finditer(name_parsed)
        matches = regex.finditer(data)
        fighter_name = [i.group() for i in matches2]
        stats = [i.group(0) for i in matches]
        fighter_data = {
            "Name": fighter_name[0],
            "Height": stats[0],
            "Weight": stats[1],
            "Reach": stats[2],
            "Stance": stats[3],
            "DOB": stats[4],
            "SLpM": stats[5],
            "Str. Acc.": stats[6],
            "SApM": stats[7],
            "Str. Def.": stats[8],
            "TD Avg.": stats[9],
            "TD Acc.": stats[10],
            "TD Def.": stats[11],
            "Sub. Avg.": stats[12]
        }
        self.fighter_data = fighter_data

    def get_fighter_data(self):
        return self.fighter_data

