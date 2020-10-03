from __future__ import unicode_literals
import os, sys, re, youtube_dl, wget, ffmpeg, taglib


dirBase = "/run/media/jediiah/My Book/Musique_WD/Riff Dealer/YoutubeDL"
albumDir = ""

def getDescriptionInfos(albumInfos=dict):
    global dirBase, albumDir
    
    descriptionStr = albumInfos["description"]
    
    rePatern = r'\d{0,2}\.?(.*[^0123456789:])(\d{1,2}:\d{2}:{0,1}\d{0,2})'
    result = re.findall(rePatern, descriptionStr)
    
    for i in range (len(result)):
        songName = result[i][0]
        forbiddenChars = " -."
        while (songName[0] in forbiddenChars or songName[-1] in forbiddenChars):
            if songName[0] in forbiddenChars:
                songName = songName[1:]
            if songName[-1] in forbiddenChars:
                songName = songName[0:-1]
        result[i] = (songName, result[i][1])

    title = albumInfos['title']
    splitTitle = re.split(r'\s-\s', title)
    albumInfos["year"] = re.search(r'\d{4}', title).group()
    albumInfos["artist"] = splitTitle[0]
    albumInfos["album"] = re.findall(r'(.*)\s\(.*\)', splitTitle[1])[0]
    albumInfos["tracks"] = result
    
    albumDir = os.path.join(dirBase, "{artist}-{album}_{date}".format(artist=albumInfos['artist'].replace(' ', '_'), album=albumInfos['album'].replace(' ', '_'), date=albumInfos['year']))
    
    try:
        os.mkdir(albumDir)
    except OSError as error:
        print(error)
        
    albumInfos["thumbnail_url"] = wget.download("http://img.youtube.com/vi/{id}/sddefault.jpg".format(id=albumInfos['id']), out="{dir}/folder.jpg".format(dir=albumDir))
       
    return(albumInfos)



def DL_Ytb(url=str):
    global dirBase
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',
            'preferredquality': '9'
        }],
        'outtmpl': r"{dir}/ytbdl_temp.%(ext)s".format(dir=dirBase),
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        info_dict = ydl.extract_info(url, download=True)
        
        albumInfos = {
            'description' : info_dict['description'],
            'id' : info_dict['id'],
            'title' : info_dict['title'],
            'thumnail_url' : "",
            'audio_url' : "{dir}/ytbdl_temp.ogg".format(dir=dirBase),
            'year' : "",
            'artist' : "",
            'album' : "",
            'tracks' : []
        }
        
    return(albumInfos)


def createTracks(albumInfos=dict):
    global dirBase, albumDir
    
    tracks = albumInfos['tracks']
    
    for i in range (len(tracks)):
        if i<(len(tracks)-1):
            trackTitle = tracks[i][0]
            trackStart = tracks[i][1]
            trackStop = tracks[i+1][1]
            
            fileOutName = "{dir}/{trackNumber}-{trackTitle}.ogg".format(dir=albumDir, trackNumber=i+1, trackTitle=trackTitle.replace(' ', '_'))
            trackAudio = ffmpeg.input(albumInfos['audio_url'], ss=trackStart, to=trackStop).output(fileOutName, c='copy').run()
            
        elif i==(len(tracks)-1):
            trackTitle = tracks[i][0]
            trackStart = tracks[i][1]
            
            fileOutName = "{dir}/{trackNumber}-{trackTitle}.ogg".format(dir=albumDir, trackNumber=i+1, trackTitle=trackTitle.replace(' ', '_'))
            trackAudio = ffmpeg.input(albumInfos['audio_url'], ss=trackStart).output(fileOutName, c='copy').run()

        tagFile = taglib.File(fileOutName)
        tagFile.tags = {
            'ARTIST': [albumInfos['artist']],
            'ALBUM': [albumInfos['album']],
            'DATE': [albumInfos['year']],
            'TITLE': [trackTitle],
            'TRACKNUMBER': ['{trckNbr}/{total}'.format(trckNbr=i+1, total=len(tracks))] 
        }
        tagFile.save()
        
    os.remove(albumInfos['audio_url'])
        
        

Ytb_url = sys.argv[1]

history = open("{dir}/history.txt".format(dir=dirBase), 'r')

if Ytb_url in history.read():
    print("Album already downloaded : Abort the Mission !!!!")
else:
    infosDL = DL_Ytb(Ytb_url)
    infosPlus = getDescriptionInfos(infosDL)
    createTracks(infosPlus)
    
    history = open("{dir}/history.txt".format(dir=dirBase), 'a')
    history.write(Ytb_url+"\n")
    
