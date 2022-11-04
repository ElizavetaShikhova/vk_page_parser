import requests

with open('secret.txt') as f:
    TOKEN = f.readline()

class Parser():
    def __init__(self,id,type="person"):
        link, params = self.make_link(id, type)
        self.info = self.parse(link, params)
        if 'response' in self.info:
            if type == 'person':
                self.info = self.info['response'][0]
            elif type == 'groups':
                self.info = self.info['response']
            elif type == 'posts':
                self.info = self.info['response']
        else:
            self.info = None

    def parse(self, l,p):
        return requests.get(l, params=p).json()

    def make_link(self, id, type):
        if type == 'person':
            params = {'user_ids': id,
                      'fields': 'bdate,relation,sex,counters,status',
                      'access_token': TOKEN,
                      'v': 5.131}
            return 'https://api.vk.com/method/users.get', params
        elif type == 'groups':
            params = {'user_id': id,
                      'extended':1,
                      'access_token': TOKEN,
                      'v': 5.131}
            return "https://api.vk.com/method/groups.get", params
        elif type == 'posts':
            params = {'owner_id': id,
                      'extended':1,
                      'access_token': TOKEN,
                      'v': 5.131
                      }
            return "https://api.vk.com/method/wall.get", params