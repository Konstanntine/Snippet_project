# -*- coding: utf-8 -*-
import json
import os
import shutil
from datetime import datetime

def init_snippets_file(filename="snippets.json"):
    if not os.path.exists(filename):
        sample_data = [
            {
                "title": "Hello World",
                "code": "print('Hello, world!')",
                "language": "Python",
                "tags": ["intro", "print"],
                "created": "2025-06-28"
            },
            {
                "title": "Factorial (Recursive)",
                "code": "def fact(n): return 1 if n <= 1 else n * fact(n - 1)",
                "language": "Python",
                "tags": ["math", "recursion"],
                "created": "2025-06-28"
            }
        ]
        with open(filename, "w") as f:
            json.dump(sample_data, f, indent=4)

def load_snippets(filename="snippets.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def backup_snippets_file(original="snippets.json", backup_dir="backups"):
    if not os.path.exists(original):
        return  # Nothing to back up

    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{backup_dir}/snippets_backup_{timestamp}.json"
    shutil.copy2(original, backup_name)

def save_snippets(snippets, filename="snippets.json"):
    backup_snippets_file(filename)
    with open(filename, "w") as f:
        json.dump(snippets, f, indent=4)



if __name__ == "__main__":
    init_snippets_file()


