from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "ffmpeg-python", "future"]
options = {
    'build.exe': {
        'packages': packages,
    },
}

setup(
    name= "pyConverter",
    options = options,
    version = "1.0",
    description = "python video converter",
    executables = executables
)
