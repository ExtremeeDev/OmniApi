<!-- ═══════════════════ HEADER BANNER (animated) ═══════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF41,50:0A8F2E,100:000000&height=260&section=header&text=OMNI-API&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=%E2%9A%A1%20The%20Most%20Detailed%20%26%20Badass%20Ben%2010%20API%20on%20the%20Internet%20%E2%9A%A1&descSize=18&descAlignY=60&stroke=00FF41&strokeWidth=2" alt="OmniApi Banner"/>
</p>

<!-- ═══════════════════ TYPING ANIMATION (Orbitron font) ═══════════════════ -->
<p align="center">
  <a href="https://github.com/ExtremeeDev/OmniApi">
    <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=24&duration=3000&pause=800&color=00FF41&center=true&vCenter=true&width=700&lines=It's+Hero+Time!+%E2%8F%B3;Game-Ready+Stats+for+Every+Alien+%F0%9F%91%BD;Power+%7C+Speed+%7C+Defense+%7C+Accuracy;Built+for+Gamers+%26+Bot+Developers+%F0%9F%A4%96;Fast+%E2%80%A2+Detailed+%E2%80%A2+Badass+%F0%9F%94%A5" alt="Typing SVG"/>
  </a>
</p>

<!-- ═══════════════════ OMNITRIX GIF ═══════════════════ -->
<!-- 👉 Apna favourite Ben 10 / Omnitrix GIF `assets/omnitrix.gif` naam se save karo -->
<p align="center">
  <img src="assets/omnitrix.gif" alt="Ben 10 Omnitrix Animation" width="280"/>
</p>

<!-- ═══════════════════ BADGES ═══════════════════ -->
<p align="center">
  <img src="https://img.shields.io/github/stars/ExtremeeDev/OmniApi?style=for-the-badge&color=00FF41&logo=github&labelColor=0d1117" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/ExtremeeDev/OmniApi?style=for-the-badge&color=0A8F2E&logo=github&labelColor=0d1117" alt="Forks"/>
  <img src="https://img.shields.io/github/issues/ExtremeeDev/OmniApi?style=for-the-badge&color=ff3b3b&logo=github&labelColor=0d1117" alt="Issues"/>
  <img src="https://img.shields.io/github/license/ExtremeeDev/OmniApi?style=for-the-badge&color=yellow&labelColor=0d1117" alt="License"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-Powered-000000?style=for-the-badge&logo=flask&logoColor=00FF41&labelColor=0d1117" alt="Flask"/>
  <img src="https://img.shields.io/badge/Response-JSON-00FF41?style=for-the-badge&logo=json&logoColor=black&labelColor=0d1117" alt="JSON"/>
  <img src="https://img.shields.io/badge/Aliens-Unlimited-00FF41?style=for-the-badge&labelColor=0d1117" alt="Aliens"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="divider"/>
</p>

---

## 🧬 &nbsp;About OmniApi

> **"Unlike boring basic APIs — OmniApi is built for gamers, bot developers & hardcore Ben 10 fans."**

Har alien ke saath milta hai **balanced game stats**, **detailed attacks** aur **direct image URLs** — sab kuch ek hi blazing-fast JSON response me. Telegram bots, Discord bots, card games, RPGs — jo bhi banao, OmniApi ready hai. 🔥

---

## 🚀 &nbsp;Features — Why OmniApi?

<table align="center">
  <tr>
    <td align="center" width="25%">
      <h3>📊</h3>
      <b>Game-Ready Stats</b><br/>
      <sub><code>Power</code> • <code>Speed</code> • <code>Defense</code> • <code>Accuracy</code><br/>(1–100 scale)</sub>
    </td>
    <td align="center" width="25%">
      <h3>⚔️</h3>
      <b>Detailed Attacks</b><br/>
      <sub><code>Damage</code> • <code>Accuracy</code><br/><code>Melee</code> / <code>Ranged</code> / <code>AoE</code> / <code>Utility</code></sub>
    </td>
    <td align="center" width="25%">
      <h3>🖼️</h3>
      <b>Direct Local Images</b><br/>
      <sub>No broken Imgur links.<br/>HQ images served from our own server.</sub>
    </td>
    <td align="center" width="25%">
      <h3>⚡</h3>
      <b>Blazing Fast</b><br/>
      <sub>Built with Flask<br/>Instant JSON responses.</sub>
    </td>
  </tr>
</table>

---

## 🔗 &nbsp;Endpoints & Usage

**Base URL:** `http://localhost:5000` *(ya apna hosted domain)*

