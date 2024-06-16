import hashlib
import base64


def generate_loyalty_number(shop_name: str, registration_number: str) -> str:
    combined_string = f"{shop_name}{registration_number}"
    hash_object = hashlib.sha256(combined_string.encode())
    hash_bytes = hash_object.digest()
    
    truncated_hash_bytes = hash_bytes[:10]
    
    loyalty_number = base64.b32encode(truncated_hash_bytes).decode('utf-8').rstrip('=')
    
    return loyalty_number

loyal = generate_loyalty_number("Jasons Spaza", "123AH732JK")
print(loyal)