<!-- Badges Section (Auto-updating stats) -->
<p align="center">
  <img src="https://img.shields.io/github/stars/ExtremeeDev/OmniApi?style=for-the-badge&color=green&logo=github" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/ExtremeeDev/OmniApi?style=for-the-badge&color=blue&logo=github" alt="Forks"/>
  <img src="https://img.shields.io/github/issues/ExtremeeDev/OmniApi?style=for-the-badge&color=red&logo=github" alt="Issues"/>
  <img src="https://img.shields.io/github/license/ExtremeeDev/OmniApi?style=for-the-badge&color=yellow" alt="License"/>
</p>

<!-- Hero Section with Animation -->
<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjM3ZTIzYTIzYTIzYTIzYTIzYTIzYTIzYTIzYTIzYTIzYTIzYTIzYyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7TKrEzvLbsVAud8I/giphy.gif" alt="Ben 10 Omnitrix Animation" width="250"/>
  
  # 🧬 OMNI-API
  **The Most Detailed & Badass Ben 10 API on the Internet.**
  
  *Get game-ready stats, attack accuracies, and direct images of your favorite aliens!*
</div>

---

## 👨‍💻 Developed By

<div align="left">
  <a href="https://t.me/ExtremeeDev" target="_blank">
    <img src="https://img.shields.io/badge/Telegram-@ExtremeeDev-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=101010" alt="Developer Telegram"/>
  </a>
</div>
<br>

## 🚀 Features (Why OmniApi?)

Unlike other basic APIs, OmniApi is built for gamers, bot developers, and hardcore fans:
- **📊 Game-Ready Stats:** Every alien comes with balanced `Power`, `Speed`, `Defense`, and `Accuracy` stats (1-100 scale).
- **⚔️ Detailed Attacks:** Not just names! Get `Damage`, `Accuracy`, and `Attack Type` (Melee, Ranged, AoE, Utility).
- **🖼️ Direct Local Images:** No broken Imgur links. We serve high-quality images directly from our server.
- **⚡ Blazing Fast:** Built with Flask for instant JSON responses.

---

## 🔗 Endpoints & Usage

### Base URL: `http://localhost:5000` (or your hosted domain)

| Method | Endpoint | What it does |
|:---:|:---|:---|
| <kbd>GET</kbd> | `/` | API Health & Status check |
| <kbd>GET</kbd> | `/api/aliens` | Fetches the complete database of all registered aliens |
| <kbd>GET</kbd> | `/api/aliens/{name}` | Fetches detailed stats of a specific alien (e.g., `heatblast`) |
| <kbd>GET</kbd> | `/assets/images/{file}`| Retrieves the direct image file (e.g., `heatblast.jpg`) |

---

## 💻 Code Example (Python/Requests)

```python
import requests

response = requests.get('[http://your-api-url.com/api/aliens/xlr8](http://your-api-url.com/api/aliens/xlr8)')
data = response.json()

print(f"Alien: {data['name']}")
print(f"Speed Stat: {data['base_stats']['speed']}")
print(f"Top Attack: {data['attacks'][0]['name']}")
