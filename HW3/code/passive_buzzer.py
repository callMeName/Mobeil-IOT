#!/usr/bin/env python
#---------------------------------------------------
#		Passive buzzer 			   Pi 
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SIG ---------------- Pin 11
#
#---------------------------------------------------

import RPi.GPIO as GPIO
import time
import sys

Buzzer = 7

CL = [0, 131, 147, 165, 175, 196, 211, 248]		# Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes

song_1 = [	CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Notes of song1
			CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3], 
			CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
			CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]	]

beat_1 = [	1, 1, 3, 1, 1, 3, 1, 1, 			# Beats of song 1, 1 means 1/8 beats
			1, 1, 1, 1, 1, 1, 3, 1, 
			1, 3, 1, 1, 1, 1, 1, 1, 
			1, 2, 1, 1, 1, 1, 1, 1, 
			1, 1, 3	]

song_2 = [	CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Notes of song2
			CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2], 
			CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1], 
			CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]	]

beat_2 = [	1, 1, 2, 2, 1, 1, 2, 2, 			# Beats of song 2, 1 means 1/8 beats
			1, 1, 2, 2, 1, 1, 3, 1, 
			1, 2, 2, 1, 1, 2, 2, 1, 
			1, 2, 2, 1, 1, 3 ]

def setup():
	GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
	GPIO.setup(Buzzer, GPIO.OUT)	# Set pins' mode is output
	global Buzz						# Assign a global variable to replace GPIO.PWM 
	Buzz = GPIO.PWM(Buzzer, 440)	# 440 is initial frequency.
	Buzz.start(50)					# Start Buzzer pin with 50% duty ration

def play(song, beat):
	for i in range(1, len(song)):		
		Buzz.ChangeFrequency(song[i])	# Change the frequency along the song note
		time.sleep(beat[i] * 0.5)		# delay a note for beat * 0.5s

def destory():
	Buzz.stop()					# Stop the buzzer
	GPIO.output(Buzzer, 1)		# Set Buzzer pin to High
	GPIO.cleanup()				# Release resource


def loop(n):
	while True:
		if n == 1:
			print '\n    Playing song 1...'
			play(song_1, beat_1)
			time.sleep(1)						# Wait a second for next song.
		if n == 2:
			print '\n\n    Playing song 2...'
			play(song_2, beat_2)
			time.sleep(1)						# Wait a second for next song.
			

def help():
	print '''python %s play_mode
Play Mode: 1 or 2''' %sys.argv[0]

if __name__ == '__main__':
	setup()
	try:
		if len(sys.argv) != 2:
			help()
			sys.exit(1)
		play_mode = int(sys.argv[1])
		if play_mode != 1 && play_mode != 2:
			help()
			sys.exit(2)
		loop(play_mode)
	except KeyboardInterrupt:  
    	pass
	finally:
    	GPIO.cleanup()

