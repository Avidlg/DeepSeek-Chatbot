import requests

def chat_with_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}

    response = requests.post(url, json=data, headers=headers)
    return response.json().get("response", "خطا: پاسخی دریافت نشد")

# تست اولیه
user_input = input("شما: ")
print("ربات:", chat_with_deepseek(user_input))


