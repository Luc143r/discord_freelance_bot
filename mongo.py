from pymongo import MongoClient
from config import settings_db
import json


client = MongoClient(settings_db['host'], settings_db['port'])
db = client[settings_db['name_db']]
collect_ds = db[settings_db['collect_ds']]
collect_users = db[settings_db['collect_users']]


def get_data(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


"""print(get_data(collect_ds, {'_id': 'luc143r#6330'})['chatId'])
_id = get_data(collect_ds, {'_id': 'luc143r#6330'})['chatId']

print(get_data(collect_users, {'_id': _id}))"""


def get_id(nickname):
    collect_ds = db[settings_db['collect_ds']]
    elements = {'_id': nickname}
    return collect_ds.find_one(elements)['chatId']


def get_points(_id):
    collect_users = db[settings_db['collect_users']]
    elements = {'_id': _id}
    data_str = collect_users.find_one(elements)['state']
    data_json = json.loads(data_str)
    try:
        count_point = data_json['MMR']
    except KeyError:
        count_point = 0
    return count_point


# print(get_id('luc143r#6330'))
print(get_points(get_id('Egogo#8170')))
