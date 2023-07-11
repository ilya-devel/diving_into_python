from pathlib import Path

from some_package import hometask

if __name__ == '__main__':
    path = Path(Path().cwd())
    hometask.scan_directory_and_write_info(path, file_name='checking')
