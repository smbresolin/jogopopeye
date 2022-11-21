import cx_freeze

executables = [cx_freeze.Executable(script="jogo.py", icon="assets/icone.ico")]
cx_freeze.setup(name="Popeye faminto!", options={"build.exe":{"packages":["pygame"],"include_files":["assets"]}}, executables = executables)