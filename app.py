from flask import Flask, render_template
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.route("/")
def home():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "✅ Database Connected"
    except Exception as e:
        db_status = f"❌ DB Error: {e}"

    return render_template("index.html", status=db_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
