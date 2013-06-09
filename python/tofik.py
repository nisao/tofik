#! /usr/bin/python3 -u
# (Note: The -u disables buffering, as else we don't get Julius's output.)
#
# Command and Control Application for Julius
#
# How to use it:
#  julius -quiet -input mic -C julian.jconf 2>/dev/null | ./command.py
#
# Copyright (C) 2013 Kamil Skowron <info@kamilskowron.pl> 
# Based on julius-voxforge example by:
# Siegfried-Angel Gevatter Pujals <rainct@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Supported commands:
#
# See tofik.voca for full reference of available commands.

import sys
import os

class Tofik:
	
	name = "Tofik"
	
	voiceOn = True
	
	commands = {
		'voice on': 'turn voice recognition off',
		'voice off': 'turn voice recognition on'        
	}
	
	def parse(self, word):
		if word == 'voice on':
			self.voiceOn = True
			return self.voiceOn
		elif word == 'voice off':
			self.voiceOn = False
			return self.voiceOn			

class Ubuntu:

	name = "Ubuntu"

	commands = {
		'lock': 'gnome-screensaver-command -l' 
	}

	def parse(self, word):
		if word in self.commands:
			return self.commands[word]

class Rhythmbox:
	
	name = "Rhythmbox"
	
	commands = {
			'play': 'play',
			'pause': 'pause',
			'next': 'next',
			'prev': 'previous',
			'show': 'notify',
			'pause': 'pause',
			'silence': 'pause',
	}
	
	def parse(self, word):
		if word in self.commands:
			notification = "notify-send -t 1000 'Rhythmbox COMMAND' ;".replace('COMMAND', self.commands[word].title())
			return notification + " rhythmbox-client --COMMAND".replace('COMMAND', self.commands[word])

class Banshee:
	
	name = "Banshee"
	
	commands = {
			'play': 'play',
			'pause': 'pause',
			'stop': 'stop',
			'next': 'next',
			'prev': 'previous',
			'pause': 'pause',
			'silence': 'pause',
	}
	
	def parse(self, word):
		if word in self.commands:
			return 'banshee --no-present --%s %% ' % self.commands[word]

class CommandAndControl:
	
	def __init__(self, file_object):
		
		self.ubuntu = Ubuntu();
		self.tofik  = Tofik();
        
		# Determine which media player to use
		if os.system('ps xa | grep -v grep | grep banshee >/dev/null') == 0:
			self.mediaplayer = Banshee()
		elif os.system('ps xa | grep -v grep | grep rhythmbox >/dev/null') == 0:
			self.mediaplayer = Rhythmbox()
		elif os.system('which banshee >/dev/null') == 0:
			self.mediaplayer = Banshee()
			os.system('bash -c "nohup banshee >/dev/null 2>&1 <&1 & disown %%"')
		elif os.system('which rhythmbox >/dev/null') == 0:
			self.mediaplayer = Rhythmbox()
		else:
			print('Couldn\'t find a supported media player. ' \
				'Please install Rhythmbox or Banshee.')
			sys.exit(1)
		print('Taking control of %s media player.' % self.mediaplayer.name)
		
		startstring = 'sentence1: <s> '
		endstring = ' </s>'
		
		while 1:
			line = file_object.readline()
			if not line:
				break
			if 'missing phones' in line.lower():
				print('Error: Missing phonemes for the used grammar file.')
				sys.exit(1)
			if line.startswith(startstring) and line.strip().endswith(endstring):
				self.parse(line.strip('\n')[len(startstring):-len(endstring)])
	
	def parse(self, line):
		# Parse the input
		params = [param.lower() for param in line.split() if param]
		if not '-q' in sys.argv and not '--quiet' in sys.argv:
			print('Recognized input:', ' '.join(params).capitalize())
		
		params.pop(0)
		# Execute the command, if recognized/supported
		# Before any execution check is listening switched on
		inputText = ' '.join(params)
		
		self.tofik.parse(inputText)
				
		if (self.tofik.voiceOn):
			command       = self.mediaplayer.parse(inputText)
			ubuntuCommand = self.ubuntu.parse(inputText)
			tofikCommand  = self.tofik.parse(inputText)        			
			if command:
				os.system(command)
			elif ubuntuCommand:
				os.system(ubuntuCommand)				
			elif tofikCommand:
				pass				
			elif not '-q' in sys.argv and not '--quiet' in sys.argv:
				print('Command not supported by %s.' % self.mediaplayer.name)
		else:
			print("Listening is disabled - say 'Computer Voice On' to active Tofik")

if __name__ == '__main__':
	try:
		CommandAndControl(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
