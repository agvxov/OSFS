#!/bin/python3

from sys import argv
from contextlib import suppress
import json
import bs4

def usage():
	print("Incorrect invokation. Usage:")
	print("\ŧ" + argv[0] + " [FILE]")
	exit(1)

if len(argv) == 1:
	usage()

with open(argv[1]) as f:
	b = bs4.BeautifulSoup(f.read(), 'html.parser')
entries = b.find_all(class_="m-grantsDatabase__item")

class donation:
	pass

def assignAttempt(o, attr, cmd):
	buf = ""
	with suppress(AttributeError): buf = eval(cmd)
	setattr(o, attr, buf)
		
donations = []
for i in entries:
	d = donation()
	d.to = i.find(class_="a-grantsDatabase__title").get_text()
	d.date = i.find(class_="a-grantsDatabase__cell--1").get_text()
	d.amount = i.find(class_="a-grantsDatabase__cell--2").get_text()
	d.desc = i.find(class_="a-grantsDatabase__cell--6").find(class_="a-grantsDatabase__text").get_text()
	assignAttempt(d, 'theme', 'i.find(string="Theme").parent.next_sibling.next_sibling.get_text()')
	assignAttempt(d, 'ref_prog', 'i.find(string="Referring Program").parent.next_sibling.next_sibling.get_text()')
	assignAttempt(d, 'term', 'i.find(string="Term").parent.next_sibling.next_sibling.get_text()')
	assignAttempt(d, 'region', 'i.find(string="Region").parent.next_sibling.next_sibling.get_text()')
	assignAttempt(d, 'funder', 'i.find(string="Funder").parent.next_sibling.next_sibling.get_text()')
	donations.append(d)



for i in donations:
	for h in vars(i):
		exec('i.{0} = i.{0}.strip(" \\t\\n")'.format(h))

print(json.dumps([i.__dict__ for i in donations]))
