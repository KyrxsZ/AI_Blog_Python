#first create .env file then
#insert your api keys in .env file like this (API_KEY='insert your api here') My Free credit is out so use your own :)
from openai import OpenAI
from dotenv import dotenv_values


config = dotenv_values('.env')
client = OpenAI(api_key=config['API_KEY'])

def generate_blog_multiple(topics):
    
    prompt_text = "Write a separate paragraph for each of the following topics:\n"
    for i, topic in enumerate(topics, start=1):
        prompt_text += f"{i}. {topic}\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes blog paragraphs."},
            {"role": "user", "content": prompt_text}
        ],
        max_tokens=800,  #300
        temperature=0.3
    )

    
    result_text = response.choices[0].message.content
    paragraphs = [p.strip() for p in result_text.split("\n\n") if p.strip()]
    return paragraphs

#get topic from user
topics = []
while True:
    answer = input("Add a topic? Y for yes, anything else for no: ")
    if answer.upper() == "Y":
        topic = input("Enter the topic: ")
        topics.append(topic)
    else:
        break

if topics:
    paragraphs = generate_blog_multiple(topics)
    print("\n--- Generated Blog ---\n")
    for p in paragraphs:
        print(p + "\n")
else:
    print("No topics entered. Exiting.")

