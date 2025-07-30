import unittest
from core.industry_detector import IndustryDetector, detect_industry

class TestIndustryDetector(unittest.TestCase):
    def setUp(self):
        self.detector = IndustryDetector()

    def test_analyze_industries_basic(self):
        title = "最新のAIを活用したクラウドサービス"
        content = "AWSやDockerなどのテクノロジーを利用するシステム開発"
        result = self.detector.analyze_industries(title, content)
        self.assertEqual(result.primary_industry, "IT・テクノロジー")
        self.assertGreater(result.confidence_score, 0)
        self.assertIn("クラウド", result.industry_keywords)

    def test_detect_industry_simple(self):
        text = "予約やテイクアウトに対応した当店のメニューをご覧ください"
        industry = detect_industry(text)
        self.assertEqual(industry, "restaurant")

    def test_detect_industry_real_estate(self):
        text = "マンションや戸建ての売買をサポートする不動産会社です"
        industry = detect_industry(text)
        self.assertEqual(industry, "real_estate")

    def test_detect_industry_empty(self):
        self.assertEqual(detect_industry(""), "unknown")

if __name__ == '__main__':
    unittest.main()
