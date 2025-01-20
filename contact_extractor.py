"""
Defines the ContactExtractor class.
"""

# Python imports.
import pandas as pd

# Project imports.
from contact import Contact


class ContactExtractor:
    """
    Class that represents an extrator to get the contact data.
    """

    def __init__(self, file_path: str) -> None:
        """
        Constructor of the ContactExtractor class.
        """
        self.__file_path = file_path

    def get_contacts(self) -> list[Contact]:
        """
        Gets the contact data from an excel file and returns it in a list.
        @return:    List of Contact objects.
        """
        contacts = []

        try:
            contact_data = pd.read_excel(self.__file_path)

            for _, row in contact_data.iterrows():
                contacts.append(
                    Contact(names=row['Nombres'],
                            lastname=row['Apellidos'],
                            company=row['Empresa'],
                            phone=row['Numero'],
                            email=row['Email'],
                            country=row['Pais'],
                            web_site=row['Web']))
            return contacts
        except Exception as err:
            raise Exception(f'Failed data extraction: {str(err)=}')
