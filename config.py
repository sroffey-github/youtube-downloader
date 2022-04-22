from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import platform, os, urllib.request, re, logging, datetime, youtube_dl

load_dotenv()

CURRENT_PATH = os.getcwd()
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')
LOG_PATH = os.getenv('LOG_PATH')

search_url = 'https://www.youtube.com/results?search_query='
video_url = 'https://www.youtube.com/watch?v='

def clear():
    if 'windows' in platform.system().lower():
        os.system('cls')
    else:
        os.system('clear')
        
def log(err):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(LOG_PATH, maxBytes=10485760, backupCount=5)
    logger.addHandler(handler)
    
    logger.info('[{}] '.format(str(datetime.datetime.now(), err)))
        
def search(query):
    top_results = []
    
    url = search_url + query.strip().replace(' ', '%20')
    html = urllib.request.urlopen(url)
    
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for vid in video_ids:
        if len(top_results) == 3:
            return top_results
        top_results.append(video_url + vid)
        
def download(link, mode):
    os.chdir(DOWNLOAD_PATH)
    
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = link, download=False
    )
    
    filename = f"{video_info['title']}.mp3"
    
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    os.chdir(CURRENT_PATH)

    return True