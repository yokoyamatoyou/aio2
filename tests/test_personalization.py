import unittest
from core.aio_scorer import calculate_personalization_score
from core.industry_detector import INDUSTRY_CONTENTS


class TestPersonalizationScore(unittest.TestCase):
    def test_personalization_score(self):
        text = "当店のメニューをご確認いただき、予約も簡単にできます。アクセスも便利です。"
        score, missing = calculate_personalization_score(text, 'restaurant', INDUSTRY_CONTENTS)
        self.assertGreater(score, 40)
        self.assertIn('地図', missing)


if __name__ == '__main__':
    unittest.main()
