import json
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {
            "role": "user",
            "content": "List the 200 oldest creation myths in the world with their date, location and title",
        }
    ],
)

output = completion.choices[0].message.content
print(output)

file_path = "output.txt"

# Write the output to a text file
with open(file_path, "w") as file:
    file.write(output)

print(f"Output saved to {file_path}.")
