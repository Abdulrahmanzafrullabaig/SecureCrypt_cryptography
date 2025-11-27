from flask import Flask, request, jsonify, render_template
import webbrowser
import threading

app = Flask(__name__)

def caesar_encrypt(text: str, key: int) -> str:
    key = (key % 26 + 26) % 26
    out = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            out.append(chr((ord(ch) - base + key) % 26 + base))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            out.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)

def caesar_decrypt(text: str, key: int) -> str:
    key = (key % 26 + 26) % 26
    return caesar_encrypt(text, -key)

def vigenere_encrypt(text: str, key: str) -> str:
    key_filtered = ''.join([c for c in key.lower() if c.isalpha()])
    if not key_filtered:
        raise ValueError("Vigenere key must contain at least one letter (a-z).")
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key_filtered[ki % len(key_filtered)]) - ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def vigenere_decrypt(text: str, key: str) -> str:
    key_filtered = ''.join([c for c in key.lower() if c.isalpha()])
    if not key_filtered:
        raise ValueError("Vigenere key must contain at least one letter (a-z).")
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key_filtered[ki % len(key_filtered)]) - ord('a')
            out.append(chr((ord(ch) - base - shift + 26*10) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process():
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify(success=False, error="Invalid JSON payload"), 400

    cipher = data.get('cipher')
    mode = data.get('mode')
    text = data.get('text', '')
    key = data.get('key', '')

    try:
        if cipher == 'caesar':
            try:
                k = int(key)
            except Exception:
                return jsonify(success=False, error="Caesar cipher requires numeric key"), 400

            if mode == 'encrypt':
                res = caesar_encrypt(text, k)
            elif mode == 'decrypt':
                res = caesar_decrypt(text, k)
            else:
                return jsonify(success=False, error="Invalid mode"), 400

        elif cipher == 'vigenere':
            if not isinstance(key, str) or not any(ch.isalpha() for ch in key):
                return jsonify(success=False, error="Vigenère key must contain alphabetic characters"), 400

            if mode == 'encrypt':
                res = vigenere_encrypt(text, key)
            elif mode == 'decrypt':
                res = vigenere_decrypt(text, key)
            else:
                return jsonify(success=False, error="Invalid mode"), 400
        else:
            return jsonify(success=False, error="Invalid cipher selection"), 400

        return jsonify(success=True, result=res)

    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

if __name__ == '__main__':
    # Auto-open browser after a short delay
    def open_browser():
        webbrowser.open('http://127.0.0.1:5000')
    
    timer = threading.Timer(1.5, open_browser)
    timer.start()
    
    # Debug mode helps during development
    app.run(host='127.0.0.1', port=5000, debug=True)