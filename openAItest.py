from openai import OpenAI

client = OpenAI(api_key="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", 
                organization="org-5fmE2w0iIwH1OfFTGhNQFhOo")


res = client.images.generate(
  model="dall-e-3",
  prompt="turn reference file into a comic hero with a close up of the face",
  n=1,
  size="1024x1024"
)

print(res.model_dump())

