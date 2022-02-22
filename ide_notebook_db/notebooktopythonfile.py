from ide_notebook_db.FileHandler import FileHandler


class NotebookToPythonFile(FileHandler):
    def __init__(self, path: str):
        self.path = path
        super().__init__(path)
        self.lines = self._read_file()

    def transform(self, convert_magic_run: bool = False):
        data = []
        for line in self.lines:
            if "# MAGIC %run" in line:
                if convert_magic_run:
                    data.append(self._convert_magic_run_to_import(line))
            else:
                data.append(line)

        return self._save_file(data)

    @staticmethod
    def _convert_magic_run_to_import(line: str) -> str:
        """
        Need improve
        :param line:
        :return:
        """
        line = line.replace("# MAGIC %run", "import")
        if line.count("./") == 1:
            line = line.replace("./", "")
        else:
            line = line.replace("../", "")
            line = line.replace("/", ".")

        if "\n" not in line:
            line += "\n"
        return line


