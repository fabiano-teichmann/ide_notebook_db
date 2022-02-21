import fire

from ide_notebook_db.python_file_to_notebook import PythonFileToNotebook
from ide_notebook_db.list_changed_files import list_changed_files
from ide_notebook_db.notebook_to_python_file import Notebook_to_python_file


def to_notebook(file: str):
    if file:
        return PythonFileToNotebook(file).transform()

    files = list_changed_files()
    for file in files:
        PythonFileToNotebook(file).transform()


def to_python(file: str):
    if file:
        print(file)
        return Notebook_to_python_file(file).transform()

    files = list_changed_files()
    for file in files:
        Notebook_to_python_file(file).transform()


if __name__ == '__main__':
    fire.Fire()


