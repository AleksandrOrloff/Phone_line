#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Oct  5 14:17:57 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import control_rng
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.State = State = 0
        self.Band = Band = 0
        self.Attenuation = Attenuation = 0

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'RNG')
        self.top_layout.addWidget(self.tabs)
        self._State_options = (0, 1, )
        self._State_labels = ('OFF', 'ON', )
        self._State_group_box = Qt.QGroupBox("State")
        self._State_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._State_button_group = variable_chooser_button_group()
        self._State_group_box.setLayout(self._State_box)
        for i, label in enumerate(self._State_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._State_box.addWidget(radio_button)
        	self._State_button_group.addButton(radio_button, i)
        self._State_callback = lambda i: Qt.QMetaObject.invokeMethod(self._State_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._State_options.index(i)))
        self._State_callback(self.State)
        self._State_button_group.buttonClicked[int].connect(
        	lambda i: self.set_State(self._State_options[i]))
        self.tabs_grid_layout_0.addWidget(self._State_group_box, 1, 0, 1, 1)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._Band_options = (0, 1, 2, )
        self._Band_labels = ('FULL_BAND', 'HALF_BAND', 'OUT_OF_BAND', )
        self._Band_tool_bar = Qt.QToolBar(self)
        self._Band_tool_bar.addWidget(Qt.QLabel("Band"+": "))
        self._Band_combo_box = Qt.QComboBox()
        self._Band_tool_bar.addWidget(self._Band_combo_box)
        for label in self._Band_labels: self._Band_combo_box.addItem(label)
        self._Band_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Band_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Band_options.index(i)))
        self._Band_callback(self.Band)
        self._Band_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_Band(self._Band_options[i]))
        self.tabs_grid_layout_0.addWidget(self._Band_tool_bar, 3, 0, 1, 1)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._Attenuation_range = Range(0, 10, 1, 0, 200)
        self._Attenuation_win = RangeWidget(self._Attenuation_range, self.set_Attenuation, "Attenuation", "counter_slider", int)
        self.tabs_grid_layout_0.addWidget(self._Attenuation_win, 0, 0, 1, 2)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,2)]
        self.control_rng_control_rng_py_0 = control_rng.control_rng_py('/dev/ttyACM1', State, Attenuation, Band)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_State(self):
        return self.State

    def set_State(self, State):
        self.State = State
        self._State_callback(self.State)
        self.control_rng_control_rng_py_0.set_state(self.State)

    def get_Band(self):
        return self.Band

    def set_Band(self, Band):
        self.Band = Band
        self._Band_callback(self.Band)
        self.control_rng_control_rng_py_0.set_band(self.Band)

    def get_Attenuation(self):
        return self.Attenuation

    def set_Attenuation(self, Attenuation):
        self.Attenuation = Attenuation
        self.control_rng_control_rng_py_0.set_attenuation(self.Attenuation)


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
