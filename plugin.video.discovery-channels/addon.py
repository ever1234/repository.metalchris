#!/usr/bin/python
#
#
# Written by MetalChris
# Released under GPL(v2) or Later

import urllib, urllib2, xbmcplugin, xbmcaddon, xbmcgui, htmllib, platform, re, xbmcplugin, sys, os
import requests
import simplejson as json
from bs4 import BeautifulSoup
import html5lib
import mechanize
import cookielib

artbase = 'special://home/addons/plugin.video.discovery-channels/resources/media/'
_addon = xbmcaddon.Addon()
_addon_path = _addon.getAddonInfo('path')
addon_path_profile = xbmc.translatePath(_addon.getAddonInfo('profile'))
selfAddon = xbmcaddon.Addon(id='plugin.video.discovery-channels')
#self = xbmcaddon.Addon(id='plugin.video.discovery-channels')
translation = selfAddon.getLocalizedString
#usexbmc = selfAddon.getSetting('watchinxbmc')
settings = xbmcaddon.Addon(id="plugin.video.discovery-channels")
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

CookieJar = cookielib.LWPCookieJar(os.path.join(addon_path_profile, 'cookies.lwp'))
br = mechanize.Browser()
br.set_cookiejar(CookieJar)
br.set_handle_robots(False)
br.set_handle_equiv(False)
#br.addheaders = [('Host', 'api.discovery.com')]
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0')]
#br.addheaders = [('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6ImRiZmIyZmZhZWYxYmJjMmUxZGIwMGM0MjYzZTg2OThjYTBkZmQ4NTgiLCJqdGkiOiJkYmZiMmZmYWVmMWJiYzJlMWRiMDBjNDI2M2U4Njk4Y2EwZGZkODU4IiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmRpc2NvdmVyeS5jb20iLCJhdWQiOiIzMDIwYTQwYzIzNTZhNjQ1YjRiNCIsInN1YiI6eyJmbG93IjoiYW5vbnltb3VzIiwiYXV0aGVudGljYXRvciI6IkRpc2NvdmVyeSIsInV1aWQiOiJFT1MtVVNOZXRzIChXZWJcL1NpdGVzKSIsImFhdCI6MTUwNDM5MTcwN30sImV4cCI6MTUwNDM5NTMwNywiaWF0IjoxNTA0MzkxNzA3LCJ0b2tlbl90eXBlIjoiYmVhcmVyIiwic2NvcGUiOnsiY29udGVudCI6W10sInN0cmVhbWluZyI6eyJ2b2QiOnsiYXV0aGVudGljYXRlZCI6eyJmaWx0ZXIiOnsibmV0d29ya3MuY29kZSI6W119fSwidW5hdXRoZW50aWNhdGVkIjpbXX0sImxpdmUiOnsiYXV0aGVudGljYXRlZCI6eyJmaWx0ZXIiOnsibmV0d29ya3MuY29kZSI6W119fSwidW5hdXRoZW50aWNhdGVkIjpbXX19LCJzZWFyY2giOltdLCJpbWFnZXMiOnsiYXNzZXQiOltdfX19.FnkVjccXgTKe6Urw5SF8-0_aFsUH-ff9MX21BgzDpCZDXA-AsZ_3zGSBtSzNHwGYFJHq-pTVTngi-KUSLKheAxh5qF5jdJqMZcQjv1MSfxV0mJzvW2JPvAeKgE3Uwv8s0VkiMJshF3zgu8pyuWpUQsH_2BFXYhaPL36-bboeGUBysbl_e0UrmQdCWkKtL92HPrOtw86HdhVGwPGtSf_fct5xh46Bksuep5cXveoFkYy7xxZM4WMyZ14MoQBix953SClQmPtYXtct7NIuAaoF22T-FpLuy6gcDtd1k_6i_LKoUSRpK_td0_oCyrgvcS6TEShDqj4WDIxXnKhE2wcfo79WCnQpEcr83Mxt0LmyFuaJSakTV6E0pU9qQHNPLbG5uUotGkrDDmH_mmQK3-OikdUdV_1MbNu6qbKC0Jf-d1y4uMdca_W31CqmFKjzvcXdRYTr_EGgmQZnSIeRF7X90yh7x9mcFv78nDN2fOiCAe_vcw-boIfYViHYYmjObH4_U1S08XTa9QqI08R9LSCI3TXK0jUmAlpvwmkrmApifMmd4Z5xc-SLvvabOL0vHASdBbcqwesgsHyJda98chnfewabs2V0SZOC263I2IfJ8VKt9ZdJIR06qL4Udwol3w4DAWEM7qaS0F-HssN4Bbhs4EwugP6sUT9-ehzOL612lgQ')]

