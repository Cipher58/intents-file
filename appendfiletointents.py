import os
import json

folder_path = "training_data"

file_list = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

# Load intents from intents.json
with open("intents.json", "r") as a:
    intents = json.load(a)

print("Loaded intents:", intents)  # Debug line

for file in file_list:
    file_path = os.path.join(folder_path, file)
    with open(file_path, "r") as f:
        data = f.read()

    # Split the data into paragraphs using newline character '\n'
    paragraphs = data.split('\n')

    # 'paragraphs' now contains a list of strings, each representing a paragraph
    for paragraph in paragraphs:
        if paragraph != "":
            for intent in intents["intents"]:
                if intent.get("tag") == "small-talk":
                    intent.setdefault("responses", []).append(paragraph)

    print(file, " done!")

# print("Modified intents:", intents)  # Debug line

# Save the modified intents back to intents.json
with open("./result/intents.json", 'w') as json_file:
    json.dump(intents, json_file, indent=4, separators=(',', ': '))
