"""
File: webcrawler.py
Name: Yu-Hsien (Jason) Wu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all("tbody")
        for tag in tags:
            text_str = tag.text
            # print(text_str)
            text_list = text_str.split("\n")
            # print(text_list)
            male_num = 0
            female_num = 0
            for i in range(2, len(text_list) - 5, 2):
                # print(text_list[i])
                name_num_list = text_list[i].split()
                # print(name_num_list)

                male_num_str = ""
                for ch in name_num_list[1]:
                    if ch != ",":
                        male_num_str += ch
                male_num += int(male_num_str)

                female_num_str = ""
                for ch in name_num_list[3]:
                    if ch != ",":
                        female_num_str += ch
                female_num += int(female_num_str)

            print("Male Number: " + str(male_num))
            print("Female Number: " + str(female_num))


if __name__ == '__main__':
    main()
