from __future__ import absolute_import
from apps import main


class TestMain:
    def test_upper_text(self):
        assert main.upper_text('hello') == 'HELLO'
