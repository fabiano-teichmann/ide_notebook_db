import fire

from ide_notebook_db.python_file_to_notebook import PythonFileToNotebook
from ide_notebook_db.list_changed_files import list_changed_files
from ide_notebook_db.notebook_to_python_file import Notebook_to_python_file


class Com(object):
    def import_to_magic_run(self, file: str):
        if file:
            return PythonFileToNotebook(file).transform()

        files = list_changed_files()
        for file in files:
            PythonFileToNotebook(file).transform()

    def magic_run_to_import(self, file: str):
        if file:
            return PythonFileToNotebook(file).transform()

        files = list_changed_files()
        for file in files:
            Notebook_to_python_file(file).transform()


def main():
    fire.Fire(Cli)


if __name__ == "__main__":
  main()

