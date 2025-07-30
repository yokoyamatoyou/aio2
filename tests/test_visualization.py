import unittest
try:
    from core.visualization import create_aio_score_chart_vertical, create_aio_radar_chart
    from core.constants import AIO_SCORE_MAP_JP
except Exception:
    create_aio_score_chart_vertical = None
    create_aio_radar_chart = None
    AIO_SCORE_MAP_JP = {}

class TestVisualization(unittest.TestCase):
    @unittest.skipUnless(create_aio_score_chart_vertical, "plotly not available")
    def test_create_aio_score_chart_vertical(self):
        data = {k: {"score": 50} for k in list(AIO_SCORE_MAP_JP.keys())[:3]}
        fig = create_aio_score_chart_vertical(data, AIO_SCORE_MAP_JP, "Test")
        self.assertTrue(hasattr(fig, 'data'))
        self.assertGreater(len(fig.data), 0)

    @unittest.skipUnless(create_aio_radar_chart, "plotly not available")
    def test_create_aio_radar_chart(self):
        labels = {
            "a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "e": "E",
            "f": "F"
        }
        values = {k: 10 for k in labels}
        fig = create_aio_radar_chart(values, labels)
        self.assertTrue(hasattr(fig, 'data'))
        self.assertEqual(len(fig.data[0]['r']), 6)

if __name__ == '__main__':
    unittest.main()
