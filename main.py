from interface import *
from table import *

app = None
app = Interface()
app.run()

def search_command():
    table = None
    table = Table()
    table.run()


app.btnBuscar.configure(command=search_command)