import mysql.connector
import json
import os
from rich import print as printc
from rich.console import Console

console = Console()

def dbconfig():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'db.json')
    try:
        with open(config_path) as f:
            config = json.load(f)
    except FileNotFoundError:
        printc("[red][!][/red] Database configuration file 'db.json' not found.")
        printc("Please create a 'db.json' file in the root directory with your database credentials.")
        printc("Example:")
        printc('''
{
    "host": "localhost",
    "user": "pm",
    "password": "password"
}
        ''')
        return None
    except json.JSONDecodeError:
        printc("[red][!][/red] Invalid JSON in 'db.json'. Please check the file format.")
        return None

    try:
        db = mysql.connector.connect(
            host=config.get('host', 'localhost'),
            user=config.get('user'),
            password=config.get('password')
        )
        return db
    except mysql.connector.Error as e:
        printc(f"[red][!] Database connection error: {e}[/red]")
        return None
    except Exception as e:
        console.print_exception(show_locals=True)
        return None