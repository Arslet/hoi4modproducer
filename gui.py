import enaml
from enaml.qt.qt_application import QtApplication

with enaml.imports():
    from view import Main

app = QtApplication()
view = Main()
view.show()
app.start()