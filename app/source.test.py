import unittest
from models import source
source = source.source

class SOURCETest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = source("al-jazeera-english", "Al Jazeera English",
        "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.","us")
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,source))


if __name__ == '__main__':
    unittest.main()