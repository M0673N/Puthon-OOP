import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_cat_eat__expect_increased_size_by_1(self):
        self.cat.eat()
        expected_result = 1
        actual_result = self.cat.size
        self.assertEqual(expected_result, actual_result)

    def test_cat_eat__expected_cat_fed_to_be_True(self):
        self.cat.eat()
        expected_result = True
        actual_result = self.cat.fed
        self.assertEqual(expected_result, actual_result)

    def test_cat_eat__when_fed__expect_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep__when_not_fed__expect_exception(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_sleep__when_sleepy_expect_not_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        expected_result = False
        actual_result = self.cat.sleepy
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
