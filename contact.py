import json


class Contact:
    def __init__(self, id=None, first=None, last=None, phone=None, email=None):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.errors = {}

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def update(self, first, last, phone, email):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def validate(self):
        if not self.email:
            self.errors['email'] = 'Email is required'
        return len(self.errors) == 0
