import math

n = 14
width = n
height = n + 1

print """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" preserveAspectRatio="xMidYMin">
  
  <desc>The sum of the first n numbers equals half of n times n plus one</desc>
  <title>Number sum</title>
""" % (width, height)

start = 0;
for i in range(0, n):
  color = "magenta" if i % 2 == 0 else "blue"
  print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i, i, 1 - 0.05, 1 - 0.05, color)
  for j in range(0, i):
    print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i, j, 1 - 0.05, 1, color)
  color = "magenta" if i % 2 == 1 else "blue"
  for j in range(i + 1, n + 1):
    print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i, j, 1 - 0.05, 1, color)
  print

print """</svg>"""