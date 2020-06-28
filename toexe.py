import cx_Freeze

# To create a installer, use "python toexe.py bdist_msi"

executables = [cx_Freeze.Executable('masterrace.py')]

cx_Freeze.setup(name = 'Master Race', options = {'build_exe': {'packages': ['pygame', 'time', 'random'], 'include_files': ['car.png', 'best_score.txt', 'gameIcon.png', 'music.wav', 'mv.png', 'fonds/', 'fonts/']}}, executables = executables)