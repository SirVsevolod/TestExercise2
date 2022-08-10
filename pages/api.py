import requests

def check():
    response = requests.get("https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name")
    products = response.json()['products']
    res = []
    list_of_name = []
    res2 = []
    for pr in products:
        list_of_name.append(pr['name'])
        res.append('Alcatras' in pr['name'])

    return res

def js_test_task(search, sort_field):
    response = requests.get(search)
