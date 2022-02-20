class FileHandler:
    def __init__(self, path: str):
        self.path = path

    def _read_file(self):
        try:
            with open(self.path, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Not found file {self.path}")

    def _save_file(self, data: list):
        with open(self.path, "w") as f:
            for d in data:
                f.write(d)