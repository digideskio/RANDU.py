The infamous RANDU algorithm

wikipedia: http://en.wikipedia.org/wiki/RANDU

Usage example:
	r = Randu(12345) # seed 12345
	r.next()
	
	for i in r:
		...
		
	
	r.sequencer() #returns a new generator
	