plugin = "Discovery Channels"

defaultimage = 'special://home/addons/plugin.video.discovery-channels/icon.png'
defaulticon = 'special://home/addons/plugin.video.discovery-channels/icon.png'
defaultfanart = 'special://home/addons/plugin.video.discovery-channels/fanart.jpg'

local_string = xbmcaddon.Addon(id='plugin.video.discovery-channels').getLocalizedString
addon_handle = int(sys.argv[1])
QUALITY = settings.getSetting(id="quality")
p = settings.getSetting(id="parser")
xbmc.log('PARSER: ' + str(p))
player = settings.getSetting(id="player")
xbmc.log('PLAYER: ' + str(player))
confluence_views = [500,501,502,503,504,508,515]

def channels():
	xbmc.log(str(platform.system()))
	xbmc.log(str(platform.release()))
	dsc = settings.getSetting(id="dsc")
	if dsc!='false':
		addDir2('Discovery Channel', 'https://www.discoverygo.com', 525, artbase + 'discovery.png')
	ap = settings.getSetting(id="ap")
	if ap!='false':
		addDir2('Animal Planet', 'https://www.animalplanetgo.com', 525, artbase + 'animalplanet.jpg')
	sci = settings.getSetting(id="sci")
	if sci!='false':
		addDir2('Discovery Science', 'https://www.sciencechannelgo.com', 525, artbase + 'sciencechannel.png')
	idsc = settings.getSetting(id="idsc")
	if idsc!='false':
		addDir2('Investigation Discovery', 'https://www.investigationdiscoverygo.com', 525, artbase + 'investigationdiscovery.jpg')
	dahn = settings.getSetting(id="dahn")
	if dahn!='false':
		addDir2('American Heroes', 'https://www.ahctvgo.com/', 525, artbase + 'ahctv.jpg')
	vel = settings.getSetting(id="vel")
	if vel!='false':
		addDir2('Velocity', 'https://www.velocitychannelgo.com', 525, artbase + 'velocity.png')
	dest = settings.getSetting(id="dest")
	if dest!='false':
		addDir2('Destination America', 'https://www.destinationamericago.com/', 525, artbase + 'destinationamerica.jpg')
	tlc = settings.getSetting(id="tlc")
	if tlc!='false':
		addDir2('TLC', 'https://www.discoverygo.com/tlc/', 525, artbase + 'tlc.jpg')
	dscl = settings.getSetting(id="dscl")
	if dscl!='false':
		addDir2('Discovery Life', 'https://www.discoverylifego.com', 525, artbase + 'discoverylife.jpg')
	dsck = settings.getSetting(id="dsck")
	if dsck!='false':
		addDir2('Discovery Kids', 'http://discoverykids.com/videos/', 535, artbase + 'discoverykids.jpg')
	views = settings.getSetting(id="views")
	if views != 'false':
		xbmc.executebuiltin("Container.SetViewMode(500)")
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#525
def dsc_menu(url):
	site = 'https://www.' + (iconimage.rsplit('/', 1)[-1]).split('.')[0] + '.com/tv-shows/'
	xbmc.log('SITE: ' + str(site))
	br.set_handle_robots( False )
	response = br.open(url)
	page = response.get_data()
	if p == '2':
		xbmc.log('PARSER: ' + 'None')
		soup = BeautifulSoup(page).find_all('div',{'class':'carousel-wrapper'})
	if p == '1':
		xbmc.log('PARSER: ' + 'html.parser')
		soup = BeautifulSoup(page,'html.parser').find_all('div',{'class':'carousel-wrapper'})
	if p == '0':
		xbmc.log('PARSER: ' + 'html5lib')
		soup = BeautifulSoup(page,'html5lib').find_all('div',{'class':'carousel-wrapper'})
	for item in soup[2:3]:
		ctitle = item.find('h3')
		xbmc.log('CTITLE: ' + str(ctitle))
	if ctitle is not None and 'Unlocked' in ctitle:
		xbmc.log('====================MATCH')
		xbmc.log('Getting Unlocked Episodes')
	plot = re.compile('data-description="(.+?)"').findall(str(item)); i = 0
	shows = re.compile('data-show-title="(.+?)"').findall(str(item))
	titles = re.compile('data-episode-title="(.+?)"').findall(str(item))
	images = re.compile('src="(.+?)width').findall(str(item))
	duration = re.compile('data-duration="(.+?)"').findall(str(item))
	dataslug = re.compile('data-slug="(.+?)"').findall(str(item))
	datashowslug = re.compile('data-show-slug="(.+?)"').findall(str(item))
	expires = re.compile('data-expiration="(.+?)"').findall(str(item))
	for item in titles:
		title = (shows[i] + ' - ' + titles[i]).replace('&amp;', '&').replace('&#x27;','\'').replace('&quot;','\'').replace('&rsquo;','\'')
		expire = (expires[i].split('T')[0]).split('-')
		year = expire[0]; month = expire[1]; day = (int(expire[2]) - 1)
		month = month.lstrip('0')
		expiry = str(month) + '/' + str(day) + '/' + str(year)
		key = datashowslug[i] + '/' + dataslug[i]
		url = 'https://www.discoverygo.com/' + str(key)
		try: description = plot[i]
		except IndexError:
			description = 'No Description Available' #plot[-1]
		description = description.replace('&amp;', '&').replace('&#x27;','\'').replace('&quot;','\'').replace('&rsquo;','\'')
		try: icon = images[i] + '&width=450&key=d06c34d5fa5f5bd74bc83'
		except IndexError:
			icon = images[-1] + '&width=450&key=d06c34d5fa5f5bd74bc83'
			icon = icon.replace('&amp;', '&')
		try: runtime = GetInHMS(int(duration[i]))
		except IndexError:
			runtime = GetInHMS(int(duration[-1]))
		add_directory3(title, url, 531, artbase + 'fanart2.jpg', icon, plot=description + ' (' + runtime.replace('00:','') + ') ' + expiry)
		xbmcplugin.setContent(addon_handle, 'episodes')
		i = i + 1
	if not 'tlc.com' in site:
		addDir('Find More Episodes From ' + name, url, 80, iconimage, artbase + 'fanart2.jpg')
		addDir(name +' Video Clips Sorted by Show', site, 533, iconimage, artbase + 'fanart2.jpg')
	#else:
		#addDir(name +' Video Clips Sorted by Show', site, 533, iconimage, artbase + 'fanart2.jpg')
		#xbmcplugin.setContent(addon_handle, 'episodes')
	views = settings.getSetting(id="views")
	if views != 'false':
		xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#80
