import json
import os
import requests
import telebot
from telebot import types

# التوكن - يقرأه من Render ولو مش موجود يستخدم ده
BOT_TOKEN = os.getenv("BOT_TOKEN", "8828660771:AAFrzqaH4ScJR8ZgGijxj4kxTE90uZxjVuc")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8828660771"))
CHANNEL_USERNAME = '@CR7SKREPT'
DATA_FILE = 'users_data.json'
DEFAULT_POSTER = 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800'

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML', threaded=False)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'Error saving: {e}')

def register_user(user_id, username='', first_name=''):
    data = load_data()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {'username': username, 'first_name': first_name or 'مستخدم', 'usage_count': 1, 'rating': 0, 'favorites': {'movies': {}, 'series': {}}}
    else:
        data[uid]['usage_count'] = data[uid].get('usage_count', 0) + 1
    save_data(data)
    return data

def check_subscription(user_id):
    if user_id == ADMIN_ID:
        return True
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['creator', 'administrator', 'member']
    except:
        return True

def send_sub_required_message(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    ch_clean = CHANNEL_USERNAME.replace('@', '')
    markup.add(
        types.InlineKeyboardButton('📢 اشترك في القناة', url=f'https://t.me/{ch_clean}'),
        types.InlineKeyboardButton('✅ تحقق من الاشتراك', callback_data='check_sub')
    )
    bot.send_message(chat_id, f"⚠️ يجب الاشتراك في {CHANNEL_USERNAME} أولاً", reply_markup=markup)

# باقي كود الـ API والكيبورد زي ما هو...
class OscarAPI:
    OSCAR_URL = 'https://mode.giize.com/OscarTV.php'
    MOVIES_URL = 'https://ostvapp.cam/api/movies/'
    MOVIE_DETAILS_URL = 'https://ostvapp.cam/api/movies/show.php'
    SERIES_URL = 'https://ostvapp.cam/api/series/'
    SERIES_DETAILS_URL = 'https://ostvapp.cam/api/series/show.php'
    ANIME_URL = 'https://ostvapp.cam/api/anime/'
    ANIME_DETAILS_URL = 'https://ostvapp.cam/api/anime/show.php'
    ANIME_EPISODES_URL = 'https://ostvapp.cam/api/anime/episodes/'
    EPISODES_URL = 'https://ostvapp.cam/api/episodes/'
    EPISODE_DETAILS_URL = 'https://ostvapp.cam/api/episodes/show.php'
    ANIME_EPISODE_DETAILS_URL = 'https://ostvapp.cam/api/anime/episodes/show.php'
    WRESTLING_URL = 'https://ostvapp.cam/api/wrestling/'
    WRESTLING_DETAILS_URL = 'https://ostvapp.cam/api/wrestling/show.php'

    def __init__(self, timeout=25):
        self.timeout = timeout
        self.session = requests.Session()

    def get_headers(self, target_url):
        try:
            res = self.session.post(self.OSCAR_URL, data={'link': target_url}, timeout=self.timeout)
            if res.status_code == 200:
               
