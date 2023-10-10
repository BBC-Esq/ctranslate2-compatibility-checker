import sys
from PySide6.QtWidgets import (
    QApplication, 
    QTableWidget, 
    QTableWidgetItem, 
    QVBoxLayout, 
    QWidget
)
import ctranslate2

def get_compatibility():
    compatibility = {
        "CPU": ctranslate2.get_supported_compute_types("cpu"),
        "GPU": ctranslate2.get_supported_compute_types("cuda")
    }
    return compatibility

def display_table(compatibility):
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    widget = QWidget()
    table = QTableWidget()

    compute_types = sorted(set(compute_type for types in compatibility.values() for compute_type in types))
    table.setColumnCount(len(compatibility))
    table.setRowCount(len(compute_types))
    table.setHorizontalHeaderLabels(compatibility.keys())
    table.setVerticalHeaderLabels(compute_types)

    for row, compute_type in enumerate(compute_types):
        for column, (device, types) in enumerate(compatibility.items()):
            table.setItem(row, column, QTableWidgetItem("✅" if compute_type in types else ""))

    table.resizeColumnsToContents()
    table.resizeRowsToContents()

    layout = QVBoxLayout()
    layout.addWidget(table)
    widget.setLayout(layout)
    widget.resize(160, 205)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    compatibility = get_compatibility()
    display_table(compatibility)
