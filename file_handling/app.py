file = open("questions.txt", "r")
content = file.readlines()
file.close()
total = len(content)
correct = 0
question_and_answer = []
for ques in content:
    if ques.strip():
        question,answer = ques.strip().split("=")
        question_and_answer.append({"question":question, "answer":answer})

for qa in question_and_answer:
    user_answer = input(f"{qa['question']}=")
    if user_answer == qa["answer"]:
        correct += 1

file = open("result.txt", "w")
file.write(f"Your final score is {correct}/{total}")
file.close()







list_of_names = ["John", "Jane", "Jim", "Jack", "Jill"]
seperator = "& "
joined_string = seperator.join(list_of_names)
print(joined_string)

