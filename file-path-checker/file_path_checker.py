"""

 Checks to see if files exists in a file path, creates 
 the path, and displays a message if not found.

Version = 0.1.0

"""

from pathlib import Path


def check_file_path(*args) -> None:
    """Checks to see if the passed files exists in a file path, creates 
    the path, and displays a message if not found.
    """
    
    for file_path in args:
        # Generate Path objects of each.
        check_path = Path(file_path)
        # Skip if file path exists.
        if check_path.exists():
            continue
        # If file path's parent folder doesn't exist, create it. 
        if not check_path.parent.is_dir():
            check_path.parent.mkdir()
        print(f"\n File: '{check_path.name}' not found.")
        print(f" Place the file in the following directory and press Enter:")
        input(f" '{check_path.parent}'")
        
        