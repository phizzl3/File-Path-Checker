"""

Checks to see if the passed files exists in their specific file paths.
If files are not found: 
    - It creates the paths (parent folder).
    - It displays a message with the missing file name and path to the console.
    
Args:
    Accepts multiple str/pathlib.Path paths to files.
        

"""

__version__ = "1.0.0"


from pathlib import Path


def checkpaths(*args) -> None:
    """Checks to see if the passed files exists in their specific file paths.
    If files are not found:
    - It creates the paths (parent folder).
    - It displays a message with the missing file name and path to the console.

    Args:
        Accepts multiple str/pathlib.Path paths to files.
    """

    for file_path in args:
        # Generate Path objects of each.
        check_path = Path(file_path)
        # Loop until each file is located.
        while True:
            # Check to see if file path exists.
            if not check_path.exists():
                # If file path's parent folder doesn't exist, create it.
                if not check_path.parent.is_dir():
                    check_path.parent.mkdir(parents=True)
                # Display messages to the user.
                print(f"\n File: '{check_path.name}' not found.")
                print("\n Place the file in the following directory and press Enter:")
                input(f" '{check_path.parent}'")
            else:
                break
