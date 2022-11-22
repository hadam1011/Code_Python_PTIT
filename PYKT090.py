with open("CONTACT.in") as file:
    emails = [s.lower().strip() for s in file.readlines()]

emails.sort()
res = []
for x in emails:
    if x not in res: res.append(x)

for email in res: print(email)
