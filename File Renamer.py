from pathlib import Path

def rename_files(folder_path, prefix):
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist.")
        return

    for file in folder.iterdir():
        if file.is_file():  # Only rename files, not folders
            new_name = prefix + file.name
            new_path = file.with_name(new_name)
            file.rename(new_path)
            print(f"Renamed: {file.name} → {new_name}")

# Example usage
rename_files("test_folder", "2026_")
