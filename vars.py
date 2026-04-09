# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

from os import environ

API_ID = int(environ.get("API_ID", "34422904")) #Replace with your api id
API_HASH = environ.get("API_HASH", "7e0002469784f47fc08a6b3d93d7ebed") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "8684246543:AAHSspI4eNVh6IikZ9uCbNt6j-J-nWcFjuA") #Replace with your bot token

# Database Configuration for MongoDB
# Example: "mongodb://user:password@host:port/dbname"
# For MongoDB Atlas: "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<dbname>?retryWrites=true&w=majority"
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://adarshppandey937:uIoPcln9vXQBF0vP@cluster0.o9mn6hb.mongodb.net/?")
# Replace "your_bot_db" with your desired database name.
# For local testing, you might use "mongodb://localhost:27017/your_bot_db"
# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))

