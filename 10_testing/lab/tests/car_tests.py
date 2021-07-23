import unittest
from project.car_manager import Car


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "X5", 5, 100)

    def test_car_init__expect_to_work(self):
        expected_result = ("BMW", "X5", 5, 100)
        actual_result = (self.car.make, self.car.model, self.car.fuel_consumption, self.car.fuel_capacity)
        self.assertEqual(expected_result, actual_result)

    def test_car_refuel__negative_fuel__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-55)

    def test_car_refuel__0_fuel__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_car_refuel__correct_fuel__expect_to_increase_fuel_with_given_amount(self):
        self.car.refuel(50)
        expected_result = 50
        actual_result = self.car.fuel_amount
        self.assertEqual(expected_result, actual_result)

    def test_car_refuel__more_fuel_than_capacity__expect_refuel_up_to_capacity(self):
        self.car.refuel(555)
        expected_result = 100
        actual_result = self.car.fuel_amount
        self.assertEqual(expected_result, actual_result)

    def test_car_drive__correct_amount__expect_reduce_fuel_amount_correctly(self):
        self.car.refuel(6)
        self.car.drive(100)
        expected_result = 1
        actual_result = self.car.fuel_amount
        self.assertEqual(expected_result, actual_result)

    def test_car_drive__incorrect_amount__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.drive(10)

    def test_car_make_setter__correct_value__expect_make_to_be_set(self):
        self.car.make = "VW"
        expected_result = "VW"
        actual_result = self.car.make
        self.assertEqual(expected_result, actual_result)

    def test_car_make_setter__none__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.make = None

    def test_car_model_setter__correct_value__expect_make_to_be_set(self):
        self.car.model = "X7"
        expected_result = "X7"
        actual_result = self.car.model
        self.assertEqual(expected_result, actual_result)

    def test_car_model_setter__none__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.model = None

    def test_car_fuel_consumption_setter__correct_value__expect_make_to_be_set(self):
        self.car.fuel_consumption = 10
        expected_result = 10
        actual_result = self.car.fuel_consumption
        self.assertEqual(expected_result, actual_result)

    def test_car_fuel_consumption_setter__0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_car_fuel_consumption_setter__negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -55

    def test_car_fuel_capacity_setter__correct_value__expect_make_to_be_set(self):
        self.car.fuel_capacity = 10
        expected_result = 10
        actual_result = self.car.fuel_capacity
        self.assertEqual(expected_result, actual_result)

    def test_car_fuel_capacity_setter__0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_car_fuel_capacity_setter__negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -55

    def test_car_fuel_amount_setter__correct_value__expect_make_to_be_set(self):
        self.car.fuel_amount = 10
        expected_result = 10
        actual_result = self.car.fuel_amount
        self.assertEqual(expected_result, actual_result)

    def test_car_fuel_amount_setter__negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -55


if __name__ == '__main__':
    unittest.main()
