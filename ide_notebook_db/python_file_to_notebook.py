import importlib

from ide_notebook_db.FileHandler import FileHandler


class PythonFileToNotebook(FileHandler):
    def __init__(self, path: str):
        self.path = path
        self.root_path = self.path.split("/")[0]
        super().__init__(path)
        self.lines = self._read_file()

    def transform(self):
        if "# Databricks notebook source" not in self.lines[0]:
            data = self._convert_to_notebook_databricks()
        else:
            data = []
            for line in self.lines:
                data.append(self._convert_import_to_magic_run(line=line))
        return self._save_file(data)

    def _convert_to_notebook_databricks(self) -> list:
        data = ["# Databricks notebook source\n"]
        for line in self.lines:
            data.append(self._convert_import_to_magic_run(line=line))

        data.append("# COMMAND ---------- \n")
        return data

    def _convert_import_to_magic_run(self, line: str) -> str:
        """

        :param line: line file
        :return: line convert import to magic run databricks
        """
        command = "# COMMAND ---------- \n"
        if "import" in line or "from" in line:
            if not self._lib_is_built_in_or_third(line):
                magic_run = "# MAGIC %run "
                line = line.replace("from", "")
                line = line.split("import")[0]
                line = line.replace(" ", "")
                line = line.split(".")
                local = line.index(self.root_path)
                del line[line.index(self.root_path)]
                if local == 0:
                    line = magic_run + "./" + "/".join(x for x in line)
                else:
                    line = magic_run + "../" * local + "/".join(x for x in line)
            else:
                return line

            if "\n" not in line:
                line += "\n"
            return command + line + command
        return line

    @staticmethod
    def _lib_is_built_in_or_third(line: str) -> bool:
        line = line.split(" ")[1].replace("\n", "").split(".")[0]
        try:
            lib = str(importlib.import_module(line)).split(" ")[-1]
            if "/python3" in lib or "/python2" in lib:
                return True
            return False
        except ModuleNotFoundError:
            raise ModuleNotFoundError(f"Not found module {line}")


