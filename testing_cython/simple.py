
def main():
    import requests
    import lxml.html
    import pandas
    import sklearn
    import scipy
    import numpy
    import nltk
    
    html = lxml.html.fromstring(requests.get("https://www.google.com").text)
    return html.xpath("//a/@href")
