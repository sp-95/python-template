# -*- coding: utf-8 -*-
from pkg_resources import DistributionNotFound, get_distribution

from src.project_template.logger import log_config

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "project-template"
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:  # pragma: no cover
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

log_config.setup()
