from fastapi import FastAPI
import math
import uvicorn
import os
app=FastAPI()

@app.get("/{n}")
async def get_factorial(n:int):
    if n<50 and n>=0:
        return {"n": n, "n!":math.factorial(n)}
    else:
        return {"n":n, "n!": "wrong number"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
