articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_list = []
    for article in articles_dict:
        article2 = article.get('title') + article.get('author')
        if letter_case == False:
            article2 = article2.lower()
            key = key.lower()
        
        if article2.find(key) != -1:
            new_list.append(article)
    return new_list


print(find_articles('Love'))
        


    
        
    
        
        
        
            
        
        
            
         
        
            
        
        
            
        
            
    