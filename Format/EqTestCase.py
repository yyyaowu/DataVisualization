import unittest
from unittest import mock


class EqTestCase(unittest.TestCase):
    # 模拟地震数据
    def test_num_side(self):
        mock_value = mock.Mock(return_value='{"type":"Feature","properties":{"mag":1.2,"place":"11km NNE of North Nenana, Alaska"}}')
        self.assertEqual('{"type":"Feature","properties":{"mag":1.2,"place":"11km NNE of North Nenana, Alaska"}}', mock_value())

if __name__ == "__main__":
    unittest.main()