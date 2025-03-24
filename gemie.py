import csv
import requests
from bs4 import BeautifulSoup

with open("Sydney2021.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Nationality", "Age"])

    url = "https://www.pianoplus.com.au/competition-2021/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    names_tags = soup.select("div.profile-item-caption-content-line.profile-item-caption-content-name")
    link_tags = soup.select("div.profile-item-caption-content-line a")

    for name_tag, link_tag in zip(names_tags, link_tags):
        name = name_tag.text.strip()
        profile_link = link_tag.get("href")  # full URL, no need for urljoin

        # Visit Individual Page
        response = requests.get(profile_link)
        if response.status_code != 200:
            print(f"Failed to fetch {profile_link} (status {response.status_code})")
            continue

        detailed_soup = BeautifulSoup(response.text, "html.parser")

        # Get Nationality and Birth Date
        info_tags = detailed_soup.select("span.entry-competitor-background-text")
        nationality = info_tags[0].text.strip() if len(info_tags) > 0 else ""
        birthdate = info_tags[1].text.strip() if len(info_tags) > 1 else ""

        # Calculate age
        try:
            birth_year = int(birthdate.split()[-1])
            age = 2021 - birth_year
        except:
            age = ""

        writer.writerow([name, nationality, age])
        print(name, nationality, age)



