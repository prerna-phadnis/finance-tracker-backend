import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("DATABASE_HOST"))  # should print localhost

from app import create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)