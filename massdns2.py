#!/usr/bin/env python2

import ADNS
import adns

def show_answer(reply, request, *other):
	print("{0} -> {1}".format(request,reply))	

if __name__ == '__main__':

	with open('tlds-alpha-by-domain.txt') as f:
		tlds = f.readlines()
		reqs = (('www.google.{0}'.format(x.rstrip()), adns.rr.A) for x in tlds)
		c = ADNS.init()
		for (h,t) in reqs:
			c.submit(h,t,callback=show_answer)
			
		c.finish()



