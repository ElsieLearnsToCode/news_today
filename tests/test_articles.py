import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''

        self.new_article = Articles('engadget',
        'Kris Holt','Apple Music arrives on Roku streaming devices, smart TVs and speakers',
        'Apple Music\r\n will be available on the Roku\r\n platform starting today...',
        'https://www.engadget.com/apple-music-roku-app-150514270.html',
        '2022-05-02T08:45:18Z')

    def test_instance(self):
        '''
        test case to test if the Sources objects exists
        '''
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        '''
        test case to test if the Articles object is initialized properly
        '''
        self.assertEquals(self.new_article.id,'engadget')
        self.assertEquals(self.new_article.title,'Apple Music arrives on Roku streaming devices, smart TVs and speakers')
        self.assertEquals(self.new_article.author,'Kris Holt')
        self.assertEquals(self.new_article.description,'Apple Music\r\n will be available on the Roku\r\n platform starting today...')
        self.assertEquals(self.new_article.url,'https://www.engadget.com/apple-music-roku-app-150514270.html')
        self.assertEquals(self.new_article.date,'2022-05-02T08:45:18Z')

if __name__ == '__main__':
    unittest.main()



