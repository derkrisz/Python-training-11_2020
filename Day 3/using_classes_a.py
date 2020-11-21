class Person: # object is the default base class
    def __init__(self, name, email): # self = this. default values will always have to come after non-default values
        self.__name = name # double underscore is name mangling
        self.__email = email
    def show_me(self):
        print(f'Name: {self.name}, E-mail: {self.email}')
    def __get_name(self):
        return self.__name
    def __set_name(self, new_name):
        if type(new_name) == str and new_name != '':
            self.__name = new_name
        else:
            self.__name = 'NA'
    def get_email(self):
        return self.__email
    def set_email(self, new_email):
        self.__email = new_email
    name = property(__get_name, __set_name)
    email = property(get_email, set_email)

class Coder(Person):
    def __init__(self, name, email, languages):
        super().__init__(name, email)
        self.__languages = languages

    def __get_languages(self):
        return self.__languages
    def __set_languages(self, languages):
        if (isinstance(languages, list)):
            self.__languages = languages
        else:
            pass # make no changes
    def show_me(self):
        print(f'Name: {self.name}, E-mail: {self.email} Languages: {" ".join(self.languages)}')
    languages = property(__get_languages, __set_languages)


if __name__ == '__main__':
    p1 = Person('Greta', 'greta@green.ie')
    p1.name = True
    p1.__name = 'Something' # this just creates a new property
    p1.show_me()
    print(p1.name)
    # print(p1.__get_name())

    c1 = Coder('Beth', 'b@c.e', ['python', 'ecmascript', 'java'])
    c1.show_me()