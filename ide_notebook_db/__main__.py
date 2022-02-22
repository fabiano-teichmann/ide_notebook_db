import click

from ide_notebook_db.handler_file import HandlerFile
from ide_notebook_db.python_file_to_notebook import PythonFileToNotebook
from ide_notebook_db.list_changed_files import list_changed_files
from ide_notebook_db.notebook_to_python_file import NotebookToPythonFile


@click.group()
def cli():
    pass


@click.command("to-notebook")
@click.option('--file', default=None, help='Pass path especific file if not pass file get all files .py changed')
def to_notebook(file: str):
    if file:
        handler_file = HandlerFile(file)
        data = PythonFileToNotebook(path=file, lines=handler_file.read_file()).transform()
        handler_file.save_file(data)
        click.echo(f"File {file} transformed in notebook databricks")

    files = list_changed_files()
    for file in files:
        handler_file = HandlerFile(file)
        data = PythonFileToNotebook(path=file, lines=handler_file.read_file()).transform()
        handler_file.save_file(data)
        click.echo(f"File {file} transformed in notebook databricks")


@click.command("to-python")
@click.option('--file', default=None, help='Pass path especific file if not pass file get all files .py changed')
def remove_magic_run(file: str):
    if file:
        print(file)
        NotebookToPythonFile(file).remove_magic_run()
        click.echo(f"File {file} transformed in notebook databricks")

    files = list_changed_files()
    for file in files:
        NotebookToPythonFile(file).remove_magic_run()
        click.echo(f"File {file} transformed in notebook databricks")


cli.add_command(remove_magic_run)
cli.add_command(to_notebook)

cli()
