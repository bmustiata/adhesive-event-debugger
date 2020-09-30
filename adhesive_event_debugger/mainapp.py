import sys

from PySide2.QtWidgets import QApplication
from adhesive_event_debugger.ui.main_window import MainWindow

import oaas_simple
import oaas


oaas.register_server_provider(oaas_simple.OaasSimpleServer(port=9000))

oaas.serve()


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
