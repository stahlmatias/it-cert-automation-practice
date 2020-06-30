def email_list(domains):
	emails = []
	for domain, user in domains.items():
		print(domain)


(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
