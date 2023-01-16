# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Starlink
                                 A QGIS plugin
 Shows the available Starlink satellites in selected geographical area.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-16
        copyright            : (C) 2023 by Alper
        email                : alperkara247@gmail.com
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
    """Load Starlink class from file Starlink.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SatelliteParse import Starlink
    return Starlink(iface)
