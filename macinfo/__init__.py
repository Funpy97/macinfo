"""
This package provides to search companies by name, country_code and mac address.
It works offline, there are 29915 available companies in the pickle file.
"""

from .modules.macinfo import (search_company_by_name,
                              search_company_by_country,
                              search_company_by_mac,
                              all_companies,
                              Company)