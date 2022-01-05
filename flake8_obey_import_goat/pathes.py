

def convert_filepath_to_importable(filepath: str) -> str:
    return filepath[:-3].replace('/', '.')
