mport unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class testSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer("This is a good movie")
        self.assertEqual(result1['label'], 'SENT_POSITIVE')

        result2 = sentiment_analyzer("This is not a good movie")
        self.assertEqual(result2['label'], 'SENT_NEGATIVE')

        result3 = sentiment_analyzer("This is a okay movie")
        self.assertEqual(result3['label'], 'SENT_NEUTRAL')
        

if __name__ ==  '__main__':
    unittest.main()
    
