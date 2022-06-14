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
    c = requests.get(url=URL_COMMENTS)
    return c.json()

def print_user(user):
    print("Nombre:", user["name"])
    print("Genero:", user["gender"])
    print("E-Mail:", user["email"])
    print("Status:", user["status"])
    print("-----------------------------")

def print_comments(comments):
    print("Nombre:", comment["name"])
    print("E-Mail:", comment["email"])
    print("Comentario:", comment["body"])
    print("-----------------------------")

def translate_users(users):
    translate_users=[]
    for user in users:
        if user["gender"]=="female":
            user.update({"gender":"Femenino"})
        elif user["gender"]=="male":
            user.update({"gender":"Masculino"})
        
        if user["status"]=="active":
            user.update({"status":"Activo"})
        elif user["status"]=="inactive":
            user.update({"status":"Inactivo"})

    translate_users = user.copy()
    return translate_users

def filter_users(users):
    result = []
    for user in users: 
        if user["gender"]=="female":
            if user['status']=="active":
                result.append(user)
                #agrego a la lista
    return result

if __name__ == "__main__":
    print("ScrapeX.io - Webscraping Challenge")
    users = extract_users()
    comments = extract_comments()
    print(f"Extracted users from: {URL_USERS}")
    print(users)
    print(f"Extracted comments from: {URL_COMMENTS}")
    print(comments)

    print("------USUARIOS------")
    filtra = filter_users(users)
    
    for usuario in filtra:
        translate_users(filtra)
        print_user(usuario)

    print("------COMENTARIOS------")
    
    for comment in comments:
        print_comments(comments)