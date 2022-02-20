import pkg_resources

from ide_notebook_db.FileHandler import FileHandler


class ImportToMagicRun(FileHandler):
    def __init__(self, path: str):
        self.path = path
        super().__init__(path)
        self.lines = self._read_file()

    def transform(self):
        data = []
        for line in self.lines:
            if "import" in line and not self._lib_is_built_in_or_third(line):

                data.append(self._convert_import_to_magic_run(line=line))
            else:
                data.append(line)
        return self._save_file(data)

    @staticmethod
    def _convert_import_to_magic_run(line: str) -> str:
        """

        :param line: line file
        :return: line convert import to magic run databricks
        """

        if "from" in line:
            line = line.replace("from ", "# MAGIC %run ")
            line = line.split(" import")[0]
        else:
            line = line.replace("import ", "# MAGIC %run ./")

        if "\n" not in line:
            line += "\n"
        return line

    @staticmethod
    def _lib_is_built_in_or_third(line: str) -> bool:
        lib = line.split(" ")[1].replace("\n", "").split(".")[0]
        dists = [d.key for d in pkg_resources.working_set]
        return True if lib in dists else False




