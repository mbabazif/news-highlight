class ARTICLE:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,articles,title,name,author,description,url,publishedAt):
        self.articles = articles
        self.title = title
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.publishedAt = publishedAt