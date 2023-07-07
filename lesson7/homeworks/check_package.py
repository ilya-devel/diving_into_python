from file_operation import create_some_files
from file_operation import rename_group_files

if __name__ == '__main__':
    some_dict = {
        'txt': 5,
        'doc': 3,
        'mkv': 3,
        'mp3': 2,
        'flac': 5,
        'ini': 2,
    }
    create_some_files.some_func_ver2(some_dict, path='../files')
    rename_group_files.rename_group_files(path='../files')