def find_more(url):
		#site = 'https://www.' + (iconimage.rsplit('/', 1)[-1]).split('.')[0] + 'go.com'
		#xbmc.log(site
		#base = url.partition('/')[0]
		#xbmc.log(base
		br.set_handle_robots( False )
		response = br.open(url)
		page = response.get_data()
		if p == '2':
			xbmc.log('PARSER: ' + 'None')
			soup = BeautifulSoup(page).find_all('div',{'class':'item small'})
		if p == '1':
			xbmc.log('PARSER: ' + 'html.parser')
			soup = BeautifulSoup(page,'html.parser').find_all('div',{'class':'item small'})
		if p == '0':
			xbmc.log('PARSER: ' + 'html5lib')
			soup = BeautifulSoup(page,'html5lib').find_all('div',{'class':'item small'})
		#soup4 = BeautifulSoup(html).find_all('div',{'class':'item small'})
		xbmc.log ('SOUP: ' + str(len(soup)))
		for item in soup:
			title = (item.find('img')['alt']).encode('utf-8').replace('&amp;', '&').replace('&#x27;','\'').replace('&quot;','\'').replace('&rsquo;','\'')
			xbmc.log('TITLE: ' + str(title))
			expire = str(re.compile('data-expiration="(.+?)"').findall(str(item))[-1]).split('T')[0].split('-')
			#expire = (expire.split('T')[0]).split('-')
			year = expire[0]; month = expire[1].lstrip('0'); day = (int(expire[2]) - 1)
			#month = month.lstrip('0')
			expiry = str(month) + '/' + str(day) + '/' + str(year)
			pageurl = 'https://www.discoverygo.com' + item.find('a')['href']
			try: description = item.find('p').text.strip()
			except TypeError:
				description = 'No Description Available' #plot[-1]
			description = description.replace('&amp;', '&').replace('&#x27;','\'').replace('&quot;','\'').replace('&rsquo;','\'').encode('utf-8')
			icon = item.find('img')['src']
			duration = re.compile('data-duration="(.+?)"').findall(str(item))[-1]
			runtime = GetInHMS(int(duration))
			add_directory3(title, pageurl, 531, artbase + 'fanart2.jpg', icon, plot=description + ' (' + runtime.replace('00:','') + ') ' + expiry)
		xbmcplugin.setContent(addon_handle, 'episodes')
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
		xbmcplugin.endOfDirectory(addon_handle)


