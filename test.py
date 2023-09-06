from unittest import TestCase, main
from whiteboard import solution
class MatchTestCase(TestCase):
    def test_example_one(self):
        self.assertEqual(solution(" Hello there thanks for trying my Kata"), "#HelloThereThanksForTryingMyKata")
    def test_example_two(self):
        self.assertEqual(solution("    Hello     World   "), "#HelloWorld")
    def test_example_three(self):
        self.assertEqual(solution(""), False)
    def test_big_string(self):
        self.assertEqual(solution('Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong cat'), False)
    def test_all_but_one(self):
        self.assertEqual(solution("  one  "),"#One")
    def test_four(self):
        self.assertEqual(solution('CoDeWaRs is niCe'),'#CodewarsIsNice')