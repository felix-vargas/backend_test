import base64

def read_image_file(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

# Example usage
image_file_path = '/Users/mamurri/Pictures/optimus_prime.jpg'
binary_data = read_image_file(image_file_path)

# Optionally, encode the binary data as base64
base64_encoded_data = base64.b64encode(binary_data)
print(base64_encoded_data)
