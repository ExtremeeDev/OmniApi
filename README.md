# 👽 OmniApi

The most detailed and complete Ben 10 API on the internet. Get base stats, attacks, accuracy, and images of your favorite aliens!

## 👨‍💻 Developer
Built with ❤️ by **[@ExtremeeDev](https://t.me/ExtremeeDev)**. 

## 🚀 Features
- 📊 Game-like stats for every alien (Power, Speed, Defense, Accuracy).
- ⚔️ Detailed attacks (Damage, Accuracy, Type).
- 🖼️ Direct image hosting without third-party URL dependencies.
- ⚡ Fast and lightweight (Built with Flask).

## 🔗 Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API Status and Info |
| `GET` | `/api/aliens` | Fetch data of all available aliens |
| `GET` | `/api/aliens/<name>` | Fetch data of a specific alien (e.g., `heatblast`) |
| `GET` | `/assets/images/<file>`| Fetch alien image (e.g., `heatblast.jpg`) |

## 🛠️ How to Run Locally (Termux / Linux)
1. Install requirements: `pip install -r requirements.txt`
2. Run the server: `python run.py`
3. Enjoy the OmniApi on `http://localhost:5000`
