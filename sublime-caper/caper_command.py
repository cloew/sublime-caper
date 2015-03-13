import sublime, sublime_plugin

import json
import subprocess

class CaperCommand(sublime_plugin.TextCommand):
    """ Command to run Caper and retrieve the results """
    PYTHON_PATH = 'C:/Python34/python.exe'
    CAPER_PATH = 'C:/dev/KaoTessur/Caper/src/main.py'

    def run(self, edit):
        """ Run the command """
        filename = self.view.file_name()
        line = self.view.rowcol(self.view.sel()[0].begin())[0]+1

        args = [self.PYTHON_PATH, self.CAPER_PATH, filename, '-l', str(line), '-e', self.PYTHON_PATH]
        results = subprocess.check_output(args)
        results = results.decode("utf-8")
        print(json.loads(results))