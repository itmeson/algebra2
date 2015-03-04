#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Algebra 2 (2014-2015)"
SITEURL = 'http://markbetnel.com/courses/algebra2/s2015'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'

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

PLUGIN_PATHS = ['../../../pelican-plugins/'] 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican_vimeo', 'pelican_youtube', 'sitemap', 'tipue_search', 'latex']

DOCUTIL_CSS = True
COMMENTS_INTRO = "Is something unclear? Leave a comment below:"
DISPLAY_PAGES_ON_MENU = True

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}


