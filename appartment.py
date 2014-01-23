#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

class Appartment(object):
	"""Appartment class consists of features that have all appartments"""
	def __init__(self, address, metro, transportation, rooms, space, price, floor, addInfo):
		super(Appartment, self).__init__()

		self.address = self.setAddress(self, address)
		self.metro = self.setMetro(self, metro)
		self.transportation = self.setTransportation(self, transportation)
		self.rooms = self.setRooms(self, rooms)
		self.space = self.setSpace(self, space)
		self.price = self.setPrice(self, price)
		self.floor = self.setFloor(self, floor)
		self.addInfo = self.setAddInfo(self, addInfo)
	
	# Getter methods

	def getAddress(self):
		return self.address

	def getMetro(self):
		return self.metro

	def getTransportation(self):
		return self.transportation

	def getRooms(self):
		return self.rooms

	def getSpace(self):
		return self.space

	def getPrice(self):
		return self.price

	def getFloor(self):
		return self.floor

	def getAddInfo(self):
		return self.addInfo

	# Setter methods

	def setAddress(self, address):
		if type(address) is str or unicode:
			self.address = address
		else:
			print "Can't set proper address, type is not string"
			self.address = None

	def setMetro(self, metro):
		if type(metro) is str or unicode:
			self.metro = metro
		else:
			print "Can't set metro, type is not string"
			self.metro = None

	def setTransportation(self, transportation):
		if type(transportation) is dict:
			self.transportation = transportation
		elif type(transportation) is str or unicode:
			time = re.search(u'\d+', transportation)
			auto = re.search(u'авто', transportation)
			foot = re.search(u'пешком', transportation)
			if time and auto:
				time = int(time.group())
				d = {}
				d['auto'] = time
				self.transportation = d
			elif time and foot:
				time = int(time.group())
				d = {}
				d['foot'] = time
				self.transportation = d
			else:
				self.transportation = None

	def setRooms(self, rooms):
		if type(rooms) is int:
			self.rooms = rooms
		elif type(rooms) is str or unicode:
			room = re.search(u'\d', rooms)
			if room:
				room = int(room.group())
				self.rooms = room
			else:
				print "error, no match"
				self.rooms = None
		else:
			print "type error, current type is " + type(rooms)

	def setSpace(self, space):
		pass