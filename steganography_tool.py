from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import stepic
from PIL import Image
import base64
import argparse
import sys

def encrypt_text(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + cipher_text).decode()

def decrypt_text(enc_text, key):
    enc_bytes = base64.b64decode(enc_text)
    iv = enc_bytes[:16]
    cipher_text = enc_bytes[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()

def hide_text_in_image(image_path, text, output_path, key):
    encrypted_text = encrypt_text(text, key)
    image = Image.open(image_path)
    encoded_image = stepic.encode(image, encrypted_text.encode())
    encoded_image.save(output_path, "PNG")
    print(f"✅ Text hidden successfully in {output_path}")

def extract_text_from_image(image_path, key):
    image = Image.open(image_path)
    extracted_data = stepic.decode(image)
    
    try:
        decrypted_text = decrypt_text(extracted_data, key)
        print("🔍 Extracted Text:")
        print(decrypted_text)
    except Exception as e:
        print("❌ Error: Unable to decrypt. Incorrect key or corrupted data.")

def main():
    parser = argparse.ArgumentParser(description="Steganography Tool with AES Encryption")
    parser.add_argument("-e", "--embed", help="Embed text into an image", action="store_true")
    parser.add_argument("-x", "--extract", help="Extract text from an image", action="store_true")
    parser.add_argument("-i", "--image", help="Path to the image file", required=True)
    parser.add_argument("-t", "--text", help="Text to hide (or path to text file)")
    parser.add_argument("-o", "--output", help="Output image file")
    parser.add_argument("-k", "--key", help="16-byte AES key", required=True)
    
    args = parser.parse_args()
    
    key = args.key.encode()
    if len(key) != 16:
        print("❌ Error: AES key must be exactly 16 bytes long.")
        sys.exit(1)

    if args.embed:
        if not args.text:
            parser.error("❌ The -t argument is required when using -e (embed).")
        if not args.output:
            parser.error("❌ The -o argument is required when using -e (embed).")

        text = args.text
        if text.endswith(".txt"):
            with open(text, "r") as file:
                text = file.read()
        
        hide_text_in_image(args.image, text, args.output, key)

    elif args.extract:
        extract_text_from_image(args.image, key)
    
    else:
        print("❌ Error: Use -e to embed or -x to extract.")

if __name__ == "__main__":
    main()
