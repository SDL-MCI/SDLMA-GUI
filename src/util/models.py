import numpy as np
from PySide6 import QtCore, QtGui

tick = QtGui.QColor("green")


def data_proto(
    arr: list,
    index: QtCore.QModelIndex,
    role: QtGui.Qt.ItemDataRole.DisplayRole,
):
    """
    Default function utilized in the SDLMA Gui models for selecting and
    displaying selection.
    """
    if role == QtGui.Qt.ItemDataRole.DisplayRole:
        return arr[index.row()].name

    if role == QtGui.Qt.ItemDataRole.DecorationRole:
        data = arr[index.row()]
        if hasattr(data, "selected") and arr[index.row()].selected:
            return tick


def row_count_proto(arr: list):
    """
    Default function utilized in the SDLMA Gui models for calculating the row
    count.
    """
    return len(arr)
