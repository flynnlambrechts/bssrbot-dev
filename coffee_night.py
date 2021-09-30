#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos

#--- Wildcat Nominations
def add_nomination(rs, args): 
# Recieves a list of words containing the persons name first followed by the reason
# E.g. ["Flynn", "for", "making", "BssrBot"]
	person = args[0]
	reason = " ".join(args[1:])
	print(Person + "For" + reason)
	return args

#--- Quote Submission
def add_quote(rs, args):
	return args


#--- Photo Submission

