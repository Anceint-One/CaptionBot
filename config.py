import os

API_ID = int(os.environ.get("API_ID",25924286 ))
API_HASH = os.environ.get("API_HASH", "3efefa73f4fa328187e22f49ee6f2af4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8508953142:AAE-xLsD9NEs5gdUkARJ0BadBJs6Vgt9ITM")

ADMIN_ID = int(os.environ.get("ADMIN_ID",6458656428 ))

_raw = os.environ.get("ALLOWED_CHATS", "-1002150284851")
ALLOWED_CHATS = [int(x.strip()) for x in _raw.split(",") if x.strip()]

LOG_FORMAT = os.environ.get(
    "LOG_FORMAT",
    "[%(asctime)s][%(name)s][%(module)s][%(lineno)d][%(levelname)s] -> %(message)s",
)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

GC_THRESHOLD = (
    int(os.environ.get("GC_THRESHOLD_0", 500)),
    int(os.environ.get("GC_THRESHOLD_1", 5)),
    int(os.environ.get("GC_THRESHOLD_2", 5)),
)

CAPTION_TEMPLATE = os.environ.get(
    "CAPTION_TEMPLATE",
    "<b>{title}</b>\n\n"
    "🎬 <b>{video_line}</b> | ⏳ <b>{duration}</b>\n"
    "🔊 <b>{audio}</b>\n"
    "💬 <b>{subtitle}</b>\n\n"
)

# --- MongoDB ---
MONGO_URI = os.environ.get("MONGO_URI", "")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "mediainfo_bot")

# --- Upstream ---
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "")      # e.g. https://github.com/user/MediaInfo-Bot
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

# --- Helper Bots ---
_helper_tokens_raw = os.environ.get("HELPER_TOKENS", "8479917977:AAGyc53Aoip8tS132lnn_U5xNpySYuGBBAg 8338573598:AAFeUZqvR4nfsoC4D-msNHWX3o8eW3v_uzA 7271648965:AAFetaWMblIGUM6z-izlE0iNZZw8SwTcbMg 7477967875:AAF47JVr3wTmC1IgMWy3DNg7uoAMY9fTia8 7304338435:AAGn1Fpzeh0aXxAhng02ivy1EfEeqr7dCPY 7479025542:AAEOZVDkUkZI5DJCIs__zBECeD78xv1INxE 7160916761:AAGgiM4IF-gwy5GrX-7B85-S97Xuux-Ilu4 6423771535:AAGiaorYfLuBl4vUUc4vymj4CQy6sLVfZd4")
HELPER_TOKENS = [x.strip() for x in _helper_tokens_raw.split() if x.strip()]

