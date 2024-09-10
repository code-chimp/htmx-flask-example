import json
from typing import Dict, List, Optional
from contact import Contact

PAGE_SIZE = 10


class ContactService:
    db: Dict[int, Contact] = {}

    @staticmethod
    def save_db() -> None:
        out_arr: List[Dict] = [c.__dict__ for c in ContactService.db.values()]
        with open("data/contacts.json", "w") as f:
            json.dump(out_arr, f, indent=2)

    @classmethod
    def load_db(cls) -> None:
        with open('data/contacts.json', 'r') as contacts_file:
            contacts: List[Dict] = json.load(contacts_file)
            cls.db.clear()
            for c in contacts:
                cls.db[c['id']] = Contact(c['id'], c['first'], c['last'], c['phone'], c['email'])

    @classmethod
    def count(cls) -> int:
        return len(cls.db)

    @classmethod
    def all(cls, page: int = 1) -> List[Contact]:
        page = int(page)
        start: int = (page - 1) * PAGE_SIZE
        end: int = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def search(cls, term: str) -> List[Contact]:
        result: List[Contact] = []

        for c in cls.db.values():
            match_first: bool = c.first is not None and term in c.first
            match_last: bool = c.last is not None and term in c.last
            match_email: bool = c.email is not None and term in c.email
            match_phone: bool = c.phone is not None and term in c.phone

            if match_first or match_last or match_email or match_phone:
                result.append(c)

        return result

    @classmethod
    def find(cls, id_: int) -> Optional[Contact]:
        id_ = int(id_)
        c: Optional[Contact] = cls.db.get(id_)
        if c is not None:
            c.errors = {}
        return c

    @classmethod
    def save(cls, contact: Contact) -> bool:
        if contact.id is None:
            if len(cls.db) == 0:
                max_id: int = 1
            else:
                max_id = max(c.id for c in cls.db.values())
            contact.id = max_id + 1
            cls.db[contact.id] = contact
        cls.save_db()
        return True

    @classmethod
    def delete(cls, contact: Contact) -> None:
        del cls.db[contact.id]
        cls.save_db()

    @classmethod
    def email_exists(cls, contact: Contact) -> bool:
        for c in cls.db.values():
            if c.email == contact.email and c.id != contact.id:
                return True
        return False
