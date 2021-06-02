import pytest

from _pytest.monkeypatch import MonkeyPatch

from src.project_template.config import Config


@pytest.mark.parametrize("environment", ["development", "production"])
def test_env(monkeypatch: MonkeyPatch, environment: str) -> None:
    monkeypatch.setenv("ENV_FOR_DYNACONF", environment)
    settings = Config(environment=True)

    assert settings.env == environment
    assert settings.debug is False if environment == "production" else True
