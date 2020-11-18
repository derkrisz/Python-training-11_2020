from modules.exercise_validation import cleanup
import requests

def get_data(category, id):
    url = 'https://jsonplaceholder.typicode.com'
    param = category
    id = id
    full_path = f'{url}/{param}/{id}'
    j = ''
    try:
        res = requests.get(full_path)
        j = res.json()
    except Exception as err:
        print('Something went wrong. ', err)
    finally:
        return j



if __name__ == '__main__':
    category = input('Choose a category from: users, posts, albums, photos ')
    id = input('Enter an id between 1-8 ')
    cleaned = cleanup(category=category, id=id)
    print(cleaned)
    data = get_data(category=cleaned['category'], id=cleaned['id'])
    print(data)