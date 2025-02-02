import math

n = 15
width = n

print """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" preserveAspectRatio="xMidYMin">
  
  <desc>The sum of the first n odd numbers equals n squared</desc>
  <title>Odd sum</title>
""" % (width, width)

start = 0;
gap = 0.05;
small_gap = gap;
for i in range(0, n):
  color = "magenta" if i % 2 == 0 else "blue"
  print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i, i, 1 - gap, 1 - gap, color)
  for j in range(0, i):
    print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (i, j, 1 - gap, 1 - small_gap, color)
    print '<rect id="block" x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.5" />' % (j, i, 1 - small_gap, 1 - gap, color)
  print

print """</svg>"""