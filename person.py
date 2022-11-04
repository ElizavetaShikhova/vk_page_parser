import datetime
from parser import Parser


class Person():
    def __init__(self, id):
        self.info = Parser(id).info
        if not self.info or self.info['first_name'] == 'DELETED':
            self.info = None
            return
        self.age = self.calculate_age()
        self.status = self.get_status()
        self.sex = self.sex_to_str()
        self.name = self.info['first_name'] + " " + self.info['last_name']
        self.id = id
        if 'counters' in self.info and 'friends' in self.info['counters']:
            self.friends = self.info['counters']['friends']
        else:
            self.friends = None
        if 'counters' in self.info and 'followers' in self.info['counters']:
            self.followers = self.info['counters']['followers']
        else:
            self.followers = None
        self.relationship = self.relationship_to_str()
        self.groups = self.get_groups()
        self.posts = self.get_posts()
        self.average_n_of_likes = self.count_likes()

    def get_status(self):
        try:
            return self.info['status']
        except Exception:
            return ''

    def calculate_age(self):
        try:
            d = datetime.datetime.strptime(self.info['bdate'], '%d.%m.%Y')
            age = (int((datetime.datetime.now() - d).days / 365.2425))
        except Exception:
            age = None
        return age

    def sex_to_str(self):
        s = self.info['sex']
        if s == 0:
            return ''
        elif s == 1:
            return 'Female'
        else:
            return 'Male'

    def relationship_to_str(self):
        if 'relation' not in self.info:
            return ''
        r = self.info['relation']
        if r == 1:
            return 'not married'
        elif r == 2:
            return 'has a friend'
        elif r == 3:
            return 'engaged'
        elif r == 4:
            return 'married'
        elif r == 5:
            return 'it is complicated'
        elif r == 6:
            return 'in active search'
        elif r == 7:
            return 'in love'
        elif r == 8:
            return 'in union'
        return ''

    def get_groups(self):
        groups = Parser(self.id, 'groups').info
        if not groups:
            return []
        res = []
        for group in groups['items']:
            res.append((group['name'], f"https://vk.com/public{group['id']}"))
        return res

    def get_posts(self):
        posts = Parser(self.id, 'posts').info
        if not posts:
            return []
        return posts['items']

    def count_likes(self):
        if len(self.posts) == 0:
            return None
        summ = 0
        for i in self.posts:
            summ += i['likes']['count']
        return summ / len(self.posts)
