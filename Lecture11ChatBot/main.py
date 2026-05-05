


from google import genai

googleAPIKEY="YOUR_API_KEY "


clientGoogle = genai.Client(api_key=googleAPIKEY)

userKaSawal= input("Enter Your Question here")

response = clientGoogle.models.generate_content(
    model="gemini-3-flash-preview", contents=userKaSawal
)
print(response.text)