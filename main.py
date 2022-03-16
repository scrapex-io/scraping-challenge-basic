import requests

URL_USERS = "https://gorest.co.in/public/v2/users"
URL_COMMENTS = "https://gorest.co.in/public/v2/comments"


def extract_users():
    """
    Method for get users from API Rest
    :return:
    """
    r = requests.get(url=URL_USERS)
    return r.json()


def extract_comments():
    """
    Method for get comments from API Rest
    :return:
    """
    # TODO: Implementar codigo para obtener los comentarios de la API
    pass


if __name__ == "__main__":
    print("ScrapeX.io - Webscraping Challenge")
    users = extract_users()
    print(f"Extracted users from: {URL_USERS}")
    print(users)

