# using decorator syntax for property getter and setter methods
class WebPage:
    def __init__(self, title, desc):
        self.__title = title
        self.__desc = desc
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title
    def __str__(self): # here we override the default printout __str__
        return f'Page Title: {self.title}, Description: {self.__desc}'
    

if __name__ == '__main__':
    home_page = WebPage('Home', 'Home page')
    home_page.title = 'something'
    print(home_page)