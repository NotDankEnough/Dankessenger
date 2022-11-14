from json import load, dump
from os.path import exists


class JSONController:
    """Controller for JSON data."""
    latest_filepath: str = ""
    """Latest path to JSON file."""

    content: dict[str, any] = {}
    """Content of latest JSON file."""

    @classmethod
    def load(cls, file_path: str) -> None:
        """Load and parse JSON content to Python dictionary."""

        if not exists(file_path):
            cls.save(file_path)
            return
        
        with open(file_path, "r") as f:
            cls.content = load(f)
            f.close()
        
        cls.latest_filepath = file_path
    
    @classmethod
    def save(cls, file_path: str) -> None:
        """Save Python dictionary to JSON file."""
        with open(file_path, "w") as f:
            dump(cls.content, f, indent=4, sort_keys=True)
            f.close()
