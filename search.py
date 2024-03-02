import webbrowser

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

    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get('edge').open(url)

