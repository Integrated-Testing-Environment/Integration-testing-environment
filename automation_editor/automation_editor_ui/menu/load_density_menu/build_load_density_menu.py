import webbrowser

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from automation_editor.utils.manager.package_manager.package_manager_class import package_manager
from automation_editor.utils.test_executor.load_density.load_density_process import \
    call_load_density_test, call_load_density_test_with_send, call_load_density_test_multi_file, \
    call_load_density_test_multi_file_and_send


def set_load_density_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.load_density_menu = ui_we_want_to_set.menu.addMenu("LoadDensity")
    ui_we_want_to_set.load_density_run_menu = ui_we_want_to_set.load_density_menu.addMenu("Run")
    # Run LoadDensity Script
    ui_we_want_to_set.run_load_density_action = QAction("Run LoadDensity Script")
    ui_we_want_to_set.run_load_density_action.triggered.connect(
        lambda: call_load_density_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(ui_we_want_to_set.run_load_density_action)
    # Run LoadDensity Script With Send
    ui_we_want_to_set.run_load_density_action_with_send = QAction("Run LoadDensity With Send")
    ui_we_want_to_set.run_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_load_density_action_with_send
    )
    # Run Multi LoadDensity Script
    ui_we_want_to_set.run_multi_load_density_action = QAction("Run Multi LoadDensity Script")
    ui_we_want_to_set.run_multi_load_density_action.triggered.connect(
        lambda: call_load_density_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action
    )
    # Run Multi LoadDensity Script With Send
    ui_we_want_to_set.run_multi_load_density_action_with_send = QAction("Run Multi LoadDensity Script With Send")
    ui_we_want_to_set.run_multi_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action_with_send
    )
    ui_we_want_to_set.load_density_help_menu = ui_we_want_to_set.load_density_menu.addMenu("HELP")
    # Open Doc
    ui_we_want_to_set.open_load_density_doc_action = QAction("Open LoadDensity Doc")
    ui_we_want_to_set.open_load_density_doc_action.triggered.connect(
        lambda: open_web_browser(
            "https://loaddensity.readthedocs.io/en/latest/"
        )
    )
    ui_we_want_to_set.load_density_help_menu.addAction(
        ui_we_want_to_set.open_load_density_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_load_density_github_action = QAction("Open LoadDensity GitHub")
    ui_we_want_to_set.open_load_density_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Intergration-Automation-Testing/LoadDensity"
        )
    )
    ui_we_want_to_set.load_density_help_menu.addAction(
        ui_we_want_to_set.open_load_density_github_action
    )
    ui_we_want_to_set.load_density_project_menu = ui_we_want_to_set.load_density_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_load_density_project_action = QAction("Create LoadDensity Project")
    ui_we_want_to_set.create_load_density_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.load_density_project_menu.addAction(
        ui_we_want_to_set.create_load_density_project_action
    )


def open_web_browser(url: str):
    webbrowser.open(url=url)


def create_project():
    package = package_manager.installed_package_dict.get("je_load_density", None)
    if package is not None:
        package.create_project_dir()
