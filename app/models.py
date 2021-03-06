class Sources:
    '''
    Sources class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,title,author,description,url,url_image,date_published):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = url_image
        self.date = date_published