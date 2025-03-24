import os  # For handling file paths and environment variables
from box.exceptions import BoxValueError  # To handle specific exceptions from the Box library
import yaml  # To read and write YAML files (commonly used for configs)
from CnnClassifier import logger  # Likely a custom logger defined in your project
import json  # To handle JSON files or data
import joblib  # For serializing (saving/loading) Python objects or models
from ensure import ensure_annotations  # To enforce type annotations at runtime
from box import ConfigBox  # For using Box as a dict-like object for configs (YAML/JSON)
from pathlib import Path  # For cleaner and cross-platform file path handling
from typing import Any  # For using generic typing (accepting any type)
import base64  # For encoding/decoding data to/from base64 (useful for binary/text conversions)


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a Box object containing the config."""
    try:
        with open(path_to_yaml) as yaml_file:
            conetnt = yaml.safe_load(yaml_file)  # Load YAML content as a dictionary
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(conetnt)  # Convert dictionary to Box object (allows dot-notation access)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e  # Raise any other unexpected errors


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories if they do not exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Creates directory if it doesn't exist
        if verbose:  # If verbose=True, log the creation
            logger.info(f"Directory created: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a JSON file."""
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)  # Save the dict as JSON with indentation for readability
    
    logger.info(f"JSON file saved: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns a Box object containing the config."""
    with open(path) as f:
        content = json.load(f)  # Load JSON into a dictionary
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)  # Return as Box object


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib."""
    joblib.dump(value=data, filename=path)  # Serialize and save data as a binary file
    logger.info(f"binary file saved: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary file and returns the data."""
    data = joblib.load(path)  # Load serialized data
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in a human-readable format (KB)."""
    size_in_kb = round(os.path.getsize(path)/1024)  # Get file size in KB and round it
    return f"{size_in_kb} KB"


def decodeImage(imgstring, fileName):
    """Decodes a base64 string and writes it as an image file."""
    imgdata = base64.b64decode(imgstring)  # Decode base64 string to binary data
    with open(fileName, 'wb') as f:
        f.write(imgdata)  # Save the binary data to a file


def encodeImageIntroBase64(croppedImagePath):
    """Encodes an image file into a base64 string."""
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())  # Read image and return base64 encoded string
