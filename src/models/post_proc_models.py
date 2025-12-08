from PySide6 import QtCore

from util.models import data_proto, row_count_proto


class FRFModel(QtCore.QAbstractListModel):
    def __init__(self, *args, frfs=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.frfs = frfs or []

    def data(self, index, role):
        return data_proto(self.frfs, index, role)

    def rowCount(self, index: QtCore.QModelIndex):
        return row_count_proto(self.frfs)
