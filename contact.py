"""
Defines the Contact dataclass.
"""

# Python imports.
from dataclasses import dataclass


@dataclass
class Contact:
    """
    Dataclass that represents a contact.
    """

    names: str
    lastname: str
    company: str
    phone: str
    email: str
    country: str
    web_site: str

    def __post_init__(self) -> None:
        self.data_by_element: dict = {
            'nombres': self.names,
            'apellidos': self.lastname,
            'empresa': self.company,
            'numero': self.phone,
            'email': self.email,
            'pais': self.country,
            'web': self.web_site
        }
