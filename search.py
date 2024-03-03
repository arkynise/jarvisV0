import webbrowser
from text_to_sound import text_to_speech
from color import write_color

def create_URL(order):

    url = "https://google.com/search?q="
    length=len(order)
    for string in order:
        url=url+string
        length=length-1
        if length!=0:
            url=url+"+"
    return url
    



def search(order):
    url=create_URL(order)

    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/Edge.exe"

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get('edge').open(url)
    name=""
    for string in order:
        name=name+string+" "
    write_color("0,255,0")
    text_to_speech("the search result for "+name+" is displayed in edge")
    write_color("200,0,0")



