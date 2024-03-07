import json
from datetime import time

from contact import Contact

PAGE_SIZE = 100


class ContactService:
    db = {}

    @staticmethod
    def save_db():
        out_arr = [c.__dict__ for c in ContactService.db.values()]
        with open("data/contacts.json", "w") as f:
            json.dump(out_arr, f, indent=2)

    @classmethod
    def load_db(cls):
        with open('data/contacts.json', 'r') as contacts_file:
            contacts = json.load(contacts_file)
            cls.db.clear()
            for c in contacts:
                cls.db[c['id']] = Contact(c['id'], c['first'], c['last'], c['phone'], c['email'])

    @classmethod
    def count(cls):
        time.sleep(2)
        return len(cls.db)

    @classmethod
    def all(cls, page=1):
        page = int(page)
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def search(cls, term):
        result = []

        for c in cls.db.values():
            match_first = c.first is not None and term in c.first
            match_last = c.last is not None and term in c.last
            match_email = c.email is not None and term in c.email
            match_phone = c.phone is not None and term in c.phone

            if match_first or match_last or match_email or match_phone:
                result.append(c)

        return result

    @classmethod
    def find(cls, id_):
        id_ = int(id_)
        c = cls.db.get(id_)
        if c is not None:
            c.errors = {}
        return c

    @classmethod
    def save(cls, contact):
        if contact.id is None:
            if len(cls.db) == 0:
                max_id = 1
            else:
                max_id = max(c.id for c in cls.db.values())
            contact.id = max_id + 1
            cls.db[contact.id] = contact
        cls.save_db()
        return True

    @classmethod
    def delete(cls, contact):
        del cls.db[contact.id]
        cls.save_db()

    @classmethod
    def email_exists(cls, contact):
        for c in cls.db.values():
            if c.email == contact.email and c.id != contact.id:
                return True
        return False
