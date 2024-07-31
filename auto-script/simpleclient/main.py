# Copyright (C) 2020 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec())
