import requests

HOST = 'localhost'
PORT = 80

def url(path='', query={}):
    q = '&'.join([f'{k}={v}' for k, v in query.items()])
    return f'http://{HOST}:{PORT}{path}?{q}'

# GET HOME PAGE
def test_get_main_page_status_code_equals_200():
    r = requests.get(url())
    assert r.status_code == 200

# GET SEARCH BY TEXT
def test_get_search_by_text_status_code_equals_200():
    r = requests.get(url('/api/v1/search', { 'text': 'привет' }))
    if r.status_code == 408:
        print('The service is not ready, let\'s give it one more chance.')
        r = requests.get(url('/api/v1/search', { 'text': 'привет' }))
    text = 'добавлю тюнингом коньках ПОДХОДИШЬ погулять интернете ЖКХ Минздрава объяснила, что сейчас через СМИ; При этом.'
    r = requests.get(url('/api/v1/search', { 'text': 'привет' }))
    assert r.status_code == 200

def test_get_search_by_text_status_code_equals_400():
    r = requests.get(url('/api/v1/search', { 'text': '' }))
    assert r.status_code == 400

def test_get_search_by_text_status_code_equals_414():
    r = requests.get(url('/api/v1/search'), { 'text': 'noway'*21 })
    assert r.status_code == 414

# DELETE BY ID
def test_delete_by_id_status_code_equals_204():
    r = requests.delete(url('/api/v1/doc/10'))
    assert r.status_code == 204

    r = requests.delete(url('/api/v1/doc/1600'))
    assert r.status_code == 204

