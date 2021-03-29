from django.shortcuts import render, HttpResponse
import requests
# myprogram to take news
from bs4 import BeautifulSoup
import pyttsx3


engine = pyttsx3.init()
voices= engine.getProperty('voices')   #To check Voices
# print(voices[0].id)     //David
engine.setProperty('voice',voices[1].id)  #By default
def speak(something):
    engine.say(something)
    engine.runAndWait()























# Create your views here.

def index(request):
    url = "https://inshorts.com/en/read/national"

    #get html
    r = requests.get(url)
    htmlContent  = r.content

    # Parse the content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    newsClass = soup.find_all('div', itemprop="articleBody")
    newses = {
        "news0": str(newsClass[0]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news1": str(newsClass[1]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news2": str(newsClass[2]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news3": str(newsClass[3]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news4": str(newsClass[4]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news5": str(newsClass[5]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news6": str(newsClass[6]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news7": str(newsClass[7]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news8": str(newsClass[8]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news9": str(newsClass[9]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news10": str(newsClass[10]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news11": str(newsClass[11]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news12": str(newsClass[12]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news13": str(newsClass[13]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
        "news14": str(newsClass[14]).replace('<div itemprop="articleBody">',"").replace("</div>",""),
    }
    
    # print(newsClass[0])
    return render(request, 'index.html', newses)


def about(request):
    return render(request, 'about.html')
