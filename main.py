from random import randint
from person import Person
import csv


def generate_id():
    return randint(1, 25000)


c = 0
while c != 10000:
    d = {}
    p = Person(generate_id())
    if not p.info or not p.age:
        continue
    c += 1
    gr = [i[0] for i in p.groups]
    gr_l = [i[1] for i in p.groups]

    d['ID'] = p.id
    d['name'] = p.name
    d['age'] = p.age
    d['status'] = p.status
    d['groups'] = '\n'.join(gr)
    d['groups_links'] = '\n'.join(gr_l)
    d['friends'] = p.friends
    d['followers'] = p.followers
    d['likes'] = p.average_n_of_likes
    d['relationships'] = p.relationship

    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'name', 'age', 'status', 'groups', 'groups_links', 'friends', 'followers', 'likes',
                      'relationships']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(d)
