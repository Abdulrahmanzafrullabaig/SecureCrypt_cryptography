# SecureCrypt - Text Encryption & Decryption Tool

A modern, web-based encryption tool that implements classical cryptography algorithms including Caesar Cipher and Vigenère Cipher. Secure your messages with military-grade encryption that runs entirely in your browser.

## 🌟 Features

- **Dual Encryption Algorithms**: 
  - Caesar Cipher (simple shift-based encryption)
  - Vigenère Cipher (keyword-based encryption - more secure)
- **Bidirectional Operations**: Encrypt and decrypt text with ease
- **Modern UI/UX**: Beautiful, responsive interface with real-time feedback
- **Privacy First**: All processing happens locally in your browser - no data leaves your device
- **Cross-Platform**: Works on desktop and mobile browsers
- **No Installation Required**: Runs directly in your web browser

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Flask web framework

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Text-Encryption-Decryption-using-Caesar-Cipher.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Text-Encryption-Decryption-using-Caesar-Cipher
   ```

3. Install required dependencies:
   ```bash
   pip install flask
   ```

### Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. The application will automatically open in your default browser after a few seconds.

## 🛠️ How to Use

1. **Select Cipher Method**:
   - Choose between Caesar Cipher (simple numeric shift) or Vigenère Cipher (keyword-based)

2. **Enter Your Text**:
   - Type or paste the text you want to encrypt or decrypt in the input field

3. **Set Encryption Parameters**:
   - For Caesar Cipher: Enter a numeric key (e.g., 3)
   - For Vigenère Cipher: Enter an alphabetic keyword (e.g., "SECRET")

4. **Choose Operation Mode**:
   - Encrypt: Encode your plain text into cipher text
   - Decrypt: Decode cipher text back to plain text

5. **Process Text**:
   - Click the "Process Text" button to perform the encryption/decryption

6. **Manage Results**:
   - Copy the result to clipboard with the "Copy" button
   - Download the result as a text file with the "Save" button
   - Use "Swap" to exchange input and output for reverse operations
   - Use "Clear All" to reset all fields

## 🔐 Encryption Methods Explained

### Caesar Cipher
- Shifts each letter by a fixed number of positions in the alphabet
- Example: With key 3, 'A' becomes 'D', 'B' becomes 'E', etc.
- 'HELLO' with key 3 becomes 'KHOOR'

### Vigenère Cipher
- Uses a keyword to determine variable shifts for each letter
- Much more secure than Caesar Cipher due to variable shifts
- Example: 'HELLO' with keyword 'KEY' becomes 'RIJVS'

## 🧱 Project Structure

```
Text-Encryption-Decryption-using-Caesar-Cipher/
│
├── app.py                 # Flask web application
├── encryption_tool.py     # Core encryption algorithms
├── templates/
│   └── index.html        # Modern web interface
└── README.md             # This file
```

## 🧪 Core Functions

### Caesar Cipher
```python
def caesar_encrypt(text: str, key: int) -> str:
    # Implementation details...

def caesar_decrypt(text: str, key: int) -> str:
    # Implementation details...
```

### Vigenère Cipher
```python
def vigenere_encrypt(text: str, key: str) -> str:
    # Implementation details...

def vigenere_decrypt(text: str, key: str) -> str:
    # Implementation details...
```

## 🎨 UI Features

- **Responsive Design**: Works beautifully on mobile, tablet, and desktop
- **Dark/Light Mode**: Automatic theme based on system preferences
- **Real-time Validation**: Instant feedback on input errors
- **Animated Transitions**: Smooth animations for better user experience
- **Accessibility**: Proper contrast ratios and keyboard navigation support

## 🔒 Security & Privacy

- **Client-Side Processing**: All encryption/decryption happens in your browser
- **No Data Collection**: We don't collect, store, or transmit any user data
- **Open Source**: Transparent code that anyone can audit
- **No External Dependencies**: Minimal external libraries for maximum security

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests for:

1. Bug fixes
2. Performance improvements
3. New cipher algorithms
4. UI/UX enhancements
5. Documentation improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by classical cryptography techniques
- Built with Flask and modern web technologies
- Designed with privacy and security as top priorities

---

<p align="center">
  Made with ❤️ and 🔒
</p>