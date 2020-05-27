import requests

class Search:
    def search(search_key):
        url = "https://google-shopping.p.rapidapi.com/search"

        querystring = {"language":"EN","keywords":search_key,"country":"US"}

        f = open("google_shopping_api_key.txt","r")
        api_key = f.read()
        headers = {
            'x-rapidapi-host': "google-shopping.p.rapidapi.com",
            'x-rapidapi-key': api_key
            }
        f.close()
        response = requests.request("GET", url, headers=headers, params=querystring)
        dic = response.json()
        s = ""
        if "message" in dic:
            return "Message: " + dic.get("message")
        for product in dic:
            s = s + "Product Title: " + product.get('title') + "<br>" + "Product Price: " + product.get('currency') + str(product.get('price')) + "<br><br>"
             
        return s
