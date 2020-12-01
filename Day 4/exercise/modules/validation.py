
def validate_string(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str) and result:
            return result
        raise Exception ('Provide a non-empty string')
    return inner

def validate_country(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str) and result and 1 < len(result) <= 3:
            return result
        raise Exception ('Provide a country code (2-3 letters, like: hun, uk)')
    return inner

def dates_equal(func):
    def inner (*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return 'These historical values are equal'
        else:
            return 'These historical values are not equal'
    return inner

@dates_equal
def compare_dates(self, other):
    return self.date == other.date