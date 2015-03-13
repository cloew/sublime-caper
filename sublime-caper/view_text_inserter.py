
class ViewTextInserter:
    """ Helper class to add text to a sublime text view """
    
    def __init__(self, view, edit):
        """ Initialize the Inserter with the view and edit context to use """
        self.view = view
        self.edit = edit
        self.insertAt = 0
        
    def addLine(self, line=''):
        """ Add the given text as a line to the file """
        self.insertAt += self.view.insert(self.edit, self.insertAt, line + "\n")