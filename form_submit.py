import requests


url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSejp7GBOIndHHIqXdaVXeP1EuM2ILMI0bV536SRk4XPng-5Yg/formResponse"

form_data = {
    "entry.896472993": 2,
    "entry.1338492938": 2,
    "entry.2001720545": 2,
}


def submit_form(url, data):
    try:
        requests.post(url, data=data)
        print("form submitted")
        # time.sleep(5)  #uncomment this if you are gonna do a loop, add delay to not make too many request too fast
    except:
        print("error occured")


submit_form(url=url, data=form_data)
