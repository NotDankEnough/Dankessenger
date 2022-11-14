from json import load, dump
from os.path import exists


class JSONController:
    """Controller for JSON data."""
    latest_filepath: str = ""
    """Latest path to JSON file."""

    content: any
    """Content of latest JSON file."""

    default_type: any
    """Type of JSON content."""

    @classmethod
    def load(cls, file_path: str, default_type: dict | list) -> None:
        """Load and parse JSON content to Python dictionary."""

        if not exists(file_path):
            cls.content = default_type
            cls.save(file_path)
            return
        
        with open(file_path, "r") as f:
            cls.content = load(f)
            f.close()
        
        cls.latest_filepath = file_path
        cls.default_type = type(default_type)
    
    @classmethod
    def save(cls, file_path: str) -> None:
        """Save Python dictionary to JSON file."""
        with open(file_path, "w") as f:
            dump(cls.content, f, indent=4, sort_keys=True)
            f.close()
