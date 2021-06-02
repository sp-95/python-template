# -*- coding: utf-8 -*-
"""
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""
import logging

import pytest

from _pytest.logging import LogCaptureFixture, _LiveLoggingNullHandler
from loguru import logger


@pytest.fixture
def caplog(caplog: LogCaptureFixture) -> LogCaptureFixture:
    class PropagateHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logging.getLogger(record.name).handle(record)

    logging.getLogger().handlers = [_LiveLoggingNullHandler()]
    handler_id = logger.add(PropagateHandler(), format="{message}")
    yield caplog
    logger.remove(handler_id)
