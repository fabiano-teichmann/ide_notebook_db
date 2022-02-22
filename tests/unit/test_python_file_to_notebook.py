import pytest

from ide_notebook_db.python_file_to_notebook import PythonFileToNotebook


class TestPythonFileToNotebook:

    @pytest.mark.parametrize('lib', [
        {
            'import': 'from share import share',
            'magic_run': '# MAGIC %run ./share',
            'root_path': 'main.py'
        },
        {
            'import': 'from logger import logger',
            'magic_run': '# MAGIC %run ./logger',
            'root_path': 'main.py'
        },
        {
            'import': 'from share.share import share',
            'magic_run': '# MAGIC %run ./share/share',
            'root_path': 'main.py'
        },
        {
            'import': 'from utils.logger import logger',
            'magic_run': '# MAGIC %run ./utils/logger',
            'root_path': 'main.py'
        },
        {
            'import': 'from utils.logger import logger',
            'magic_run': '# MAGIC %run ../../utils/logger',
            'root_path': 'test/unit/test.py'
        }
    ])
    def test_transform_import_in_magic_run(self, lib):
        data = PythonFileToNotebook(lines=[lib['import']],
                                    path=lib['root_path']).transform()

        command = "# COMMAND ---------- \n"
        magic_run = f"{command}{lib['magic_run']}\n{command}"
        assert '# Databricks notebook source\n' == data[0]
        assert magic_run == data[1]
        assert command == data[2]
