class Interfaz():
    def __init__(self):
        self.actual_page = ""
        self.actual_widget = ""
        self.allwidget = []
    def addWidgets(self, widgets):
        self.allwidget.append(widgets)
    def initialWidget(self):
        self.allwidget[0].pack()
        self.actual_widget = self.allwidget[0]
        for widget in self.allwidget[0:]:
            widget.unpack()

    def toWidget(self,numWidget):
        self.allwidget[numWidget].pack()
        Widgets = self.allwidget
        Widgets.pop(numWidget)
        for widget in Widgets:
            widget.unpack()
    
