from PySide6 import QtCore

from util.models import data_proto, row_count_proto


class PyMAGuiChannel:
    def __init__(self, channel):
        self.channel = channel
        self.name = self.channel.name
        self.selected = False


class ChannelModel(QtCore.QAbstractListModel):
    def __init__(self, *args, channels=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.channels = channels or []

    def data(self, index, role):
        return data_proto(self.channels, index, role)

    def rowCount(self, index):
        return row_count_proto(self.channels)

    def get_selected_channels(self):
        sel_channels = []
        for gui_channel in self.channels:
            if gui_channel.selected:
                sel_channels.append(gui_channel)
        return sel_channels
