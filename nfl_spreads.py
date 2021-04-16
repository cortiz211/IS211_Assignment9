


from bs4 import BeautifulSoup

html = "http://www.footballlocks.com/nfl_point_spreads.shtml"

def main():
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all('table', cols="4", width="580")
    spreads = tables[0].find_all("tr")

    header = True
    for spread in spreads:
       cells = spread.find_all("td")
       if header:
           header = False
           continue

       favorite = cells[1].text.replace("At ", "")
       underdog = cells[3].text.replace("At ", "")
       spread = float(cells[2].text)
       print(f"Favorite = {favorite}, Underdog = {underdog}, Spread = {spread}")

if __name__ == "__main__":
    main()

