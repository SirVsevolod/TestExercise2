import requests

def check_name(link):
    response = requests.get(link)
    products = response.json()['products']
    res = []
    for pr in products:
        res.append("Alcatel" in pr['name'])
    return res


def check_sort(link):
    response = requests.get(link)
    products = response.json()['products']
    res = []
    for pr in products:
        res.append(pr['name'])
    copy_res = res.copy()
    return copy_res == res.sort()