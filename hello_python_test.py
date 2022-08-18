import io
import unittest
import unittest.mock

from hello_python import main


class Test(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_only_numbers(self):
        self.assert_stdout('Hello Python!\n')
        
 
if __name__ == '__main__':
    unittest.main()