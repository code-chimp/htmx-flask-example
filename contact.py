import json
from typing import Optional, Dict


class Contact:
    def __init__(self, id: Optional[int] = None, first: Optional[str] = None, last: Optional[str] = None,
                 phone: Optional[str] = None, email: Optional[str] = None):
        self.id: Optional[int] = id
        self.first: Optional[str] = first
        self.last: Optional[str] = last
        self.phone: Optional[str] = phone
        self.email: Optional[str] = email
        self.errors: Dict[str, str] = {}

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)

    def update(self, first: str, last: str, phone: str, email: str) -> None:
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def validate(self) -> bool:
        if not self.email:
            self.errors['email'] = 'Email is required'
        return len(self.errors) == 0
