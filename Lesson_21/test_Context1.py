from unittest import TestCase
import Context

class TestContext(TestCase):

    def test_enter(self):
        self.assertEqual(print(open('text.txt', 'r')), print(Context.File('text.txt', 'r')))

    def test_logging(self):
        with Context.File('text.txt', 'r') as f:
            print(f.read())
            raise FileExistsError
        log = open('logging.txt', 'r')
        self.assertEqual(log.readline(), "<class 'FileExistsError'>\n")

    def test_exit(self):
        with Context.File('text.txt', 'r') as f:
            print(f.read())
        self.assertEqual(f.closed, True)

    def test_xcounter(self):
        self.assertEqual(Context.File.counter, 3)

    def test_Filenotfound(self):
        with self.assertRaises(FileNotFoundError):
            with Context.File('tet.txt', 'r') as f:
                print(f.read())





