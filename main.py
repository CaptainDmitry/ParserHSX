import json
import csv
import requests
from bs4 import BeautifulSoup

result_data = []

request = requests.get("https://www.hsx.vn/Modules/Rsde/Report/QuoteReport?pageFieldName1=Date&pageFieldValue1=17.03.2022&pageFieldOperator1=eq&pageFieldName2=KeyWord&pageFieldValue2=&pageFieldOperator2=&pageFieldName3=IndexType&pageFieldValue3=0&pageFieldOperator3=&pageCriteriaLength=3&_search=false&nd=1647545735074&rows=2147483647&page=1&sidx=id&sord=desc")
data = request.json()
i = 1

for element in data.get("rows"):
    print('Load rows: ' + f"{i}")
    result_data.append(
        {
            "Id": element['cell'][0],
            "ISIN CODE": element['cell'][2],
            "FIGI CODE": element['cell'][3],
            "Ceiling price": element['cell'][4],
            "Floor price": element['cell'][5],
            "Reference price": element['cell'][6],
            "Open price": element['cell'][7],
            "Close price": element['cell'][8],
            "Up/Down": element['cell'][9],
            "Up/Down(%)": element['cell'][10],
            "Low price": element['cell'][11],
            "High price": element['cell'][12],
            "Average price": element['cell'][13],
            "Trading volume": element['cell'][14],
            "Trading value": element['cell'][15]
        }
    )
    i += 1

with open("result_data.json", "w") as file:
    json.dump(result_data, file, indent=4, ensure_ascii=False)

with open("result_data.csv", "w") as file:
    file_writer = csv.DictWriter(file, fieldnames=list(result_data[0].keys()))
    for element in result_data:
        file_writer.writerow(element)
