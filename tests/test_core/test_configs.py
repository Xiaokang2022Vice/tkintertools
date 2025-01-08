# pylint: disable=all

import unittest
import unittest.mock

from tkintertools.core import configs


class TestEnv(unittest.TestCase):

    def test_reset(self) -> None:
        configs.Env.system = ""
        configs.Env.is_dark = False
        configs.Env.default_animation = False
        configs.Env.auto_update = False

        configs.Env.reset()

        self.assertEqual(configs.Env.system, configs.Env.get_default_system())
        self.assertFalse(configs.Env.is_dark)
        self.assertTrue(configs.Env.default_animation)
        self.assertTrue(configs.Env.auto_update)

    def test_get_default_system(self) -> None:
        with unittest.mock.patch('platform.system', return_value='Windows'):
            with unittest.mock.patch('platform.win32_ver', return_value=('10', '10.1.22000', 'multiprocessor Free')):
                self.assertEqual(configs.Env.get_default_system(), "Windows11")

        with unittest.mock.patch('platform.system', return_value='Windows'):
            with unittest.mock.patch('platform.win32_ver', return_value=('10', '10.0.19041', 'multiprocessor Free')):
                self.assertEqual(configs.Env.get_default_system(), "Windows10")

        with unittest.mock.patch('platform.system', return_value='Linux'):
            self.assertEqual(configs.Env.get_default_system(), "Linux")


class TestFont(unittest.TestCase):

    def test_reset(self) -> None:
        configs.Font.family = ""
        configs.Font.size = 0

        configs.Font.reset()

        self.assertEqual(configs.Font.family, configs.Font.get_default_family())
        self.assertEqual(configs.Font.size, -20)

    def test_get_default_family(self) -> None:
        with unittest.mock.patch('platform.system', return_value='Windows'):
            self.assertEqual(configs.Font.get_default_family(), "Microsoft YaHei")

        with unittest.mock.patch('platform.system', return_value='Darwin'):
            self.assertEqual(configs.Font.get_default_family(), "PingFang SC")

        with unittest.mock.patch('platform.system', return_value='Linux'):
            self.assertEqual(configs.Font.get_default_family(), "Noto Sans")


if __name__ == "__main__":
    unittest.main()