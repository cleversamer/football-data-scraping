# import external modules
import openpyxl
import requests
from bs4 import BeautifulSoup

# create an Excel file
excel = openpyxl.Workbook()

# make sure that we are working on the active sheet
sheet = excel.active

# set the name of the sheet
sheet.title = "Football Database"

# requesting the IMDB website
url = "https://www.footballdatabase.eu/en/players"
source = requests.get(url)

# throws an error in case of the URL has issues
source.raise_for_status()

# read and parse HTML file
soup = BeautifulSoup(source.text, "html.parser")


# scrape the best worldwide scorers
def scrape_best_scorers():
    # read table rows
    rows = soup.find_all("div", class_="pbestscorers")[0].find_all("tr", class_="line")

    # write table head
    sheet.append(["Players", "Goals"])

    for row in rows:
        # read player child element
        player_name = row.find("td", class_="player").get_text(strip=True)

        # read score element
        player_score = row.find("td", class_="score").get_text(strip=True)

        # write a new row to the current table
        sheet.append([player_name, player_score])

    # write a break line in the sheet
    sheet.append(["", ""])


def scrape_best_passers():
    # read table rows
    rows = soup.find_all("div", class_="pbestscorers")[1].find_all("tr", class_="line")

    # write table head
    sheet.append(["Players", "Assists"])

    for row in rows:
        # read player child element
        player_name = row.find("td", class_="player").get_text(strip=True)

        # read score element
        player_score = row.find("td", class_="score").get_text(strip=True)

        # write a new row to the current table
        sheet.append([player_name, player_score])

    # write a break line in the sheet
    sheet.append(["", ""])


scrape_best_scorers()
scrape_best_passers()

# save Excel file
excel.save("Football Database.xlsx")
