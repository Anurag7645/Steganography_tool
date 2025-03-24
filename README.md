# Steganography Tool with AES Encryption

## Overview
This project implements a **steganography tool** that allows users to **hide and extract text from images** using **AES encryption** for added security. The tool provides both a **command-line interface (CLI)** and a **graphical user interface (GUI)** using Tkinter.

## Features
✅ Hide a text file inside an image with encryption  
✅ Extract the hidden text from an image  
✅ AES-128 encryption ensures data security  
✅ CLI and GUI support  

## Project Structure
```
steganography_project/
│── steganography_tool.py  # Core functionality (Encryption & Steganography)
│── steganography_gui.py   # GUI interface using Tkinter
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

## Installation
### **1️⃣ Install Dependencies**
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the CLI Tool**
#### **Embed a Text File into an Image**
```bash
python steganography_tool.py -e -i input.png -t secret.txt -o output.png -k mysecretpassword123
```
#### **Extract the Hidden Text from the Image**
```bash
python steganography_tool.py -x -i output.png -k mysecretpassword123
```

### **3️⃣ Run the GUI Tool**
```bash
python steganography_gui.py
```

## Testing the Environment
To ensure everything is working correctly, follow these steps:
1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv steganography_env
   source steganography_env/bin/activate  # On macOS/Linux
   steganography_env\Scripts\activate  # On Windows
   ```
2. **Install dependencies within the environment:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run a basic test:**
   - Create a text file `test.txt` with some secret content.
   - Embed it in an image using the CLI:
     ```bash
     python steganography_tool.py -e -i sample.png -t test.txt -o output.png -k mysecretpassword123
     ```
   - Extract the hidden text from the image:
     ```bash
     python steganography_tool.py -x -i output.png -k mysecretpassword123
     ```
   - The extracted text should match `test.txt`.

## Usage
- **Select an image** (PNG/JPG/JPEG format) using the GUI.
- **Enter the text** you want to hide.
- **Provide a 16-byte encryption key** (for AES encryption).
- Click **Embed Text** to hide the data or **Extract Text** to reveal hidden content.

## Dependencies
- `pillow` (For image processing)
- `stepic` (For steganography)
- `pycryptodome` (For AES encryption)
- `tkinter` (For GUI)

## Notes
🔹 The AES encryption key **must be exactly 16 bytes long**.  
🔹 Only **PNG images** are supported for saving the modified images.  

## License
This project is licensed under the MIT License.
                                                                                                                                                                                                                    
