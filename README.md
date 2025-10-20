# Python Password Manager

A simple, local password manager written in Python. It uses [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) to derive a 256-bit key from a master password and a device secret, which is then used with AES-256 to encrypt and decrypt your passwords.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3
*   MariaDB (or MySQL)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/sailesh-010/Password_manager-main.git
    cd Password_manager-main
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up the database:**

    *   Make sure your MariaDB (or MySQL) server is running.
    *   Create a new user and database for the password manager.

    ```sql
    -- Log in to your database as a root user
    sudo mysql -u root

    -- Create a new user (e.g., 'pm') with a password
    CREATE USER 'pm'@'localhost' IDENTIFIED BY 'password';

    -- Grant all privileges to the new user
    GRANT ALL PRIVILEGES ON *.* TO 'pm'@'localhost';
    ```

4.  **Configure the database connection:**

    *   Create a file named `db.json` in the root of the project.
    *   Add your database credentials to this file in the following format:

    ```json
    {
        "host": "localhost",
        "user": "pm",
        "password": "password"
    }
    ```

5.  **Initialize the password manager:**

    *   Run the configuration script to set up the database tables and choose your master password.

    ```bash
    python3 config.py
    ```

## Usage

### Add a New Password

```bash
python3 pm.py a -s <site_name> -u <site_url> -l <login_username>
```

### Retrieve a Password

*   **Search for an entry and copy the password to the clipboard:**

    ```bash
    python3 pm.py e -s <site_name> -c
    ```

*   **Search by other fields:**

    You can also search by URL (`-u`), email (`-e`), or username (`-l`).

*   **View entries without revealing the password:**

    If you omit the `-c` flag, the manager will display the search results without showing the passwords.

### Generate a New Password

```bash
python3 pm.py g --length <password_length>
```

This will generate a secure password of the specified length and copy it to your clipboard.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.