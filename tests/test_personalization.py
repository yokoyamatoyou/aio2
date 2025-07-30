import unittest
from core.aio_scorer import calculate_personalization_score
from core.industry_detector import INDUSTRY_CONTENTS
try:
    from seo_aio_streamlit import calculate_aio_score
except Exception:
    calculate_aio_score = None


class TestPersonalizationScore(unittest.TestCase):
    def test_personalization_score(self):
        text = "当店のメニューをご確認いただき、予約も簡単にできます。アクセスも便利です。"
        score, missing = calculate_personalization_score(text, 'restaurant', INDUSTRY_CONTENTS)
        self.assertGreater(score, 40)
        self.assertIn('地図', missing)

    def test_calculate_aio_score(self):
        text = "当店のメニューをご確認いただき、予約も簡単にできます。アクセスも便利です。"
        if not calculate_aio_score:
            self.skipTest("main module not available")
        total, scores, industry, missing = calculate_aio_score(text)
        self.assertEqual(industry, 'restaurant')
        self.assertIn('業種適合性', scores)
        self.assertAlmostEqual(total, scores['業種適合性'], places=1)
        self.assertIn('地図', missing)

    def test_calculate_aio_score_unknown(self):
        if not calculate_aio_score:
            self.skipTest("main module not available")
        text = "これはどの業種にも当てはまらない内容です。"
        total, scores, industry, missing = calculate_aio_score(text)
        self.assertEqual(industry, 'unknown')
        self.assertEqual(total, 0.0)
        self.assertEqual(scores['業種適合性'], 0.0)
        self.assertEqual(missing, [])

    def test_calculate_aio_score_empty(self):
        if not calculate_aio_score:
            self.skipTest("main module not available")
        total, scores, industry, missing = calculate_aio_score('')
        self.assertEqual(industry, 'unknown')
        self.assertEqual(total, 0.0)
        self.assertEqual(scores['業種適合性'], 0.0)
        self.assertEqual(missing, [])


if __name__ == '__main__':
    unittest.main()
