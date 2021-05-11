import pickle
from typing import List

path_1 = "/".join(str(__file__).split("\\")[0:-1])
path_2 = "/data/companies.py"
full_path = path_1 + path_2 if path_1 else "data/companies.py"


class Company:
    def __init__(self, name: str, mac_hex_formatted: str, mac_hex: str, address: str, country_code: str):
        """
        The class for storing a company's information.

        :param name: Company's name
        :param mac_hex_formatted: Company's mac address separated with ':', example: 00:00:00
        :param mac_hex: Company's mac address in hexadecimal, example: 000000
        :param address: Company's address
        :param country_code: Company's country_code code
        """

        self._name = name
        self._mac_hex_formatted = mac_hex_formatted
        self._mac_hex = mac_hex
        self._address = address
        self._country_code = country_code

    @property
    def name(self):
        """
        :return: The company's name
        """

        return self._name

    @property
    def mac_hex_formatted(self):
        """
        :return: The company's mac address in hexadecimal formatted as: 00:00:00
        """

        return self._mac_hex_formatted

    @property
    def mac_hex(self):
        """
        :return: The company's mac address in hexadecimal not formatted: 000000
        """

        return self._mac_hex

    @property
    def address(self):
        """
        :return: The company's address
        """

        return self._address

    @property
    def country_code(self):
        """
        :return: The company's country_code code
        """

        return self._country_code

    @property
    def info(self) -> dict:
        """
        :return: A dict containing all information about the company
        """

        return {"name": self.name,
                "mac_hex_formatted": self.mac_hex_formatted,
                "mac_hex": self.mac_hex,
                "address": self.address,
                "country_code":  self.country_code}


def search_company_by_name(name: str) -> List[Company]:
    """
    Not case sensitive search based on the name.
    It uses the "in" keyword for matching the name, so even a substring of the company's name will
    produce a True results.

    :param name: The full name or a part of the name
    :return: A list of Company instances
    """

    companies = []

    for company in pickle.load(open(full_path, "rb")):
        try:
            if name.lower() in company.name.lower():
                companies.append(company)

        except AttributeError:
            pass

    return companies


def search_company_by_mac(mac_address: str) -> List[Company]:
    """
    Search a company by its mac address.
    It automatically convert formatted hexadecimal mac address values to raw address,
    so "00:00:00", "00-00-00" or "000000" are equivalent.
    It use the "in" keyword for matching the mac address, so if a non complete mac address is provided it will return
    every company that has the same substring in the mac address, so if mac="00" it will return companies with "001111"
    or "1F004A", etc.

    :param mac_address: A hexadecimal value of a mac address
    :return: A list of Company instances
    """

    companies = []

    mac_address = mac_address.lower().replace(":", "").replace("-", "")
    mac_address = mac_address if len(mac_address) <= 6 else mac_address[:6]

    for company in pickle.load(open(full_path, "rb")):
        try:
            if mac_address in company.mac_hex.lower():
                companies.append(company)

        except AttributeError:
            pass

    return companies


def search_company_by_country(country_code: str) -> List[Company]:
    """
    Not case sensitive search by the alpha-2 country code.
    "Us", "US" or "uS" are equivalent.

    :param country_code: The alpha-2 country_code code
    :return: A list of Company instances
    """

    companies = []

    for company in pickle.load(open(full_path, "rb")):
        try:
            if country_code.lower() == company.country_code.lower():
                companies.append(company)

        except AttributeError:
            pass

    return companies


def all_companies() -> List[Company]:
    """
    Get all companies stored in the pickle file.

    :return: A list of Company instances
    """

    return pickle.load(open(full_path, "rb"))
