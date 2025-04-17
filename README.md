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
chmod +x run.sh
./run.sh
```

---

## 🧪 How This Will Look

```html
<img src="https://yourdomain.com/api/view?username=subarna-sahoo" />
```

Live Example (on localhost):
<img src="https://localhost:5000/api/view?username=subarna-sahoo" />

---

## 🗂️ Project Structure

```
profile_tracker/
├── main.py
├── models.py
├── database.py
├── schemas.py
├── utils/
│   ├── svg_generator.py
│   ├── geoip.py
├── views/
│   └── tracker.py
├── alembic/ (optional for migrations)
├── .env
├── requirements.txt
├── README.md
└── run.sh
```

---

## 📝 License

This project is licensed under the MIT License.

