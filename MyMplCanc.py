from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCavans

class MtMplCanv(FigureCavans):
    def __init__(self, figure, parent = None):
        self.figure = figure
        FigureCavans.__init__(self, self.figure)
        FigureCavans.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCavans.updateGeometry(self)
