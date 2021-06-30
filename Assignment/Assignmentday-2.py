import random
Maximum_Participants_variable = int(input("enter the number:"))
participants = []
for i in range(0, Maximum_Participants_variable):
    n = input("enter the name:")
    participants.append(n)

m = random.randint(0,Maximum_Participants_variable-1)
print(participants[m])