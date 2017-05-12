#!/usr/local/bin/python

import clusters

blog,words,data=clusters.readfile('blogdata.txt')

coordinates = clusters.scaledown(data)

clusters.draw2d(coordinates, blog, jpeg='blogs.jpg')
