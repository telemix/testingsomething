from ._anvil_designer import Form2Template
from anvil import *

class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    data = [
      {"My Label 1": TextBox()},
      {"My label 2": CheckBox()}
    ]

    row_count = 0
    for d in data:
      for k,v in d.items():
        l = Label(text=k)
        self.grid_panel_1.add_component(l, row=f"row{row_count}", width_xs=6)
        self.grid_panel_1.add_component(v, row=f"row{row_count}", width_xs=6)
      
      
      