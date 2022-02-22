import importlib

import click


class PythonFileToNotebook:
    def __init__(self, path: str, lines: list):
        self.path = path
        self.lines = lines

    def transform(self) -> list:
        """
        if file is notebook find local lib to convert in magic run databricks, else add comments to transform in
        notebook accepted by databricks.
        :return list content data to save

        """
        if "# Databricks notebook source" not in self.lines[0]:
            data = self._convert_to_notebook_databricks()
        else:
            data = []
            for line in self.lines:
                data.append(self._convert_import_to_magic_run(line=line))
        return data

    def _convert_to_notebook_databricks(self) -> list:
        data = ["# Databricks notebook source\n"]
        for line in self.lines:
            data.append(self._convert_import_to_magic_run(line=line))

        data.append("# COMMAND ---------- \n")
        return data

    def _breadcrumb_magic_run(self, line: str) -> str:
        line = line.split(" ")[1].split(".")
        level_file = len(self.path.split("/"))
        level_import = len(line)
        magic_run = "# MAGIC %run "
        if level_import == 1 or level_file == 1:
            breadcrumb = "./"
        else:
            breadcrumb = "../" * level_import

        line = magic_run + breadcrumb + "/".join(x for x in line)
        return line

    def _convert_import_to_magic_run(self, line: str) -> str:
        """

        :param line: line file
        :return: line convert import to magic run databricks
        """
        command = "# COMMAND ---------- \n"
        if "import" in line or "from" in line:
            if self._lib_is_built_in_or_third(line):
                return line

            line = self._breadcrumb_magic_run(line)
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
            click.echo('⚠️ \033[31m' + 'Warming: ' + '\033[30m' + f"Not found module {line}")
            return False


