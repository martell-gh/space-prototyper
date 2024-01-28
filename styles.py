class Theme:
    main = ''
    central = ''
    tree = ''
    add_comp = ""
    id_input = ""
    parent_input = ""
    name_input = ""

class LightTheme(Theme):
    main = """QMenuBar {
                                    background-color: #DFDFDF;
                                    color: #414141;
                                }"""
    central = """
                            QLineEdit { 
                                    border: 1px solid #A0A0A0;
                                    background-color: white;
                                    border-radius: 4px;
                                } 
                            QComboBox {
                                border: 1px solid #A0A0A0;
                                background-color: white;
                                border-radius: 4px;
                            }
                            """
    tree = """
                            QLineEdit {
                                color: black;
                                background-color: white;
                            }
                            QPushButton {
                                    background-color: #CECECE;
                                    color: black;
                                    width: 90px;
                                    height: 26px;
                                }
                                QPushButton::hover {
                                    background-color: #DFDFDF;
                                }
                                QPushButton::pressed {
                                    background-color: #8DF79E;
                                }

                                QLineEdit:disabled {
                                    background-color: #EEEEEE;
                                    color: darkgray;
                                    border: 1px solid #CCCCCC;
                                }
                            QLabel {
                                color: black;
                            }
                            QHeaderView::section {
                                            background-color: white;
                                            color: black;
                                            border-top-left-radius: 5px;
                                            border-top-right-radius: 5px;
                                            padding-left: 10px;
                                            border: 1px solid #A0A0A0;
                                        }
                                        QTreeWidget {
                                            border-radius: 5px;
                                            background-color: #DFDFDF;
                                            border: 1px solid #BBBBBB;
                                        }
                            QTreeWidget::item {
                                            border-bottom: 1px solid #A0A0A0;
                                            color: red;
                                            background-color: #F6F6F6;
                                        }
                                        """
    add_comp = ""
    id_input = ""
    parent_input = ""
    name_input = ""

class DarkTheme(Theme):
    main = """
                    QMenuBar {
                        background-color: #333;
                        color: #F0F0F0;
                    }
                    QMenuBar::item:selected {
                        background-color: #555;
                    }

                    QMenuBar::item:pressed {
                        background-color: #888;
                    }

                    """
    central = """
                                QWidget {
                                    background-color: "#1F1F24";
                                    color: white;
                                }
                                QMessageBox {
                                    color: white;
                                }
                                QComboBox {
                                    border: 1px solid #A0A0A0;
                            background-color: #171719;
                            border-radius: 4px;
                                }
                            """
    tree = """
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

                            """
    add_comp = """
                QPushButton {
                background-color: "#464966";
                color: white;
                border-radius: 2px;
                border-top-right-radius: 14px;
                border-bottom-left-radius: 14px;
                height: 30px;
            }
            QPushButton::hover {
                background-color: "#575B7F";
                color: white;
            }
            QPushButton::pressed {
                background-color: "#3E6C45";
                color: white;
            }"""

    id_input = """
                QLineEdit {
                    border: 1px solid #A0A0A0;
                    background-color: #171719;
                    border-radius: 4px;
                }
            """
    parent_input = """
                                QLineEdit {
                                    border: 1px solid #A0A0A0;
                                    background-color: #171719;
                                    border-radius: 4px;
                                }
                            """
    name_input = """
                                QLineEdit {
                                    border: 1px solid #A0A0A0;
                                    background-color: #171719;
                                    border-radius: 4px;
                                }
                            """