| Method | Endpoint | Description |
|:---:|:---|:---|
| <kbd>GET</kbd> | `/` | 💚 API Health & Status check |
| <kbd>GET</kbd> | `/api/aliens` | 👽 Saare registered aliens ka complete database |
| <kbd>GET</kbd> | `/api/aliens/{name}` | 🎯 Kisi ek alien ki detailed stats (e.g. `heatblast`) |
| <kbd>GET</kbd> | `/assets/images/{file}` | 🖼️ Direct image file (e.g. `heatblast.jpg`) |

---

## 📦 &nbsp;Sample Response

`GET /api/aliens/xlr8`

```json
{
  "name": "XLR8",
  "species": "Kineceleran",
  "base_stats": {
    "power": 55,
    "speed": 100,
    "defense": 40,
    "accuracy": 85
  },
  "attacks": [
    {
      "name": "Tail Whip",
      "damage": 45,
      "accuracy": 90,
      "type": "Melee"
    },
    {
      "name": "Sonic Dash",
      "damage": 60,
      "accuracy": 80,
      "type": "Utility"
    }
  ],
  "image": "/assets/images/xlr8.jpg"
}
```

---

## 💻 &nbsp;Code Example (Python / Requests)

```python
import requests

response = requests.get("http://your-api-url.com/api/aliens/xlr8")
data = response.json()

print(f"Alien: {data['name']}")
print(f"Speed Stat: {data['base_stats']['speed']}")
print(f"Top Attack: {data['attacks'][0]['name']}")
```

**Output:**

```text
Alien: XLR8
Speed Stat: 100
Top Attack: Tail Whip
```

<details>
<summary><b>🤖 Telegram Bot (Pyrogram) Example — click to expand</b></summary>

```python
import requests
from pyrogram import Client, filters

app = Client("ben10bot")

@app.on_message(filters.command("alien"))
async def alien_cmd(_, message):
    name = message.command[1].lower()
    r = requests.get(f"http://your-api-url.com/api/aliens/{name}")
    if r.status_code != 200:
        return await message.reply("❌ Alien nahi mila!")

    a = r.json()
    s = a["base_stats"]
    await message.reply_photo(
        f"http://your-api-url.com{a['image']}",
        caption=(
            f"👽 **{a['name']}**\n\n"
            f"💪 Power: {s['power']}\n"
            f"⚡ Speed: {s['speed']}\n"
            f"🛡️ Defense: {s['defense']}\n"
            f"🎯 Accuracy: {s['accuracy']}"
        ),
    )

app.run()
```

</details>

---

## ⚙️ &nbsp;Installation & Run

```bash
# 1️⃣ Clone the repo
git clone https://github.com/ExtremeeDev/OmniApi.git
cd OmniApi

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Start the API
python app.py
```

🟢 Server live hoga: **`http://localhost:5000`**

---

## 📁 &nbsp;Project Structure

```text
OmniApi/
├── app.py                # Flask server & routes
├── requirements.txt
├── data/
│   └── aliens.json       # Alien database
├── assets/
│   ├── omnitrix.gif      # README animation
│   └── images/           # Alien images (heatblast.jpg, xlr8.jpg ...)
└── README.md
```

---

## 🗺️ &nbsp;Roadmap

- [x] Core alien database with stats
- [x] Detailed attacks system
- [x] Local image serving
- [ ] 🔍 Search & filter by stat / type
- [ ] 🎲 Random alien endpoint
- [ ] ⚔️ Battle simulator endpoint
- [ ] 🔑 API key & rate limiting

---

## 🤝 &nbsp;Contributing

Naya alien add karna hai? Stats balance karne hain? **PRs welcome!** 💚

1. 🍴 Fork the repo
2. 🌿 Create your branch: `git checkout -b feature/new-alien`
3. 💾 Commit: `git commit -m "Added Four Arms"`
4. 🚀 Push & open a Pull Request

---

## 👨‍💻 &nbsp;Developed By

<div align="center">
  <a href="https://t.me/ExtremeeDev" target="_blank">
    <img src="https://img.shields.io/badge/Telegram-@ExtremeeDev-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=101010" alt="Developer Telegram"/>
  </a>
  <a href="https://github.com/ExtremeeDev" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-ExtremeeDev-00FF41?style=for-the-badge&logo=github&logoColor=white&labelColor=101010" alt="GitHub"/>
  </a>
</div>

<br/>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=18&duration=2500&pause=1000&color=00FF41&center=true&vCenter=true&width=500&lines=Star+%E2%AD%90+the+repo+if+you+like+it!;Go+Hero%2C+Go+Alien!+%F0%9F%9F%A2" alt="Footer Typing"/>
</p>

<p align="center">
  <sub>⚠️ Ben 10 is a trademark of Cartoon Network / Warner Bros. OmniApi is an unofficial fan project and is not affiliated with them.</sub>
</p>

<!-- ═══════════════════ FOOTER (animated) ═══════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:0A8F2E,100:00FF41&height=140&section=footer" alt="Footer"/>
</p>
