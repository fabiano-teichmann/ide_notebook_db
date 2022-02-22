import pytest

from example_notebooks.share.save_share.save_share import save_share
from ide_notebook_db.notebook_to_python_file import NotebookToPythonFile


class TestNotebookToPython:
    @pytest.mark.parametrize('lib', [
        {
            'import': 'from ide_notebook_db.utils.logger import logger',
            'magic_run': '# MAGIC %run ../../utils/logger'
        },

        {
            'import': 'from ide_notebook_db.share.save_share.save_share import save_share',
            'magic_run': '# MAGIC %run ./share/save_share/save_share',
        }
    ])
    def test_transform_magic_run_to_import(self, lib):
        data = NotebookToPythonFile(lines=[lib['magic_run']]).remove_magic_run()
        assert data[0] == lib["import"]
