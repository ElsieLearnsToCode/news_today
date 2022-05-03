import unittest

from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        self.new_source = Sources('abc-news',
        'ABC News',
        'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
        'https://abcnews.go.com','general','en',"us")

    def test_instance(self):
        '''
        test case to test if the Sources objects exists
        '''

        self.assertTrue(isinstance(self.new_source,Sources))

    
    def test_to_verify_sources_variables(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEquals(self.new_source.id,'abc-news')
        self.assertEquals(self.new_source.name,'ABC News')
        self.assertEquals(self.new_source.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEquals(self.new_source.url,'https://abcnews.go.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.language,'en')
        self.assertEquals(self.new_source.country,'us')


if __name__ == '__main__':
    unittest.main()
