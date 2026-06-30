from pathlib import Path

from config.paths import DATA_DIR


class FileManager:

    def get_path(self, filename: str) -> Path:
        """
        Returns the absolute path of the file inside DATA_DIR.
        Prevents path traversal attacks.
        """

        path = (DATA_DIR / filename).resolve()

        if not str(path).startswith(str(DATA_DIR.resolve())):
            raise ValueError("Invalid file path.")

        return path

    # ---------------------------------------------------
    # List Files
    # ---------------------------------------------------

    def list_files(self) -> str:

        files = [file.name for file in DATA_DIR.iterdir() if file.is_file()]

        if not files:
            return "No files found."

        return "\n".join(
            f"{i}. {file}"
            for i, file in enumerate(files, start=1)
        )

    # ---------------------------------------------------
    # Create File
    # ---------------------------------------------------

    def create_file(self, filename: str) -> str:

        path = self.get_path(filename)

        if path.exists():
            return f"{filename} already exists."

        path.touch()

        return f"{filename} created successfully."

    # ---------------------------------------------------
    # Delete File
    # ---------------------------------------------------

    def delete_file(self, filename: str) -> str:

        path = self.get_path(filename)

        if not path.exists():
            return "File doesn't exist."

        path.unlink()

        return f"{filename} deleted successfully."