import openai
openai.organization = "org-5bPJuHRemCDzteuHacQLydzL"
openai.api_key = "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"
# os.getenv("OPENAI_API_KEY")
print(openai.Model.list())