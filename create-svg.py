import math

n = 7
width = n * (n + 1) / 2

print """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" preserveAspectRatio="xMidYMin">
  
  <desc>The sum of the first n cubes equals the square of the sum of the first n numbers</desc>
  <title>Cube sum</title>
""" % (width, width)

start = 0;
for i in range(1, n + 1):
  color = "magenta" if i % 2 == 0 else "blue"
  for j in range(0, int(math.ceil(i / 2.0))):
    print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (start, i * j, i - 0.05, i - 0.05, color)
    if i * j != start:
      print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i * j, start, i - 0.05, i - 0.05, color)      
  start = start + i
  print

print """</svg>"""