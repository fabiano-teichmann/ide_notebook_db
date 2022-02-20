import fire

from ide_notebook_db.import_to_magic_run import ImportToMagicRun
from ide_notebook_db.list_changed_files import list_changed_files
from ide_notebook_db.magic_run_to_import import MagicRunToImport


class Com(object):
    def import_to_magic_run(self, file: str):
        if file:
            return ImportToMagicRun(file).transform()

        files = list_changed_files()
        for file in files:
            ImportToMagicRun(file).transform()

    def magic_run_to_import(self, file: str):
        if file:
            return ImportToMagicRun(file).transform()

        files = list_changed_files()
        for file in files:
            MagicRunToImport(file).transform()


def main():
    fire.Fire(Cli)


if __name__ == "__main__":
  main()

