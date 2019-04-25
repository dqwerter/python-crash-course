name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower() + "\n")

first_name = "ada"
last_name = "lovelace"
print("\tHello, " + first_name.title() + " " + last_name.title())
print("\n")

strs = "     python     "
print("\"" + strs.strip()  + "\"")
print("\"" + strs.rstrip() + "\"")
print("\"" + strs.lstrip() + "\"")
print("\n")
quotation = "---> ' <---"
print(quotation)
quotation = '---> " <---'
print(quotation)

int_var = 23
message = str(int_var) + " is an integer. " # do not redefine str, otherwise error will occur here
print(message)

