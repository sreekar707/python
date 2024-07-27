import requests
jokes_iter=[]
def fetch_api():
    url=("https://api.freeapi.app/api/v1/public/randomjokes?query=science")
    response=requests.get(url)
    data=response.json()
    # print()
    for i in range (0,3):
        
    
        if data ["success"] and "data" in data:
               jokes_iter.append(data["data"]["data"][i]["content"])
    
        else:
            raise Exception ("failed")
        
        
def main():
    try:
        random_jokes=fetch_api()
        print(f"Jokes:  {jokes_iter}")
    except Exception as e:
        print(str(e))
          
        
if __name__=="__main__":
     
        main()

# fetch_api()       
    
    
    
    
    