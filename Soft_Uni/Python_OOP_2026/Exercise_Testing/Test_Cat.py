class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False

from unittest import TestCase, main

class CatTests(TestCase):
    def test_init(self):
        c = Cat("tom")
        self.assertEqual("tom", c.name)
        self.assertEqual(False, c.fed)
        self.assertEqual(False, c.sleepy)
        self.assertEqual(0, c.size)

    def test_eat(self):
        c = Cat("tom")
        c.eat()
        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual("Already fed.", str(ex.exception))
        self.assertEqual(True, c.fed)
        self.assertEqual(1, c.size)

        c.fed = False
        c.eat()

        self.assertEqual(2, c.size)


    def test_sleep(self):
        c = Cat("tom")
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))
        self.assertEqual(False, c.sleepy)

        c.eat()

        self.assertEqual(True, c.sleepy)

        c.sleep()

        self.assertEqual(False, c.sleepy)


if __name__ == "__main__":
    main()