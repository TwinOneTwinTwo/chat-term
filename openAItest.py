from openai import OpenAI
import os

client = OpenAI(api_key= os.environ["OPENAI_API_KEY"], 
                organization="org-5fmE2w0iIwH1OfFTGhNQFhOo")


res = client.images.generate(
  model="dall-e-3",
  prompt="turn reference file into a comic hero with a close up of the face",
  n=1,
  size="1024x1024"
)

print(res.model_dump())

