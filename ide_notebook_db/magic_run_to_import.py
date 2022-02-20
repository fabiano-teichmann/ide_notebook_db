from ide_notebook_db.FileHandler import FileHandler


class MagicRunToImport(FileHandler):
    def __init__(self, path: str):
        self.path = path
        super().__init__(path)
        self.lines = self._read_file()

    def transform(self):
        data = []
        for line in self.lines:
            # line = line.replace(" ", "")
            if "# MAGIC %run" in line:
                line = line.replace("# MAGIC %run", "import")
                if line.count("./") == 1:
                    line = line.replace("./", "")
                else:
                    line = line.replace("../", "")
                    line = line.replace("/", ".")

                if "\n" not in line:
                    line += "\n"
                data.append(line)
            else:
                data.append(line)

        return self._save_file(data)
