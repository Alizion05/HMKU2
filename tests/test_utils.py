import unittest
import os
import xml.etree.ElementTree as ET
from src.utils import load_config
from src.exceptions import ConfigError

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Создаем временный XML файл конфигурации для тестирования
        self.config_path = "test_config.xml"
        self.valid_config = {
    		"graphviz_path": r"C:\Program Files\Graphviz\bin\dot.exe",
    		"repo_path": r"C:\Users\Noxen\KY\DZ2\HM2KU-main\my_repo",
    		"output_path": "test_output.png",
    		"since_date": "2023-11-30"
	}

        self.create_xml_config(self.valid_config)

    def create_xml_config(self, config_data):
        """Вспомогательная функция для создания XML-файла конфигурации."""
        root = ET.Element("config")
        for key, value in config_data.items():
            child = ET.SubElement(root, key)
            child.text = value
        tree = ET.ElementTree(root)
        tree.write(self.config_path, encoding="utf-8", xml_declaration=True)

    def tearDown(self):
        # Удаляем временный файл конфигурации
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        if os.path.exists("test_output.png"):
            os.remove("test_output.png")

    def test_load_config_valid(self):
        # Тестируем загрузку корректной конфигурации
        config = load_config(self.config_path)
        self.assertEqual(config, self.valid_config)

    def test_load_config_file_not_found(self):
        # Тестируем случай, когда файл конфигурации не найден
        with self.assertRaises(ConfigError):
            load_config("nonexistent_config.xml")

    def test_load_config_invalid_xml(self):
        # Тестируем случай, когда файл конфигурации содержит некорректный XML
        with open(self.config_path, 'w') as f:
            f.write("invalid xml")
        with self.assertRaises(ConfigError):
            load_config(self.config_path)

    def test_load_config_missing_keys(self):
        # Тестируем случай, когда в конфигурации отсутствуют обязательные ключи
        invalid_config = {"repo_path": "some/path"}
        self.create_xml_config(invalid_config)
        with self.assertRaises(ConfigError):
            load_config(self.config_path)

    def test_load_config_repo_path_not_exist(self):
        # Тестируем случай, когда путь к репозиторию не существует
        invalid_config = self.valid_config.copy()
        invalid_config["repo_path"] = "nonexistent/path"
        self.create_xml_config(invalid_config)
        with self.assertRaises(ConfigError):
            load_config(self.config_path)

    def test_load_config_graphviz_path_not_exist(self):
        # Тестируем случай, когда путь к Graphviz не существует
        invalid_config = self.valid_config.copy()
        invalid_config["graphviz_path"] = "nonexistent/path"
        self.create_xml_config(invalid_config)
        with self.assertRaises(ConfigError):
            load_config(self.config_path)

    def test_load_config_invalid_date_format(self):
        # Тестируем случай, когда формат даты некорректен
        invalid_config = self.valid_config.copy()
        invalid_config["since_date"] = "invalid-date"
        self.create_xml_config(invalid_config)
        with self.assertRaises(ConfigError):
            load_config(self.config_path)
