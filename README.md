# macinfo version 0.0.4a
Search mac info offline in about 29915 tech companies

# Usage

First of all, import the package.

(**Note**: you need to import the class "Company" or it will not work, you can simply use **"import *"**)

```
from macinfo import *
```
Print all available companies name
```
print([company.name for company in all_companies()])
```
Print all available companies name where mac address contains "00"
```
print([company.name for company in search_company_by_mac(mac_address="00")])
```
Print all available companies mac address where alpha-2 country code is "US"
```
print([company.mac_hex_formatted for company in search_company_by_country(country_code="US")])
```
Print if is available a company with mac address "00:00:00"
```
if search_company_by_mac(mac_address="00:00:00"):
    print("Available")

else:
    print("Not available")
```
Print all available mac addresses of "Microsoft" 
```
print([company.mac_hex_formatted for company in search_company_by_name("Microsoft")])
```
Check if exists the mac address "E0:E0:C2" in the available companies in China, if exists print the company's info
```
if "E0:E0:C2" in [company.mac_hex_formatted for company in search_company_by_country(country_code="CN")]:
    print(search_company_by_mac(mac_address="E0:E0:C2")[0].info)

else:
    print("E0:E0:C2 not exists in China")
```
