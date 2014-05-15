#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Algebra 2"
SITEURL = 'http://markbetnel.com/courses/algebra2-f2014'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'algebra2'

# Blogroll
LINKS =  (
    ('SAGE', 'http://sagemath.org/'),
    ('Wolfram Alpha', 'http://www.wolframalpha.com/'),
    ('Khan Academy', 'http://www.khanacademy.org'),
    ('Math Fun Facts', 'http://www.math.hmc.edu/funfacts/'),
    ('R - Statistics', 'http://cran.r-project.org'),
    ('DESMOS', 'http://www.desmos.com')	
        )


DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATH = '../../../pelican-plugins' 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican-vimeo', 'pelican-youtube']
