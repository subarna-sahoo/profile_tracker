# 👁️‍🗨️ profile_tracker
Track your GitHub visitors with custom SVG badges, and log their device & location — just for fun 🛰️

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Visitors](https://img.shields.io/badge/Profile%20Views-Live--Tracked-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ⚙️ Features

- 📊 Track GitHub profile views
- 🌍 Get location and device info
- 🖼️ Serve custom SVG badges
- 💾 Store everything in a database

---

## 🛠️ Run Locally

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
chmod +x run.sh
./run.sh          # uvicorn on http://localhost:8000
```

Views are stored in a local SQLite database (`profile_tracker.db`), and tables are created on startup.

---

## 📡 API

| Method | Path | Description |
|---|---|---|
| `GET` | `/api/view?username=<name>` | Logs the visit (IP, user agent, referrer, country/city) and returns an SVG badge with the total view count. Bots and crawlers are ignored. |
| `GET` | `/api/logs?username=<name>` | Last 50 visits as JSON |

---

## 🧪 Add It to Your Profile

Deploy the app somewhere public, then add this to your GitHub profile README:

```html
<img src="https://yourdomain.com/api/view?username=subarna-sahoo" />
```

To test locally, open <http://localhost:8000/api/view?username=subarna-sahoo> in a browser.

---

## 🗂️ Project Structure

```
profile_tracker/
├── main.py
├── models.py                # ViewLog model
├── models/                  # SQLAlchemy base
├── database.py
├── schemas.py
├── utils/
│   ├── svg_generator.py
│   ├── geoip.py
├── views/
│   └── tracker.py
├── alembic/                 # Migrations (optional)
├── requirements.txt
├── README.md
└── run.sh
```

---

## 📝 License

This project is licensed under the MIT License.

