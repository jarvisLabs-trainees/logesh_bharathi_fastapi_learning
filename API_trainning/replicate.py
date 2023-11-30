from fastapi import FastAPI
import replicate

app = FastAPI()

@app.get("/generate_dream_image")
async def generate_dream_image(prompt:str):
    model_version = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
    result =replicate.run(
        model_version,
        input={"prompt": prompt}
    )

    image_url = result  [0]

    return{"image_url": image_url}
