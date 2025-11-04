from PySide6 import QtGui

tick = QtGui.QColor("green")


def data_proto(arr, index, role):
    if role == QtGui.Qt.ItemDataRole.DisplayRole:
        return arr[index.row()].name

    if role == QtGui.Qt.ItemDataRole.DecorationRole:
        data = arr[index.row()]
        if hasattr(data, "selected") and arr[index.row()].selected:
            return tick


def row_count_proto(arr):
    return len(arr)
