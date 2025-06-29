import json
import os
__init__ = "filegen"
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

if __name__ == "__main__":
    init_snippets_file()


