# Scrapy settings for gator project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'gator'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['gator.spiders', 'gator.items']
NEWSPIDER_MODULE = 'gator.spiders', 'gator.items'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

