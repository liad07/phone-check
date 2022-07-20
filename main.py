import phonenumbers
from phonenumbers import geocoder,carrier
x = phonenumbers.parse("+972509507172", None)
print(x)
print("valid number:"+f"{phonenumbers.is_valid_number(x)}")
print("possibility number:"+f"{phonenumbers.is_possible_number(x)}")
print(geocoder.description_for_number(x,"he"))
print(carrier.name_for_number(x,"he"))