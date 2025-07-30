import unittest
from core.advice_utils import generate_actionable_advice

class TestActionableAdvice(unittest.TestCase):
    def test_known_industry(self):
        advice = generate_actionable_advice(['予約', '地図'], 'restaurant')
        self.assertIn('飲食店', advice)
        self.assertIn('予約', advice)
        self.assertIn('地図', advice)

    def test_unknown_industry(self):
        advice = generate_actionable_advice(['予約'], 'unknown')
        self.assertIn('業種を特定できませんでした', advice)
        self.assertNotIn('飲食店', advice)

    def test_no_missing_keywords(self):
        advice = generate_actionable_advice([], 'restaurant')
        self.assertIn('重要キーワードは見当たりません', advice)

if __name__ == '__main__':
    unittest.main()
