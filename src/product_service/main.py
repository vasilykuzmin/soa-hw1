from connexion import AsyncApp

def createProduct(*args):
    pass

def getProducts(page, size, status, category):
    print(page, size, status, category)
    pass

def getProductById(*args):
    pass

def updateProduct(*args):
    pass

def archiveProduct(*args):
    pass

def aboba():
    print('aboba')
    return 200

def post_greeting(name: str, greeting: str):  # Paramaeters are automatically unpacked
    return f"{greeting} {name}", 200          # Responses are automatically serialized

if __name__ == '__main__':
    app = AsyncApp(__name__)
    app.add_api("openapi.yaml")

    app.run()
