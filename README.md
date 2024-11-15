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
└── test_transposition.py
```

### Test Categories
* Unit Tests: Testing individual cipher implementations
 * Encryption/decryption functionality
 * Edge cases
 * Input validation
* Parametrized Tests: Testing multiple inputs

```python
messages = [
    ("", 1),  # Edge case: empty message
    ("A", 1),  # Single character
    ("AB", 1),  # Single key
    ("AB", 2),  # Key equal to message length
    ("This is a test message!", 4),  # Common case
    ("Short", 10),  # Key greater than message length
    ("EdgeCase", 3),  # Odd message length
    ("AnotherTest", 5),  # Key not dividing message length evenly
]
@pytest.mark.parametrize("message, key", messages)
def test_encrypt_decrypt(message, key):
    """Test encryption followed by decryption returns the original message."""
    encrypted = transposition.cipher(message, key, CMD.ENCRYPT)
    decrypted = transposition.cipher(encrypted, key, CMD.DECRYPT)
    assert decrypted == message
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
