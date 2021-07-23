import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.list_to_test = IntegerList()

    def test_init__ints_only_and_then_ints_and_string__expect_pass(self):
        list_to_test = IntegerList(1, 2, 3, 4, 5)
        expected_result = 5
        actual_result = len([x for x in list_to_test.get_data() if type(x) == int])
        self.assertEqual(expected_result, actual_result)

        list_to_test = IntegerList(1, 2, "a", 4, "b")
        expected_result = 3
        actual_result = len([x for x in list_to_test.get_data() if type(x) == int])
        self.assertEqual(expected_result, actual_result)

    def test_add__int_and_then_str__expect_pass(self):
        expected_result = [1]
        actual_result = self.list_to_test.add(1)
        self.assertEqual(expected_result, actual_result)

        with self.assertRaises(ValueError):
            self.list_to_test.add("str")

    def test_remove_index__correct_and_then_incorrect_index__expect_pass(self):
        self.list_to_test.add(1)
        expected_result = []
        actual_result = self.list_to_test.remove_index(0)
        self.assertEqual(expected_result, actual_result)

        with self.assertRaises(IndexError):
            self.list_to_test.remove_index(8)

        with self.assertRaises(IndexError):
            self.list_to_test.remove_index(-8)

    def test_get__correct_and_then_incorrect_index__expect_pass(self):
        self.list_to_test.add(1)
        self.list_to_test.get(0)
        expected_result = 1
        actual_result = self.list_to_test.get_data()[0]
        self.assertEqual(expected_result, actual_result)

        with self.assertRaises(IndexError):
            self.list_to_test.get(8)

    def test_insert__invalid_index_then_string__expect_pass(self):
        with self.assertRaises(IndexError):
            self.list_to_test.insert(8, 1)

        self.list_to_test.add(1)
        with self.assertRaises(ValueError):
            self.list_to_test.insert(0, "str")

    def test_get_biggest__expect_pass(self):
        list_to_test = IntegerList(1, 2, 3, 4, 5)
        expected_result = 5
        actual_result = list_to_test.get_biggest()
        self.assertEqual(expected_result, actual_result)

    def test_get_index__expect_pass(self):
        list_to_test = IntegerList(1, 2, 3, 4, 5)
        expected_result = 4
        actual_result = list_to_test.get_index(5)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
