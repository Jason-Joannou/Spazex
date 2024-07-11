import hashlib

def generate_loyalty_number(shop_name: str, registration_number: str) -> str:
    combined_string = f"{shop_name}_{registration_number}"
    hash_object = hashlib.md5(combined_string.encode())
    hash_hex = hash_object.hexdigest()
    
    # Take the first 6 characters for a simpler identifier
    simple_identifier = hash_hex[:6]
    
    loyalty_number = f"{shop_name[:3].upper()}{registration_number[:3].upper()}{simple_identifier}"
    
    return loyalty_number

loyal = generate_loyalty_number("Jasons Spaza", "123AH732JK")
print(loyal)