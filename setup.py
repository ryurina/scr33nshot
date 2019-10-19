from cx_Freeze import setup, Executable


setup(
    name = "system",
    version = "1",
    description = "system",
    executables = [Executable("main.py")],
)
