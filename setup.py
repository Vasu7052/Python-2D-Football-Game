import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Vasu\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Vasu\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["images/racecar.png"]}},
    executables = executables ,

    )