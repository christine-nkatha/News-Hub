class News:
    def __init__(self,title,description,urlToImage,content,publishedAt):
        self.title = title  
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt

    def __str__(self) -> str:
        return self.title;