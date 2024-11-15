# Classic Cipher Application
A Python application that implements various classical cryptographic ciphers for text encryption and decryption.

## Features
* Multiple classical cipher implementations:
 * Caesar Cipher
 * Vigenère Cipher
 * Substitution Cipher
 * Transposition Cipher
* Support for both encryption and decryption
* GUI interface
* Support for uppercase, lowercase letters, and spaces
* Comprehensive test suite using pytest

## Installation
1. Clone the repository:
```bash
git clone https://github.com/hakouguelfen/cipher.git
cd classic-cipher-app
```

2. Ensure you have Python 3.7+ installed:
```bash
python --version
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Dependencies include:
 * pytest
 * pytest-cov (for coverage reports)
 * tkinter (for graphical interface)
 * ttkthemes (for modern themes)

## Usage
### Command Line Interface

```bash
python cipher/main.py
```

## Testing

### Running Tests
Run the entire test suite:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=ciphers tests/
```

Run specific test file:
```bash
pytest tests/test_caesar.py
```

### Test Structure

```
tests/
├── __init__.py
├── test_caesar.py
├── test_vigenere.py
├── test_substitution.py
├── test_atbash.py
└── test_utils.py
```

### Test Categories
* Unit Tests: Testing individual cipher implementations
 * Encryption/decryption functionality
 * Edge cases
 * Input validation
* Integration Tests: Testing cipher interactions
 * Command-line interface
 * File handling
 * End-to-end encryption/decryption
* Parametrized Tests: Testing multiple inputs

```python
@pytest.mark.parametrize("input_text,shift,expected", [
    ("hello", 3, "khoor"),
    ("WORLD", 1, "XPSME"),
    ("Hello, World!", 5, "Mjqqt, Btwqi!")
])
def test_caesar_encrypt(input_text, shift, expected):
    assert caesar_encrypt(input_text, shift) == expected
```

## Supported Ciphers
### Caesar Cipher
* Shifts each letter in the plaintext by a fixed number of positions
* Key: Integer (shift value)

### Vigenère Cipher
* Uses a keyword to shift letters based on the keyword's letters
* Key: String (keyword)

### Substitution Cipher
* Replaces each letter with another letter based on a substitution alphabet
* Key: 26-letter substitution alphabet

## Acknowledgments
* Inspiration from classical cryptography
* Python community resources
* pytest documentation and community
