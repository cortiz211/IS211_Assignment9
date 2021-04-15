#URL is https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/")
soup = BeautifulSoup(response.text, "html.parser")
tops = soup.find_all(class_="CellPlayerName--long", limit=20)

for top in tops:
    name = top.find("a").get_text()
    position = top.find("CellPlayerName-position").get_text()
    team = top.find("CellPlayerName-team").get_text()
    print(name, team, position)

if __name__ == "__main__":
    main()