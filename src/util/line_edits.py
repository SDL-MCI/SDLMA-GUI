from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLineEdit


def check_line_edits_valid(line_edits: list[QLineEdit]):
    for line_edit in line_edits:
        if not line_edit.hasAcceptableInput():
            return False
    return True


def set_line_edit_change_func(widget, func):
    line_edits = widget.findChildren(QLineEdit)
    for line_edit in line_edits:
        line_edit.textChanged.connect(func)
