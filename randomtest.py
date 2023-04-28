import requests
from requests_html import HTMLSession




'''
Scratch for getting topmost color for each column
/html/body/div[2]/table/tbody/tr[1]/td[3] #Top row column 3
/html/body/div[2]/table/tbody/tr[2]/td[3] # Second from top column 3
/html/body/div[2]/table/tbody/tr[1]/td[4] # Top row Column 4
'''
class sugandese:
    def __init__(self):
        self.curBoard = []
        self.lastBoard = []

    
def getRecentMove(response):
    #response = requests.get('http://127.0.0.1:5000/p2Join')
    print(response.text)
    print(response.status_code)
    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            return response.json()
        except ValueError:
            # decide how to handle a server that's misbehaving to this extent
            return 
    return

session = HTMLSession()

r = session.get('http://127.0.0.1:5000/p2Join')

r.html.render()  # this call executes the js in the page
print(r.html)
#getRecentMove(x)