from typing import List

from PySide6.QtCore import QPoint, Signal
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget

from pycad.ComponentLayers import LayerModel
from pycad.Drawable import Drawable
from pycad.Plugin import PluginInterface

class PycadCoreLinePlugin(PluginInterface):
  
    class Line(Drawable):
        changed = Signal(object)  # Define a custom signal with a generic object type
        finished = Signal(bool)  # Define a custom signal with a generic object type
        points: List[QPoint] = []
        moving_point: QPoint = None
        max_points: int = 2

        def __init__(self):
            super(Drawable, self).__init__()
            pass

        def push(self, point: QPoint):
            self.points.append(point)

        def is_finished(self) -> bool:
            return len(self.points) == 2

        def temp(self, point: QPoint):
            self.moving_point = point

        def draw(self, painter: QPainter):
            painter.drawLine(self.start_point.x(), self.start_point.y(), self.end_point.x(), self.end_point.y())
            pass
    _instance = None

    @staticmethod
    def get_instance() -> 'PycadCoreLinePlugin':
        if PycadCoreLinePlugin._instance is None:
            PycadCoreLinePlugin._instance=PycadCoreLinePlugin()
        return PycadCoreLinePlugin._instance
    
    def destroy_ui(self, element: QWidget):
        pass

    def create_drawable(self, layer: LayerModel, start_point: QPoint) -> Drawable:
        return Line()

  
    def modify_drawable(self, layer: LayerModel, new_point: QPoint) -> Drawable:
        pass
