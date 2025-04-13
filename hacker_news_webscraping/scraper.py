import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")

#print(res.text)

# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(res.text) # to handle any unicode errors

soup = BeautifulSoup(res.text, "html.parser")

# grab the title and the link of the story that has more than 100 votes

links = soup.select(".titleline")

subtext = soup.select(".subline")


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        
        if len(vote):
            points_text = vote[0].getText().replace(" ","")
            
            # Remove the word "points" and convert to int
            points = int(points_text.replace("points", ""))
            if points > 99:
                hn.append({"title": title, "link":href, "votes": points})    

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))





