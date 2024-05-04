import requests
import json

def get_book():
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/spells/random')
    print(response)
    books = response.json()
    book = json.dumps(books)
    bookDict = json.loads(book)
    return ("Spell: " + bookDict['spell'], " Use: " + bookDict['use'])
get_book()
    