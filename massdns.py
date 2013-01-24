#!/usr/bin/env python2

import adns
from collections import deque

def resolve_all(source, buffer = 10):
	s = iter(source)
	c = adns.init()
	q = deque()

	def put():
		req = next(s)
		q.append(c.submit(*req))

	try:
		for x in range(0,buffer):
			put()

		while True:
			put()
			yield q.popleft().wait()

	except StopIteration:
		for x in q:
			yield x.wait()
	
if __name__ == '__main__':


	with open('tlds-alpha-by-domain.txt') as f:
		tlds = f.readlines()
		reqs = (('www.google.{0}'.format(x.rstrip()), adns.rr.A) for x in tlds)
		answers = resolve_all(reqs, buffer=6000)
		for a in answers:
			print a
		


