# https://stackoverflow.com/questions/9374063/remove-all-items-from-a-layout/9383780#9383780
def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())
