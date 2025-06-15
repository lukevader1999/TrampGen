import unittest
from Sprung import Sprung
from SprungFilter import SprungFilter

class DummySprung:
    def __init__(self, start, ende, rotationen, schrauben, position):
        self.start = start
        self.ende = ende
        self.rotationen = rotationen
        self.schrauben = schrauben
        self.position = position

class TestSprungFilter(unittest.TestCase):
    def setUp(self):
        self.spruenge = [
            DummySprung("F", "F", 0, 0, "a"),
            DummySprung("B", "F", 1, 0, "a"),
            DummySprung("F", "B", 1, 1, "b"),
            DummySprung("R", "F", 2, 1, "c"),
            DummySprung("F", "R", 2, 2, "a"),
            DummySprung("F", "F", 1, 0, "b"),
        ]

    def test_max_rotationen(self):
        f = SprungFilter(max_rotationen=1)
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.rotationen <= 1 for s in result))

    def test_max_schrauben(self):
        f = SprungFilter(max_schrauben=1)
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.schrauben <= 1 for s in result))

    def test_start_list(self):
        f = SprungFilter(start=["F"])
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.start == "F" for s in result))

    def test_ende_list(self):
        f = SprungFilter(ende=["F"])
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.ende == "F" for s in result))

    def test_position_list(self):
        f = SprungFilter(position=["a","b"])
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.position in ["a","b"] for s in result))

    def test_exclude_starts(self):
        f = SprungFilter(exclude_starts=["B","R"])
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.start not in ["B","R"] for s in result))

    def test_exclude_endes(self):
        f = SprungFilter(exclude_endes=["B","R"])
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.ende not in ["B","R"] for s in result))

    def test_combined(self):
        f = SprungFilter(start=["F"], exclude_endes=["B"], max_rotationen=1)
        result = f.filter(self.spruenge)
        self.assertTrue(all(s.start == "F" and s.ende != "B" and s.rotationen <= 1 for s in result))

if __name__ == "__main__":
    unittest.main()
