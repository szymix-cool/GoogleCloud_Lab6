from fastapi import FastAPI
import math
app=FastAPI()

@app.get("/{n}")
async def get_factorial(n:int):
    if n<50 and n>=0:
        return {"n": n, "n!":math.factorial(n)}
    else:
        return {"n":n, "n!": "wrong number"}
