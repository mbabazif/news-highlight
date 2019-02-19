import unittest
from models import article
article = article.article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = article("Newsbtc.com", "Aayush Jindal","Crypto Market Adds $10B: Litecoin (LTC), Bitcoin Cash, Tron (TRX), XLM Price Analysis",
        "The total crypto market cap added more than $10.0B recently and broke the $130.0B resistance. Litecoin (LTC) price gained momentum and broke the $45 and $47 resistance levels. Bitcoin cash price rallied close to 15% and tested the $150 resistance area. Tron (…",
        ,"https://www.newsbtc.com/2019/02/19/crypto-market-adds-10b-litecoin-ltc-bitcoin-cash-tron-trx-xlm-price-analysis/","https://www.newsbtc.com/wp-content/uploads/2018/08/techanalysis-alts4.jpg","2019-02-19T06:00:01Z",
        "The total crypto market cap added more than $10.0B recently and broke the $130.0B resistance.\r\nLitecoin (LTC) price gained momentum and broke the $45 and $47 resistance levels.\r\nBitcoin cash price rallied close to 15% and tested the $150 resistance area.\r\nTro… [+2464 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,article))


if __name__ == '__main__':
    unittest.main()