#531
def discovery_shows(name,url):
		r = requests.get(url)
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie', r.cookies))
		f = opener.open(url)
		page = f.read()
		try: m3u8 = re.compile('streamUrl(.+?)hdsStreamUrl').findall(page)[0]
		except IndexError:
			xbmcgui.Dialog().notification(name, ' Episode Not Available', iconimage, 5000, False)
			return
		if QUALITY =='2':
			url = (str(m3u8.replace('\/','/'))[13:-13])
		elif QUALITY =='1':
			url = (str(m3u8.replace('\/','/'))[13:-13]).replace('4500k,', '')
		elif QUALITY =='0':
			url = (str(m3u8.replace('\/','/'))[13:-13]).replace('2200k,3000k,4500k,', '')
		#description = (re.compile('detailed(.+?)}').findall(page)[0]).replace('&quot;','').replace(':','')
		if player != '0':
			play(url)
		else:
			PLAY(name,url)
		xbmcplugin.endOfDirectory(addon_handle)


#532
def discovery_clips(url, iconimage):
	site = url.split('/tv')[0]
	try: html = urllib2.urlopen(url)
	except urllib2.HTTPError:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	#try: dscdata = json.load(response)
	#except ValueError:
		#xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		#return
	#list_clips(dscdata)
	soup = BeautifulSoup(html,'html5lib').find_all("a",{"class":"thumbnailTile__link"})
	#xbmc.log(soup[0]
	for item in soup:
		title = item.find('div',{'class':'thumbnailTile__lineTwo'}).text.encode('ascii', 'ignore')
		if 'Season' in title:
			continue
		link = site + item.get('href')
		add_directory2(title, link, 550, artbase + 'fanart2.jpg', iconimage,plot='')
	xbmcplugin.endOfDirectory(addon_handle)


#550
def get_clips(name,url):
	r = requests.get(url)
	video_id = re.compile('platform=desktop&video_id=(.+?)&networks').findall(str(r.content))[0]
	xbmc.log('VIDEO_ID: ' + str(video_id))
	video_url = 'http://api.discovery.com/v1/streaming/video/' + video_id + '?platform=desktop'
	opener = urllib2.build_opener()
	xbmc.log('COOKIES LENGTH: ' + str(len(r.cookies)))
	if len(str(r.cookies)) < 1:
		xbmcgui.Dialog().notification(name, 'Currently Unavailable.  Try Again Later', iconimage, 5000, False)
		xbmc.log('CURRENTLY UNAVAILABLE')
		return
	#xbmc.log('COOKIES: ' + str(r.cookies))
	#xbmc.log(r.request.headers
	#auth = re.findall(r'%2522%253A%2522.*\n', str(r.cookies), flags=re.MULTILINE)
	auth = 'Bearer ' + re.compile('%2522%253A%2522(.+?)%2522%252C%2522').findall(str(r.cookies))[0]
	opener.addheaders.append(('Host', 'api.discovery.com'))
	opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0'))
	opener.addheaders.append(('Referer', url))
	opener.addheaders.append(('Authorization', auth))
	f = opener.open(video_url)
	page = f.read()
	jsob = json.loads(page)
	stream = jsob['streamUrl']
	xbmc.log('STREAM: ' + str(stream))
	PLAY(name,stream)
	xbmcplugin.endOfDirectory(addon_handle)


