
import os
import sys

from epyk.core.Page import Report

template_path = 'reports'
sys.path.append(template_path)

# The path to the Vue App
out_path = r".\vue-apps"
folder_target = r"src\views"


def refresh(view_name):
  """
  Description:
  ------------
  This will transpile only the selected report.
  Transpilation will generate HTML content from the python code using Epyk framework

  Attributes:
  ----------
  :param view_name:
  """
  mod = __import__(view_name)
  if hasattr(mod, 'get_page'):
    page = Report()
    mod.get_page(page)
    page.outs.publish(server="vue", app_path=out_path, module="MyModule", selector='mymodule', target_folder=folder_target, auto_route=True)
  else:
    mod.page.outs.publish(server="vue", app_path=out_path, module="MyModule", selector='mymodule', target_folder=folder_target, auto_route=True)


if __name__ == '__main__':
  """
  This will transpile all the reports in the reports folder
  """
  for report in os.listdir(template_path):
    if report.endswith(".py"):
      view_name = report[:-3]
      mod = __import__(view_name)
    if hasattr(mod, 'get_page'):
      page = Report()
      mod.get_page(page)
      page.outs.publish(server="vue", app_path=out_path, module=view_name, selector=view_name.lower(), target_folder=folder_target, auto_route=True)
    else:
      mod.page.outs.publish(server="vue", app_path=out_path, module=view_name, selector=view_name.lower(), target_folder=folder_target, auto_route=True)
