import re
from pathlib import Path
from datetime import datetime

DATE_PATTERN = re.compile(r"_(\d{8})\.csv$")

def find_latest_file(directory: str, prefix: str) -> Path | None:

    dir_path = Path(directory)
    files = list(dir_path.glob(f"{prefix}_*.csv"))

    latest = None
    latest_date = None

    for file in files:
        match = DATE_PATTERN.search(file.name)
        if not match:
            continue

        file_date = datetime.strptime(match.group(1), "%Y%m%d")

        if latest is None or file_date > latest_date:
            latest = file
            latest_date = file_date

    return latest