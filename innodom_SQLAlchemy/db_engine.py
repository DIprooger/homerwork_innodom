import os
from dotenv import load_dotenv
from urllib.parse import quote

BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_SQLAlchemy'
env = load_dotenv(os.path.join(BASE_DIR, '.env'))
db_url = (f"postgresql://{os.getenv('DB_USER_POS')}:{quote(os.getenv('DB_PASSWORD_POS'))}"
          f"@{os.getenv('DB_HOST_POS')}:{os.getenv('DB_PORT_POS')}/{os.getenv('DB_NAME_POS')}")
