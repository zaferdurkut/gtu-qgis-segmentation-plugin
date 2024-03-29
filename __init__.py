# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GTUSegmentation
                                 A QGIS plugin
 This plugin work on segmentation of multiple bands with K-means
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-20
        copyright            : (C) 2022 by Zafer Durkut
        email                : durkutzafer@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GTUSegmentation class from file GTUSegmentation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gtu_segmentation import GTUSegmentation

    return GTUSegmentation(iface)
