import requests

URL = "https://spclient.wg.spotify.com/signup/public/v1/account"
# ?
KEY = "a1e486e2729f46d6bb368d6b2bcda326"

def createSpotify(username, email, password):
	response = requests.post(URL, data={
		"birth_day":             "1",
		"birth_month":           "01",
		"birth_year":            "2000",
		"collect_personal_info": "undefined",
		"creation_point":        "https://www.spotify.com/us/",
		"displayname":           username,
		"email":                 email,
		"gender":                "male",
		"iagree":                "1",
		"key":                   KEY,
		"password":              password,
		"password_repeat":       password,
		"username":              username,
	}).text
	if "\"login_token\"" in response:
		return response
	elif "That email is already" in response:
		return "Email is currently being occupied on Spotify | {}".format(email)
	return "Account could not be made | {} : {} : {}".format(username, email, password)

if __name__ == "__main__":
	username = input("Username: ")
	email = input("Email: ")
	password = input("Password: ")

	print(createSpotify(username, email, password))
