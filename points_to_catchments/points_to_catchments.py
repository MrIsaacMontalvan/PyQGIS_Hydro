# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PointsToCatchments
                                 A QGIS plugin
 This plugin calculate the catchment for each point in a vector layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-03-09
        copyright            : (C) 2019 by Hans van der Kwast/IHE Delft
        email                : h.vanderkwast@un-ihe.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Hans van der Kwast/IHE Delft'
__date__ = '2019-03-09'
__copyright__ = '(C) 2019 by Hans van der Kwast/IHE Delft'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .points_to_catchments_provider import PointsToCatchmentsProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class PointsToCatchmentsPlugin(object):

    def __init__(self):
        self.provider = PointsToCatchmentsProvider()

    def initGui(self):
        QgsApplication.processingRegistry().addProvider(self.provider)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)