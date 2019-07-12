import json
import requests
import os
BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool'
BASE_ENDPOINT = '/api/catalogue/detail.json?item='


def main():

    item_list = open_json('objects_87.json')

    user_in = input("Please search an item name: ")
    while user_in != "":
        for item in item_list:
            if user_in in item['name']:
                item_info = get_item_info(item)
                print("Item name: {}, Item Id: {}\nDescription: {}\nPrice: {}\n".format(
                    item_info['item']['name'],
                    item_info['item']['id'],
                    item_info['item']['description'],
                    item_info['item']['current']['price']))
        user_in = input("Please search an item name: ")


def open_json(file_name):
    curr_dir = os.path.dirname(__file__)
    relative_path = "files/" + file_name
    path = os.path.join(curr_dir, relative_path)
    with open(path, "r") as file:
        json_contents = json.loads(file.read())
    return json_contents


def get_item_info(item):
    request_url = "{}{}{}".format(BASE_URL, BASE_ENDPOINT, item['id'])
    response_json = requests.get(url=request_url)
    if response_json.status_code != 200:
        print("API Request error ", response_json, sep="")
    data = response_json.json()
    return data


main()
