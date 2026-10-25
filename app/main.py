from pathlib import Path

VERSION_FILE = Path(__file__).parent.parent / "version.txt"


def get_version() -> str:
    return VERSION_FILE.read_text().strip()


print(get_version())
