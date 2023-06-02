import requests

URL_USERS = "https://gorest.co.in/public/v2/users"
URL_COMMENTS = "https://gorest.co.in/public/v2/comments"


def extract_users():
    """
    Method for get users from API Rest
    :return:
    """
    r = requests.get(url=URL_USERS)
    users = r.json()

    for user in users:
        user['status'] = 'activo' if user['status'] == 'active' else user.update({'status': 'inactivo'})

        user['gender'] = 'femenino' if user['gender'] == 'female' else user.update({'gender': 'masculino'})
        

        if user['gender'] == 'femenino' and user['status'] == 'activo':
            yield  f'''
                *Nombre: {user['name']}
                *Género: {user['gender']}
                *Email: {user['email']}
                *Status: {user['status']}\n'''
        

def extract_comments():
    """
    Method for get comments from API Rest
    :return:
    """
    # TODO: Implementar codigo para obtener los comentarios de la API
    r = requests.get(URL_COMMENTS)
    comments = r.json()

    for comment in comments:
        yield f'''
        *Nombre: {comment['name']}
        *Email: {comment['email']}
        *Comment: {comment['body']}
        '''



if __name__ == "__main__":
    print("ScrapeX.io - Webscraping Challenge\n")
    print(f"Extracted users from: {URL_USERS}")
    for user in extract_users(): print (user)
    print(f"Extracted comments from: {URL_COMMENTS}")
    for comment in extract_comments(): print (comment)