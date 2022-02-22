import click

from ide_notebook_db.python_file_to_notebook import PythonFileToNotebook
from ide_notebook_db.list_changed_files import list_changed_files
from ide_notebook_db.notebooktopythonfile import NotebookToPythonFile


@click.group()
def cli():
    pass


@click.command("to-notebook")
@click.option('--file', default=None, help='Pass path especific file if not pass file get all files .py changed')
def to_notebook(file: str):
    if file:
        return PythonFileToNotebook(file).transform()

    files = list_changed_files()
    for file in files:
        PythonFileToNotebook(file).transform()


@click.command("to-python")
@click.option('--file', default=None, help='Pass path especific file if not pass file get all files .py changed')
def to_python(file: str):
    if file:
        print(file)
        return NotebookToPythonFile(file).transform()

    files = list_changed_files()
    for file in files:
        NotebookToPythonFile(file).transform()


cli.add_command(to_python)
cli.add_command(to_notebook)

cli()
