def check_question(question):
if question[-1] is "?":
answer_question()
elif question == "quit":
print ("Talk to you later.")
else:
ask_question()

ask_question()
