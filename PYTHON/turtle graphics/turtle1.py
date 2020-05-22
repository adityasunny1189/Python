from turtle import *
import time
import random
import math

colors = ["red", "green", "yellow", "black", "purple", "violet"]

for i in range(10):
	color(colors[i % len(colors)])
	fillcolor("pink")
	shape("turtle")
	forward(500)
	right(500)
	forward(500)
	right(500)

time.sleep(10)