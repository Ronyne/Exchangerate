import requests
#import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?access_key=e408c0beedeb543b4d5e884adaa5b488"

payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
params = {}
params = response.json()

#print(params)
ratelist = params["rates"]

#print (ratelist)
html = """<!doctyple html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Rates</title>
    </head>
    <body>
        <table border="1" bordercolor="lightgray" style="width:50%">
            <tr style="background-color: lightgray; height: 25px" >
                <td border-color: lightgray style="width:40%">
                    Currency
                </td>
                <td>
                    Excahnge rate (Base EUR)
                </td>
            </tr>"""

for key,rate in ratelist.items():
    html += f"""<tr style=\"height: 23px;\">
                 <td>
                    {key}
                </td>
                <td>
                    {rate}
                </td>
               </tr>
             """

html+="""</table></body></html>"""
#print(html)

f = open("index.html", "w")
f.write(html)
f.close()