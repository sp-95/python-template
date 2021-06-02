from typing import Optional

import fire
from loguru import logger

from src.project_template import __version__


class Main:
    def __init__(self, option: str = "info") -> None:
        self.option = option

    def version(self) -> Optional[str]:
        if self.option.lower() == "info":
            logger.info(f"{__version__}")
            return __version__
        else:
            logger.info("Hello, World!")
            return None


def main() -> None:
    fire.Fire(Main)


if __name__ == "__main__":
    main()
