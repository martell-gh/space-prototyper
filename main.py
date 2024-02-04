import sys

from ruamel.yaml import YAML

from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTreeWidget, QPushButton, QHBoxLayout, \
    QLineEdit, QTreeWidgetItem, QMessageBox, QInputDialog, QLabel, QSizePolicy, QComboBox, QFileDialog, \
    QAction, QShortcut
from constants import COMPONENT_TYPES, COMPONENT_PROPERTIES
from styles import *

class DynamicYMLApp(QMainWindow):
    def __init__(self):
        super().__init__()
        types = ['entity', 'null']

        self.setWindowTitle('Space Prototyper')
        app_icon = QIcon(':/icon.ico')
        self.setWindowIcon(app_icon)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.type_label = QLabel('Type:')
        self.type_combo = QComboBox()
        self.type_combo.addItems(types)
        self.type_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type_combo)

        self.layout.addLayout(type_layout)

        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Prototype name")
        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)

        self.layout.addLayout(name_layout)

        self.id_label = QLabel('ID:')
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Prototype ID")
        id_layout = QHBoxLayout()
        id_layout.addWidget(self.id_label)
        id_layout.addWidget(self.id_input)

        self.layout.addLayout(id_layout)

        self.optional_label = QLabel('Optional:')
        self.layout.addWidget(self.optional_label)
        self.parent_label = QLabel('Parent:')
        self.parent_input = QLineEdit()
        self.parent_input.setPlaceholderText("Parent of prototype (OPTIONAL)")

        parent_layout = QHBoxLayout()
        parent_layout.addWidget(self.parent_label)
        parent_layout.addWidget(self.parent_input)

        self.layout.addLayout(parent_layout)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Components"])
        self.layout.addWidget(self.tree)

        self.add_component_button = QPushButton('+ Add Component')
        self.add_component_button.clicked.connect(self.add_component)
        self.layout.addWidget(self.add_component_button)

        self.author_label = QLabel('Developed by Ogunefu')

        file_menu = self.menuBar().addMenu('File')
        theme_menu = self.menuBar().addMenu('Theme')
        self.tree.setStyleSheet("""
                    QPushButton {
                        background-color: #464966;
                        color: white;
                        width: 90px;
                        height: 26px;
                    }
                    QPushButton::hover {
                        background-color: "#575B7F";
                        color: white;
                    }
                    QPushButton::pressed {
                        background-color: "#3E6C45";
                        color: white;
                    }
                QLineEdit {
                        border: 1px solid #A0A0A0;
                        background-color: #171719;
                        border-radius: 4px;
                    }
                    QLineEdit:disabled {
                        background-color: #2F2F33;
                        color: darkgray;
                        border: 1px solid gray;
                    }
                            QHeaderView::section {
                                background-color: "#25252A";
                                color: white;
                                border-top-left-radius: 5px;
                                border-top-right-radius: 5px;
                                padding-left: 10px;
                                border: 1px solid #A0A0A0;
                            }
                            QTreeWidget {
                                border-radius: 5px;
                                background-color: #121214;
                                border: 1px solid #A0A0A0;
                            }
                            QTreeWidget::item {
                                border-bottom: 1px solid #A0A0A0;

                            }

                        """)
        self.set_theme(DarkTheme)

        new_file_action = QAction('New File', self)
        new_file_action.triggered.connect(self.clear_values)
        file_menu.addAction(new_file_action)

        save_action = QAction('Save as YML', self)
        save_action.triggered.connect(self.save_as_yml)
        file_menu.addAction(save_action)

        shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        shortcut.activated.connect(self.save_as_yml)

        load_action = QAction('Load YML', self)
        load_action.triggered.connect(self.load_yml_file)
        file_menu.addAction(load_action)

        light_theme = QAction('Light theme', self)
        light_theme.triggered.connect(lambda: self.set_theme(LightTheme))
        theme_menu.addAction(light_theme)

        dark_theme = QAction('Dark theme', self)
        dark_theme.triggered.connect(lambda: self.set_theme(DarkTheme))
        theme_menu.addAction(dark_theme)

        theme_menu = self.menuBar().addMenu('Credits')

        credits_action = QAction('Show Credits', self)
        credits_action.triggered.connect(self.show_credits)

        theme_menu.addAction(credits_action)

    def show_credits(self):
        text = (
            "Developer:\n"
            "Martell.\n\n"
            "Discord - .martell\n\n"
            "Special thanks:\n"
            "DL94\n"
            "your_mommy\n"
            "_Krypton_"
        )

        msg = QMessageBox()
        msg.setWindowTitle('Credits')
        msg.setText(text)

        msg.setStyleSheet("QLabel { font-size: 26px; }")

        msg.exec_()

    def set_theme(self, theme: Theme):
        self.setStyleSheet(theme.main)
        self.central_widget.setStyleSheet(theme.central)
        self.tree.setStyleSheet(theme.tree)
        self.add_component_button.setStyleSheet(theme.add_comp)
        self.id_input.setStyleSheet(theme.id_input)
        self.parent_input.setStyleSheet(theme.parent_input)
        self.name_input.setStyleSheet(theme.name_input)

    def clear_values(self):
        confirmation = QMessageBox.question(
            self, 'Confirm New File', 'Are you sure you want to create a new file? All unsaved data will be lost.',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            self.type_combo.setCurrentIndex(0)
            self.name_input.clear()
            self.parent_input.clear()
            self.id_input.clear()
            self.tree.clear()
            return True
        else:
            return False

    def add_component(self):
        sorted_types = sorted(COMPONENT_TYPES, key = lambda x: (x != "Empty", x))

        component_type, ok = QInputDialog.getItem(self, "Select Component Type", "Choose a component type:",
                                                  sorted_types, 0, False)

        if ok and component_type:

            if component_type == "Empty":
                item = CustomTreeWidgetItem(self.tree, isComponent = True)
            else:
                item = CustomTreeWidgetItem(self.tree, isComponent = True, name = component_type)

            item.value_input.setEnabled(False)

            self.tree.addTopLevelItem(item)

    def save_as_yml(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save YML', '', 'YML Files (*.yml)', options = options)
        if file_name:
            try:
                components = []
                for i in range(self.tree.topLevelItemCount()):
                    top_item = self.tree.topLevelItem(i)
                    component = self.get_item_data(top_item)
                    components.append({'data': component, 'level': top_item.level})

                with open(file_name, 'w') as file:
                    file.write(f'- type: {self.type_combo.itemText(self.type_combo.currentIndex())}\n')
                    file.write(f'  name: {self.name_input.text()}\n')
                    if self.parent_input.text():
                        file.write(f'  parent: {self.parent_input.text()}\n')
                    file.write(f'  id: {self.id_input.text()}\n')
                    if components:
                        file.write('  components:\n')
                        for component in components:
                            file.write(self.dict_to_yaml(component['data'], indent_level = component['level']))

                QMessageBox.information(self, 'Success', f'YML file "{file_name}" saved successfully!')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error occurred while saving the file: {str(e)}')

    def get_item_data(self, item, indent_level=0):
        data = {}
        name = item.name_input.text()
        value = item.value_input.text()

        if item.isComponent:
            data['type'] = name
        else:
            if value:
                data[name] = value

        children_count = item.childCount()
        if children_count > 0:
            children_data = {}
            for i in range(children_count):
                child = item.child(i)
                child_data = self.get_item_data(child, indent_level + 1)
                children_data.update(child_data)
            if children_data:
                if 'type' in data:
                    data.update(children_data)
                else:
                    data[name] = children_data

        return self.indent_data(data, indent_level)

    def indent_data(self, data, indent_level):
        indented_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                indented_value = self.indent_data(value, indent_level + 1)
                indented_data[key] = indented_value
            else:
                indented_data[key] = value
        return indented_data

    def dict_to_yaml(self, data, indent_level):
        def represent(data, indent=0, level=1):
            yaml_str = ''
            for key, value in data.items():
                if isinstance(value, dict):
                    yaml_str += '  ' * indent + f"{key}:\n"
                    yaml_str += represent(value, indent + 1, level = level + 1)
                else:
                    yaml_str += '  ' * indent + f"{key.replace('  type:', '- type:')}: {value}\n"
            return yaml_str.replace('  type:', '- type:')

        return represent(data, indent_level)

    def load_yml_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open YML File', '', 'YAML Files (*.yml *.yaml)')
        if file_path:
            try:
                self.text = ''
                with open(file_path, 'r') as file:
                    self.text = file.read()
                    self.text = self.text.replace("!", "LVOSK").replace('  - LVOSK', '    LVOSK')\
                        .replace('    - ', '      LTIRE_').replace('{','OPNSKOB').replace('}','CLSESKOB')

                with open(file_path, 'r') as file:
                    yaml = YAML()
                    yaml.preserve_quotes = True
                    yml_data = yaml.load(self.text)

                    prototypes = self.extract_prototypes(yml_data)
                    if prototypes:
                        chosen_prototype, ok = QInputDialog.getItem(self, "Choose Prototype",
                                                                    "Select a prototype to load:",
                                                                    prototypes.keys(), 0, False)
                        if ok and chosen_prototype:
                            if self.clear_values():
                                chosen_data = prototypes[chosen_prototype]
                                self.apply_yml_data(chosen_data)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error occurred while loading the file: {str(e)}')
                print(e)

    def extract_prototypes(self, yml_data):
        prototypes = {}
        current_prototype = []
        for item in yml_data:
            if 'type' in item and item['type']:
                if current_prototype:
                    prototypes[current_prototype[0]['id']] = current_prototype
                    current_prototype = []
                current_prototype.append(item)
            else:
                current_prototype.append(item)
        if current_prototype:
            prototypes[current_prototype[0]['id']] = current_prototype
        return prototypes

    def apply_yml_data(self, yml_data):
        if isinstance(yml_data, list):
            for item in yml_data:
                self.apply_yml_data(item)
        else:
            type_value = yml_data.get('type', '')
            name_value = yml_data.get('name', '')
            parent_value = yml_data.get('parent', '')
            id_value = yml_data.get('id', '')

            self.type_combo.setCurrentText(type_value)
            self.name_input.setText(name_value)
            self.parent_input.setText(parent_value)
            self.id_input.setText(id_value)

            components = yml_data.get('components', [])
            for component in components:
                self.apply_component(component, self.tree.invisibleRootItem())

    def apply_component(self, component, parent_item):
        component_type = component.get('type', '')
        child_item = CustomTreeWidgetItem(parent_item, isComponent = True, name = component_type)

        if 'components' in component:
            sub_components = component['components']
            for sub_component in sub_components:
                self.apply_component(sub_component, child_item)

        self.apply_properties(component, child_item)
        parent_item.addChild(child_item)
        child_item.update_value_input_state()

    def apply_properties(self, component, item):
        for key, value in component.items():
            if key != 'type' and key != 'components':
                if isinstance(value, dict):
                    sub_item = CustomTreeWidgetItem(item, isComponent = False, name = key.replace('LVOSK', '!')
                                                    .replace('LTIRE_', '- '))
                    self.apply_properties(value, sub_item)
                    item.addChild(sub_item)
                else:
                    sub_item = CustomTreeWidgetItem(item, isComponent = False, name = key.replace('LVOSK', '!')
                                                    .replace('LTIRE_', '- '))
                    if value is not None:
                        sub_item.value_input.setText(str(value).replace('LVOSK', '!').replace('OPNSKOB','{')
                                                     .replace('CLSESKOB', '}').replace('LTIRE_', '- '))
                    item.addChild(sub_item)

        self.update_child_value_inputs(item)

    def update_child_value_inputs(self, item):
        item.update_value_input_state()
        for i in range(item.childCount()):
            child = item.child(i)
            self.update_child_value_inputs(child)


class CustomTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent=None, isComponent=False, name='', level=2):
        super().__init__(parent)

        self.isComponent = isComponent

        self.level = level
        self.tree_widget_item = QWidget()
        layout = QHBoxLayout()

        self.name_label = QLabel('Component name:')
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)
        self.name_input.setText(name)

        self.value_label = QLabel('Value:')

        self.value_input = QLineEdit()

        if not self.isComponent:
            layout.addWidget(self.value_label)
            layout.addWidget(self.value_input)
            self.name_label.setText('Datafield variable name:')

        self.add_child_button = QPushButton('+')
        self.add_child_button.setStyleSheet("""
        QPushButton {
                border-radius: 2px;
                border-bottom-left-radius: 14px;
            }""")
        self.add_child_button.clicked.connect(self.add_child)
        layout.addWidget(self.add_child_button)

        self.remove_button = QPushButton('-')
        self.remove_button.setStyleSheet("""
        QPushButton {
                border-radius: 2px;
                border-top-right-radius: 14px;
            }
            """)
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

        self.tree_widget_item.setLayout(layout)
        self.treeWidget().setItemWidget(self, 0, self.tree_widget_item)
        self.update_value_input_state()

    def add_child(self):
        try:
            child_item = CustomTreeWidgetItem(self, level = self.level + 1)

            component_properties = next((item[self.name_input.text()] for item in COMPONENT_PROPERTIES if
                                         self.name_input.text() in item), None)

            if component_properties:
                component_prop, ok = QInputDialog.getItem(self.treeWidget().window(), "Select Component Property",
                                                          "Choose a component property:", sorted(component_properties),
                                                          0, False)

                if ok and component_prop:
                    child_item.name_input.setText(component_prop)
            else:
                pass

            self.addChild(child_item)
            self.update_value_input_state()
        except Exception as e:
            print(e)

    def remove_item(self):
        reply = QMessageBox.question(
            self.treeWidget(), 'Delete Confirmation',
            'Are you sure you want to delete this component and its children?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            parent = self.parent()
            if parent:
                parent.removeChild(self)
                if parent.childCount() == 0:
                    parent.update_value_input_state()
            else:
                self.treeWidget().invisibleRootItem().removeChild(self)

    def update_value_input_state(self):
        has_children = self.childCount() > 0
        self.value_input.setEnabled(not has_children)

def main():
    app = QApplication(sys.argv)
    window = DynamicYMLApp()
    window.setGeometry(200, 200, 400, 300)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
