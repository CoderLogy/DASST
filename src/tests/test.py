import unittest
from unittest.mock import patch,MagicMock
from src.core import System_Usage

class Test_Usage(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sys_usage = System_Usage()
    @patch('psutil.virtual_memory')
    def test_memory_info(self,mock_memory):
        mock_memory.return_value = MagicMock(
            total=8 * 1024**3,
            available=4 * 1024**3,
            free=2 * 1024**3,
            percent=50.0,
            used=4 * 1024**3
        )
        
        expected_result = {
            "total": 8,
            "available": 4,
            "free": 2,
            "percent": 50.0,
            "used": 4
        }
        
        result = self.sys_usage.memory_info(unit='GB')
        self.assertEqual(result, expected_result)