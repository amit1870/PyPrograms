import datetime as dt

REF_SHIFT = "A"
REF_DATE  = dt.date(2018, 7, 23)

def get_shift(date_obj):
	global REF_SHIFT, REF_DATE
	NEW_SHIFT = REF_SHIFT
	cur_date = date_obj
	timedelta = cur_date - REF_DATE
	days = timedelta.days
	while days > 6:
		NEW_SHIFT = "B" if NEW_SHIFT == "A" else "A"
		days = days - 7

	return NEW_SHIFT


if __name__ == "__main__":
		date_obj = dt.date(2018, 8, 20)
		print get_shift(date_obj)