#533
def other_shows(url, iconimage):
	xbmc.log('ICONIMAGE: ' + str(iconimage))
	site = url.replace('/tv-shows/','')
	xbmc.log('SITE: ' + str(site))
	#add_directory2('Search', url, 538, artbase + 'fanart2.jpg', iconimage,plot='')
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib').find_all("div",{"class":"headerMain__showDropDesktop"})[0]
	for show in soup.find_all("a")[1:]:
		tvshow = show.text.encode('utf-8')#.replace("\\'","'")
		if not 'tlc.com' in url:
			link = site + show.get('href')#url.replace('videos', 'tv-shows') + show.get('data-ssid').split('/')[-1] + '?flat=1'
			mode = 532
		else:
			link = url.replace('videos', 'tv-shows') + show.get('data-ssid').split('/')[-1] + '?flat=2'
			mode = 534
		if 'aerospace' in link:
			continue
			#xbmc.log('LINK: ' + str(link))
		#if 'velocity' in url:
			#link = velocity_clips(link)
			#mode = 542
		#else:
			#link = url.replace('videos', 'tv-shows') + show.get('data-ssid').split('/')[-1] + '?flat=2'
		#mode = 534
		add_directory2(tvshow, link, mode, artbase + 'fanart2.jpg', iconimage,plot='')
		#xbmc.log(link
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#534
def tlc_clips(url, iconimage):
	html = get_html(url)
	try: soup = BeautifulSoup(html,'html5lib').find_all("div",{"class":"grid-wrapper"})[0]
	except TypeError:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	for show in soup.find_all("div",{"class":"caption table-cell"}):
		paragraph = str(show.find('p',{'class': 'extra video'}))
		if paragraph == 'None':
			continue
		tvshow = str(show.find('a'))
		tvshow =  re.compile('">(.+?)</a>').findall(tvshow)[0]
		link = show.find('a')['href']
		link = link + '?flat=1'
		add_directory2(tvshow, link, 532, artbase + 'fanart2.jpg', iconimage,plot='')
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#535
def dsc_kids(url):
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib').find_all("ul",{"class":"dropdown-menu"})
	soup = str(soup).split('</a>'); i = 0
	while i < 9:
		cat = re.compile('data-category="(.+?)"').findall(str(soup))[i]
		if i == 0:
			cat = 'all'
			link = 'http://discoverykids.com/app/themes/discoverykids/ajax-load-more/ajax-load-more.php?postType=video&taxonomyName=category&taxonomyTerm=&orderBy=post_date&order=DESC&device=computer&numPosts=24&onScroll=false&pageNumber=1'
		else:
			link = 'http://discoverykids.com/app/themes/discoverykids/ajax-load-more/ajax-load-more.php?postType=video&taxonomyName=category&taxonomyTerm=' + cat + '&orderBy=post_date&order=DESC&device=computer&numPosts=24&onScroll=false&pageNumber=1'
		title = cat.title()
		i = i + 1
		add_directory2(title, link, 536, artbase + 'fanart2.jpg', iconimage,plot='')
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#536
def kids_clips(url,iconimage):
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib').find_all("div",{"class":"thumbnail super-item"})
	for item in soup:
		title = item.find('div',{'class':'caption'})
		plot = (striphtml(str(title)).strip()).splitlines()[-1]
		title = (striphtml(str(title)).strip()).splitlines()[0]
		title = sanitize(title)
		image = item.find('img')['src']
		link = item.find('a')['href']
		add_directory3(title, link, 537, artbase + 'fanart2.jpg', image,plot)
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#537
def kids_stream(name,url):
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib')
	try: url = soup.find('iframe')['src']
	except TypeError:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	if 'facebook' in url:
		html = get_html(url)
		stream = (re.compile('hd_src_no_ratelimit":"(.+?)"').findall(str(html))[0]).replace('\\','')
		xbmc.log('STREAM: ' + str(stream))
	else:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	play(stream)
	xbmcplugin.endOfDirectory(addon_handle)


#538
def search(url):
	if 'velocity' in url:
		url=url.replace('videos-2/', 'search/?q=')
	url = url.replace('videos/', 'search/?q=')
	xbmc.log('SEARCH URL: ' + str(url))
	keyb = xbmc.Keyboard('', 'Search')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		xbmc.log('SEARCH: ' + str(search))
		url = url + search.replace(' ','+')
	xbmc.log('SEARCH URL: ' + str(url))
	get_search(url)


