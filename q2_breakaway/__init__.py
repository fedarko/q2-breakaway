# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._alphas import alpha, plot
from ._chrono_plot import chrono_plot
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions

__all__ = ['breakaway']
