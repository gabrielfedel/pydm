from . import qtlib
QT_LIB = qtlib.QT_LIB
if QT_LIB == 'PyQt4':
    from PyQt4.QtCore import *
    #Crappy work around:  QItemSelection exists in QtGui for PyQt4 but QtCore for PyQt5.  We'll make it available in both.
    from PyQt4.QtGui import QItemSelection
elif QT_LIB == 'PyQt5':
    from PyQt5.QtCore import *