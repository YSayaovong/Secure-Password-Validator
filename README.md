# Password Checker

A simple Python script to check if your password has been compromised in any known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

## Features

- **Password Strength Check**: This script checks if a given password has appeared in public data breaches.
- **Secure Hashing**: The password is securely hashed using SHA-1 before being checked against the API, ensuring the full password is never sent over the network.
- **Real-time Feedback**: Get immediate feedback on whether your password has been compromised and how many times it has appeared in data breaches.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/password-checker.git
    cd password-checker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python check_password.py
    ```

2. You will be prompted to enter a password:
    ```
    Enter a password to check: 
    ```

3. The script will check if the password has been found in any known data breaches and return the number of times it has been compromised (if any).

## Example

Enter a password to check: password123 Your password was found 52345 times... you should probably change it!


If the password has not been found in any breach:

Enter a password to check: S3cur3P@ssw0rd Your password was NOT found. Carry on!


## How It Works

- The password is first hashed using the SHA-1 algorithm.
- The first 5 characters of the hashed password are sent to the [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords).
- The API returns a list of hashes with the same prefix. The script compares the rest of the hash with the returned hashes to see if the password has been compromised.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add your feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Have I Been Pwned](https://haveibeenpwned.com/) service.
