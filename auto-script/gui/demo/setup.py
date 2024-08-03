from setuptools import setup

APP = ['mainWindow.py']
#自写模块放在DATA_FILES列表中
DATA_FILES = ['ui_MainWindow.py','wyy_click_play.py','MainWindow.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PySide6'],
}

# python setup.py py2app -A 打包命令
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)