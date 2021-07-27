import unittest


class WorkerTests(unittest.TestCase):
    name = "Pesho"
    salary = 1500
    energy = 100
    energy_2 = 0

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_init_worker__name_salary_energy__expect_correct(self):
        expected_result = [self.name, self.salary, self.energy]
        actual_result = [self.worker.name, self.worker.salary, self.worker.energy]
        self.assertEqual(expected_result, actual_result)

    def test_rest__expect_energy_increased_by_1(self):
        self.worker.rest()
        expected_result = 101
        actual_result = self.worker.energy
        self.assertEqual(expected_result, actual_result)

    def test_work__negative_or_zero_energy__expect_error(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(context.exception))
        self.worker.energy = -5
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__expect_increased_salary(self):
        self.worker.work()
        expected_result = 1500
        actual_result = self.worker.money
        self.assertEqual(expected_result, actual_result)

    def test_work__expect_decreased_energy(self):
        self.worker.work()
        expected_result = 99
        actual_result = self.worker.energy
        self.assertEqual(expected_result, actual_result)

    def test_get_info__expect_correct(self):
        expected_result = 'Pesho has saved 0 money.'
        actual_result = self.worker.get_info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
