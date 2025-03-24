import csv
import requests
from bs4 import BeautifulSoup


with open("Sydney2021.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Nationality", "Birth Year"])

    names_tags = soup.select("div.profile-item-caption-content-line.profile-item-caption-content-name")
    link_tags = soup.select("div.profile-item-caption-content-line a")

    for name_tag, link_tag in zip(names_tags, link_tags):
        name = name_tag.text.strip()
        profile_link = link_tag.get("href")

        # Visit Individual Page
        response = requests.get(profile_link)
        detailed_soup = BeautifulSoup(response.text, "html.parser")

        # Initialize variables
        nationality = ""
        birth_year = ""

        # Loop through each background item safely
        for item in detailed_soup.select("div.entry-competitor-item-line"):
            label_tag = item.select_one("label")
            span_tag = item.select_one("span")

            if label_tag and span_tag:
                label = label_tag.text.strip()
                value = span_tag.text.strip()

                if label == "Nationality":
                    nationality = value
                elif label == "Date of Birth":
                    birth_year = value.split()[-1]  # Get just the year

        writer.writerow([name, nationality, birth_year])
        print(name, nationality, birth_year)

        
