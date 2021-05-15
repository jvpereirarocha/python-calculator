from apps import app


class TestApp:
    def test_get_list_numbers(self):
        assert 5 in app.get_list_numbers()