#539
def get_search(url):
	site = re.compile('www.(.+?).com').findall(url)
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib').find_all("div",{"class":"item"})
	try :nextpage = 'http://www.' + site[0] + '.com' + re.compile('href="(.+?)"><div class="next').findall(str(html))[-1]
	except IndexError:
		return
	for item in soup:
		title = striphtml(str(item.find('h4'))).split(' | ')[0]
		xbmc.log('TITLE: ' + str(title))
		try: icon = item.find('img')['src']
		except TypeError:
			icon = defaulticon
		url = item.find('a')['href']
		if not 'videos' in url:
			continue
		post_url = url.split('videos')[-1]
		if len(post_url) < 2:
			continue
		xbmc.log('URL: ' + str(url))
		description = striphtml(str(item.find('div',{'class':'item-detail'}))).replace('\n','').strip().split('http')[0]
		add_directory3(title, url, 540, artbase + 'fanart2.jpg', icon, plot=description)# + ' (' + runtime.replace('00:','') + ')')
	add_directory2('Next Page', nextpage, 539, artbase + 'fanart2.jpg', iconimage, plot='')
	views = settings.getSetting(id="views")
	if views != 'false':
		xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


#540
def search_streams(url):
	html = get_html(url)
	try: m3u8 = ((re.compile('referenceId":"(.+?)m3u8"').findall(str(html))[0]).replace('\\', '') + 'm3u8').split('"src":"')[-1]
	except IndexError:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	xbmc.log('SEARCH M3U8: ' + str(m3u8))
	play(m3u8)


#541
def velocity_clips(url):
	#key = url.split('/')[-1]
	#key = key.replace('?flat=1','-2')
	link = url.replace('?flat=1', '/').replace('-2/','/')
	return link


#542
def get_json(url):
	html = get_html(url)
	soup = BeautifulSoup(html,'html5lib')
	data = re.compile('var initialVideoData = (.+?);</script>').findall(str(soup))[-1]
	xbmc.log ('DATA LENGTH: ' + (str(len(data))))
	try: dscdata = json.loads(data)
	except ValueError:
		xbmcgui.Dialog().notification(name, ' No Streams Available', iconimage, 5000, False)
		return
	list_clips(dscdata)


def list_clips(dscdata):
	i=0
	if not 'nextVideosList' in dscdata:
		xbmcgui.Dialog().notification(name, ' No Streams Found - Try the Search Function', iconimage, 5000, False)
		return
	for title in dscdata["nextVideosList"]:
		title = (dscdata["nextVideosList"][i]["post_title"])
		description = (dscdata["nextVideosList"][i]["video"]["description"])
		iconimage = (dscdata["nextVideosList"][i]["video"]["thumbnailUrl"])
		duration = (dscdata["nextVideosList"][i]["video"]["duration"])
		url = (dscdata["nextVideosList"][i]["video"]["src"])
		if QUALITY =='1':
			url = url.replace('4500k,', '')
		elif QUALITY =='0':
			url = url.replace('2200k,3000k,4500k,', '')
		i = i + 1
		infoLabels = {'title':title,
					  'tvshowtitle':title,
					  'plot':description}
		li = xbmcgui.ListItem(title, iconImage= iconimage, thumbnailImage= iconimage)
		li.setProperty('fanart_image', artbase + 'fanart2.jpg')
		li.setInfo(type="Video", infoLabels=infoLabels)
		li.addStreamInfo('video', { 'duration': duration })
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, totalItems=15)
		xbmcplugin.setContent(addon_handle, 'episodes')
		views = settings.getSetting(id="views")
		if views != 'false':
			xbmc.executebuiltin("Container.SetViewMode("+str(confluence_views[3])+")")
	xbmcplugin.endOfDirectory(addon_handle)


def GetInHMS(seconds):
	hours = seconds / 3600
	seconds -= 3600*hours
	minutes = seconds / 60
	seconds -= 60*minutes
	ti = "%02d:%02d:%02d" % (hours, minutes, seconds)
	ti = str(ti)
	return ti


def striphtml(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)


def sanitize(data):
	output = ''
	for i in data:
		for current in i:
			if ((current >= '\x20') and (current <= '\xD7FF')) or ((current >= '\xE000') and (current <= '\xFFFD')) or ((current >= '\x10000') and (current <= '\x10FFFF')):
			   output = output + current
	return output


#99
def PLAY(name,url):
	listitem = xbmcgui.ListItem(name, thumbnailImage = defaultimage)
	listitem.setInfo(type="Video", infoLabels={"Title": name})
	listitem.setProperty('IsPlayable', 'true')
	xbmc.Player().play( url + '&m3u8=yes', listitem )
	while xbmc.Player().isPlaying():
		continue
	sys.exit()
	xbmcplugin.endOfDirectory(addon_handle)


