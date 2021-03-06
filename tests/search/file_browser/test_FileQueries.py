import pytest
from ulauncher.search.file_browser.FileQueries import FileQueries


class TestFileQueries:

    @pytest.fixture
    def queries(self, mocker):
        mocker.patch('ulauncher.search.file_browser.FileQueries.FileQueries._init_autosave')
        return FileQueries('basename')

    def test_put(self, queries, mocker):
        orig_put = mocker.patch('ulauncher.search.file_browser.FileQueries.KeyValueDb.put')
        time = mocker.patch('ulauncher.search.file_browser.FileQueries.time')
        queries.put('path1')
        orig_put.assert_called_with('path1', time.return_value)
