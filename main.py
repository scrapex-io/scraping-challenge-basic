import requests  
import pandas as pd  
from rich.console import Console


URL_USERS = "https://gorest.co.in/public/v2/users"
URL_COMMENTS = "https://gorest.co.in/public/v2/comments" 
console = Console()


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
    j = requests.get(url=URL_COMMENTS)
    return j.json()
    



if __name__ == "__main__": 
    users = extract_users()
    comments = extract_comments()
    
    console.print("[bold][red]\nScrapeX.io - Webscraping Challenge\n")
    console.print(f"[red]Extracted users from: {URL_USERS}\n")
    
    df = pd.DataFrame(users) 
    df['gender']=df['gender'].map({'male':'masculino','female':'femenino'})  
    df['status']=df['status'].map({'active':'activo','inactive':'inactivo'}) 
    columns = df[df.columns[1:]]

    df2 = pd.DataFrame(comments) 
    columns2 = df2[df2.columns[2:]]

    query = columns.query("gender=='femenino' and status=='activo'") 
    print(columns) 
    console.print("\n[red]Users filtering by gender and status:\n")
    print(query) 
    
    console.print(f"\n[green]Extracted comments from: {URL_COMMENTS}\n") 
    print(columns2)
    print("\n")
    
    query.to_csv('Query.csv', index=False)
    columns.to_csv('users.csv', index=False)   
    columns2.to_csv('comments.csv', index=False)