#999
def play(url):
	xbmc.log('URL: ' + str(url))
	item = xbmcgui.ListItem(path=url + '&m3u8=yes')
	item.setProperty('IsPlayable', 'true')
	return xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


def add_directory2(name,url,mode,fanart,thumbnail,plot):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
		liz.setInfo( type="Video", infoLabels={ "Title": name,
												"plot": plot} )
		if not fanart:
			fanart=''
		liz.setProperty('fanart_image',fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True, totalItems=40)
		return ok


def add_directory3(name,url,mode,fanart,thumbnail,plot):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
		liz.setInfo( type="Video", infoLabels={ "Title": name,
												"plot": plot} )
		if not fanart:
			fanart=''
		liz.setProperty('fanart_image',fanart)
		liz.setProperty('IsPlayable', 'true')
		#liz.setProperty('mimetype', 'application/x-mpegURL')
		#liz.setProperty('mimetype', 'vnd.apple.mpegURL')
		#commands = []
		#commands.append
		#li.addContextMenuItems([('Download File', 'XBMC.RunScript(special://home/addons/plugin.video.discovery-channels/downloader.py)',)])
		#liz.addContextMenuItems([('Find More Episodes', 'XBMC.RunPlugin(%s?mode=80&url=%s)' % (addon_handle, url))])
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False, totalItems=40)
		return ok


def get_html(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent','User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0')

	try:
		response = urllib2.urlopen(req)
		html = response.read()
		response.close()
	except urllib2.HTTPError:
		response = False
		html = False
	return html


def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring) >= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params) - 1] == '/'):
			params = params[0:len(params) - 2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]

	return param

def addDir(name, url, mode, iconimage, fanart=True, infoLabels=True):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
		ok = True
		liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo(type="Video", infoLabels={"Title": name})
		liz.setProperty('IsPlayable', 'true')
		if not fanart:
			fanart=defaultfanart
		liz.setProperty('fanart_image', artbase + 'fanart2.jpg')
		ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
		return ok


def addDir2(name,url,mode,iconimage, fanart=False, infoLabels=True):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		if not fanart:
			fanart=defaultfanart
		liz.setProperty('fanart_image', artbase + 'fanart5.jpg')
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok


def addDirectoryItem2(name, isFolder=True, parameters={}):
	''' Add a list item to the XBMC UI.'''
	li = xbmcgui.ListItem(name, iconImage=defaultimage, thumbnailImage=defaultimage)
	li.setProperty('fanart_image', defaultfanart)
	url = sys.argv[0] + '?' + urllib.urlencode(parameters)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=isFolder)


def unescape(s):
	p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()




params = get_params()
url = None
name = None
mode = None
cookie = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass

xbmc.log("Mode: " + str(mode))
xbmc.log("URL: " + str(url))
xbmc.log("Name: " + str(name))

if mode == None or url == None or len(url) < 1:
	xbmc.log("Discovery Channels")
	channels()
elif mode==80:
	xbmc.log("Find More")
	find_more(url)
elif mode==525:
	xbmc.log("DSC Menu")
	dsc_menu(url)
elif mode==530:
	xbmc.log("Discovery Menu")
	discovery_menu(url)
elif mode==531:
	xbmc.log("Discovery Shows")
	discovery_shows(name,url)
elif mode==532:
	xbmc.log("Discovery Clips")
	discovery_clips(url, iconimage)
elif mode==533:
	xbmc.log("Other Clips")
	other_shows(url, iconimage)
elif mode==534:
	xbmc.log("Get TLC Clips")
	tlc_clips(url, iconimage)
elif mode==535:
	xbmc.log("Get DSC Kids")
	dsc_kids(url)
elif mode==536:
	xbmc.log("Get Kids Clips")
	kids_clips(url, iconimage)
elif mode==537:
	xbmc.log("Get Kids Stream")
	kids_stream(name,url)
elif mode==538:
	xbmc.log("Search")
	search(url)
elif mode==539:
	xbmc.log("Get Search")
	get_search(url)
elif mode==540:
	xbmc.log("Search Streams")
	search_streams(url)
elif mode==541:
	xbmc.log("Velocity Clips")
	velocity_clips(url)
elif mode==542:
	xbmc.log("Velocity JSON")
	get_json(url)
elif mode==550:
	xbmc.log("Get Clips")
	get_clips(name,url)
elif mode == 99:
	xbmc.log("PLAY Video")
	PLAY(name,url)
elif mode==999:
	xbmc.log("Play Video")
	play(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
