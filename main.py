import sys

import requests
from bs4 import BeautifulSoup


def printExamples(searchKey):
    print(searchKey, "\n")
    # example url of a real request
    # https://www.linguee.com/english-german/search?source=auto&query=hello
    url_root = "https://www.linguee.com/german-english/search?source=german&query="
    query = searchKey 

    res = requests.get(url_root + query)
    soup = BeautifulSoup(res.text, "html.parser")

    lemma_content = soup.find_all("div", class_="lemma_content")

    for lemma in lemma_content:
        examples = lemma.find("span", class_="tag_s")

        if examples is not None:
            print(examples.text)

    if len(lemma_content) == 0:
        examples = soup.find_all("a", class_="dictLink")

        for example in examples:
            if example['href'].startswith("/german-english/"):
                print(example.text)

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        
        printExamples(arg)
        print("--------------------------------------------")

