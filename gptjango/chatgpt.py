import openai

openai.api_key = ""

def chat_with_gpt(prompt,type):
    if type == 0:
        extra_message = "과 같은 증상을 갖는 강아지가 가질만한 병명을 5개 확률 높은 순서대로 예측해줘."
    else:
        extra_message = "를 갖는 강아지 처치법 5개 알려줘 in English"    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt+extra_message,
        max_tokens=400, #왜 토큰이 잘릴까?
        temperature=0.3, 
        n=4,
        stop=['n5'],
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=4,
    )
    message = response.choices[0].text.strip()
    return message

if __name__ == '__main__':
    print(chat_with_gpt("강아지가 기침을 하는데 "))
    