from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str = 'World'):
    message = f"Hello, {name}!"
    return {'message': message}