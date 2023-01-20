##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQCdDLjbdJcEiMsNFyk6T0W-wjLfBfHPS2wPnG5psboGVZfdXup0uOrx2Rn_nLQHjhcZZ3qe9z2oiLq6d0EiTQtHGNfe1_OQlki2wL5AwBOBwyf1hQJWvBv53zfs8Evo_EvuNWY77QxZSMIrH-vzUq0FWmV0sMhlG74KzA_G4ysYoZuObO2CnUQV9fnmxTYJUrUg-M99abEVf0GPiYv68ZtPEA8DAmVGB2g9IsmxKREpDLLESs7VzL1WMKumt0Ynyyd7kEn9fqUpz0AlJUzT-8IetPVPEh_NvjDH7EPTbLTf99nA0tNy4lr_sOSpjrNpKwZROEKm1F8MRz96wtYp85RXAAAAAVGnG2QA')
BOT_TOKEN = getenv('BOT_TOKEN', '5989100103:AAEgrSJBumngRO278Bd0CtkZ1Knv9vyw3bg')
API_ID = int(getenv("API_ID", "3974784"))
API_HASH = getenv('API_HASH', 'c58c42689bdd066c7e64af20484a34f7')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! .').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://cyberop:cyberop@cyberop.vpddu.mongodb.net/cyberop?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001668224190'))
ASS_ID = int(getenv("ASS_ID", "5001717969"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5001717969').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/62c6a23532aed6f4def02.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/85c226cce124d25c5b2ad.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
