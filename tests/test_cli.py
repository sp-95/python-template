from _pytest.logging import LogCaptureFixture

from src.project_template.cli import Main, __version__


class TestMain:
    @staticmethod
    def test_version(caplog: LogCaptureFixture) -> None:
        main = Main()
        version = main.version()
        assert version in caplog.text
        assert version == __version__

    @staticmethod
    def test_option(caplog: LogCaptureFixture) -> None:
        Main(option="extra").version()
        assert "Hello, World!" in caplog.text
