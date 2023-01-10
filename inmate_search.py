from splinter import Browser
from time import sleep


last_name = ["string_here"]
first_name = ["string_here"]
trav = False
wilco = False
date = "04/01/2016"
allGood = True
#charges = []


for person in range(len(last_name)):
	with Browser() as browser:
		# Travis County Inmate Search
		
		t_url = "https://public.co.travis.tx.us/SIPS/default.aspx"
		
		browser.visit(t_url)
		browser.fill('LastName',last_name[person])
		browser.fill('FirstInitial',first_name[person])
		button = browser.find_by_name('SubmitNameSearch')
		button.click()
		if browser.is_text_present('Currently in Custody'):
			details = browser.find_by_name('SubmitInmate')
			details.click()
			results = browser.find_by_id('InmateCharges').first
			allGood = False
			#charges.append(results.value)
			print("")
			print("%s %s IS IN JAIL FOR:" % (first_name[person],last_name[person]))
			print("")
			print(results.value)
		
		#Williamson County Inmate Search 
		w_url = "http://judicialrecords.wilco.org/JailingSearch.aspx?ID=400"
		browser.visit(w_url)
		browser.click_link_by_partial_href("JailingSearch.aspx?ID=400")
		browser.fill('LastName',last_name[person])
		browser.fill('FirstName',first_name[person])
		browser.fill('DateBookingOnAfter',date)
		button = browser.find_by_name('SearchSubmit')
		button.click()
		if browser.is_text_not_present('No jailings matched your search criteria.'):
			browser.click_link_by_partial_href('JailingDetail.aspx')
			charges = browser.find_by_tag('tbody').last
			allGood = False
			#charges.append(result.value)
			print("")
			print("%s %s IS IN JAIL FOR:" % (first_name[person],last_name[person]))
			print("")
			print(charges.value)

		sleep(2)

if (allGood):
	print("Everything is good...for now")
