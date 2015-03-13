import sublime, sublime_plugin

import json
import subprocess

from .view_text_inserter import ViewTextInserter

class CaperCommand(sublime_plugin.TextCommand):
    """ Command to run Caper and retrieve the results """
    PYTHON_PATH = 'C:/Python34/python.exe'
    CAPER_PATH = 'C:/dev/KaoTessur/Caper/src/main.py'

    def run(self, edit):
        """ Run the command """
        results = self.getResults()
        self.displayResults(results, edit)

    def getResults(self):
        filename = self.view.file_name()
        line = self.view.rowcol(self.view.sel()[0].begin())[0]+1

        args = [self.PYTHON_PATH, self.CAPER_PATH, filename, '-l', str(line), '-e', self.PYTHON_PATH]
        results = subprocess.check_output(args)
        results = results.decode("utf-8")
        return json.loads(results)

    def displayResults(self, results, edit):
        """ Display the given results """
        resultsView = self.view.window().new_file()
        inserter = ViewTextInserter(resultsView, edit)

        self.insertVariableStates(inserter, results['states'])
        self.insertReturnResults(inserter, results['returned'])
        resultsView.set_read_only(True)
        
    def insertVariableStates(self, inserter, states):
        """ Insert the variable states during the caper function execution """
        for state in states:
            inserter.addLine("Line {0}".format(state['lineNumber']))
            variables = state['variables']
            for varName in variables:
                inserter.addLine("{0} = {1}".format(varName, variables[varName]))
            inserter.addLine()

    def insertReturnResults(self, inserter, returned):
        """ Insert the return results from the caper function execution """
        inserter.addLine("Line {0}".format(returned['lineNumber']))
        inserter.addLine("returned {0}".format(returned['value']))


    def addLine(self, view, line):
        """ Adds the given line text to the view """
        self.view.insert()