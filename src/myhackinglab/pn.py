import phonenumbers as p_number
from phonenumbers.geocoder import description_for_number
from phonenumbers.util import u


def numdata(number, lang, region=None):  # REGION "GB"
    n = p_number.parse(number=number, region=region)
    country_code = n.country_code
    national_number = n.national_number
    city = description_for_number(n, lang=lang)
    return country_code, national_number, city


data = numdata(number="+442083612345", region="DE", lang="de")
print(data[0])