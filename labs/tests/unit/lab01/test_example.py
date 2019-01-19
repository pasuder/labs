import mock
import unittest

from labs.lab01 import example as l1_example


class TestObject(unittest.TestCase):

    def setUp(self):
        self.mocked_param = mock.Mock()
        self.tested_object = l1_example.Object(self.mocked_param)

    def test_str(self):
        self.assertEqual(str(self.tested_object),
                         "Object: %s" % self.mocked_param)

    def test_repr(self):
        self.assertEqual(repr(self.tested_object),
                         "<Object: __private_field=%s>" %
                         self.mocked_param)

    def test_hash(self):
        self.assertEqual(hash(self.tested_object),
                         hash(self.mocked_param))

    def test_bool(self):
        self.assertEqual(bool(self.tested_object),
                         bool(self.mocked_param))


class TestDynamicObject(unittest.TestCase):

    def setUp(self):
        self.tested_object = l1_example.DynamicObject()

    def test_attr(self):
        mocked_attr = mock.Mock()
        self.tested_object.attr = mocked_attr
        self.assertEqual(self.tested_object.attr, mocked_attr)
        del self.tested_object.attr
        self.assertRaises(ValueError, self.tested_object.attr)


if __name__ == '__main__':
    unittest.main()
