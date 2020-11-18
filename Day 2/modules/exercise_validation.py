categories = ('users', 'posts', 'albums', 'photos')

def cleanup(**kwargs):
    category = kwargs['category'].lower().strip()
    if not category or not category in categories:
        print('Choose one of the following categories: users, posts, albums, photos. Defaulting to photos')
        category = 'photos'

    id = int(float(kwargs['id']))
    if not id or id not in range(1,9):
        print('Provide an id between 1-8. Defaulting to 1.')
        id = 1
    return {'category': category, 'id': id}
    

if __name__ == '__main__':
    result = cleanup(category='users', id=3)
    print('result1: ', result)
    result2 = cleanup(category='something', id=1)
    print('result2: ', result)
    result3 = cleanup(category='', id=1)
    print('result3: ', result)
    result4 = cleanup(category='PHOTOS', id=1)
    print('result4: ', result)
    result5 = cleanup(category='photos', id=0)
    print('result5: ', result)
    result6 = cleanup(category='users', id=3.2)
    print('result6: ', result)
    result7 =cleanup(category='users', id='3.4252')

