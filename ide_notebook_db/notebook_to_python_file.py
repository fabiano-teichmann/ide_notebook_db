import os
import importlib

import click


class NotebookToPythonFile:
    def __init__(self, lines: list):
        self.lines = lines

    def remove_magic_run(self):
        data = []
        for line in self.lines:
            if "# MAGIC %run" not in line:
                data.append(line)
            else:
                data.append(self.convert_magic_import(line))
        return data

    @staticmethod
    def convert_magic_import(line: str) -> str:
        line = line.replace("# MAGIC %run ", "")
        line = line.replace("../", "").replace("./", "")
        part_path_file = line + ".py"
        line = line.replace("/", ".")

        try:
            files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(os.getcwd()) for f in filenames if
                     os.path.splitext(f)[1] == '.py']
            for file in files:
                if part_path_file in file:
                    cwd = os.path.split(os.getcwd())[1]
                    file = file.split("/")
                    file = file[file.index(cwd) + 1:]
                    module = ".".join(f.replace(".py", "") for f in file)
                    modules = dir(importlib.import_module(module))
                    list_module = []
                    for m in modules:
                        if "__" not in m:
                            try:
                                importlib.import_module(m)
                            except ModuleNotFoundError:
                                list_module.append(m)
                    if list_module:
                        return f"from {cwd}.{line} import " + ", ".join(m for m in list_module)
                    return f"import {line}"
        except ModuleNotFoundError:
            click.echo('⚠️ \033[31m' + 'Warming: ' + '\033[30m' + f"Not found module {line}")
            return ''

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
