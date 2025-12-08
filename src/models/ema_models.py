from PySide6 import QtCore

from util.models import data_proto, row_count_proto


class SignalModel(QtCore.QAbstractListModel):
    def __init__(self, *args, signals=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = signals or []

    def data(self, index, role):
        return data_proto(self.signals, index, role)

    def rowCount(self, index):
        return row_count_proto(self.signals)


class EMAModel(QtCore.QAbstractListModel):
    def __init__(self, *args, measurements=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.measurements = measurements or []

    def data(self, index, role):
        return data_proto(self.measurements, index, role)

    def rowCount(self, index):
        return row_count_proto(self.measurements)
