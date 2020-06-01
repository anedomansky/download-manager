# download-manager

Python desktop app

## Requirements

- Linux:
    `sudo apt install xclip`            - necessary for pyperclip to work

## Development Setup

1. `python3 -m venv env`
2. `source env/bin/activate`            - close virtualenv with `deactivate`
3. `pip install -r requirements.txt`    - use `pip freeze > requirements.txt` in the project root if you are changing the dependencies
4. `pip install *`                      - add new dependencies with the virtualenv's pip
