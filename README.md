# DeepSeek Reverse Client (Python)

A powerful, reverse-engineered Python client for DeepSeek AI that bypasses the web interface to provide direct API access. It features advanced capabilities like **Deep Thinking** separation, **Web Search**, and robust session management, all in a beautiful CLI interface.

> **Disclaimer**: This is an unofficial tool for educational and research purposes. Use responsibly and respect DeepSeek's Terms of Service.

## ✨ Key Features

- **🧠 Deep Thinking Integration**: Full support for DeepSeek's "Chain of Thought" reasoning, displayed in a dedicated, collapsible panel separate from the final response.
- **🌐 Web Search Capable**: Toggle web search on/off to give the AI access to real-time information.
- **🔐 Robust Authentication**: 
  - Automated login using `nodriver` (bypassing standard Selenium detections).
  - Supports **Brave Browser** and **Chrome/Chromium**.
  - Intelligent session persistence (auto-saves cookies & tokens).
- **🛡️ Anti-Bot Defense**: Built-in WebAssembly (WASM) runtime to automatically solve DeepSeek's Proof-of-Work (PoW) challenges.
- **💻 Interactive CLI**: A rich, colored terminal interface with slash commands (`/think`, `/search`).

## 🛠️ Prerequisites

- **Python 3.8+**
- **Browser**: **Brave Browser** (Recommended) or Google Chrome/Chromium installed.
  - *Note: The script is currently configured to look for Brave by default but can be adjusted for Chrome.*
- **DeepSeek Account**: You need a valid account at [chat.deepseek.com](https://chat.deepseek.com).

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aryaniiil/deepseek-reverse-api.git
   cd deepseek-reverse-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Credentials:**
   Create a `.env` file in the `data/` directory (or rename `data/.env.example` if it exists):
   ```env
   # data/.env
   DEEPSEEK_EMAIL=your_email@example.com
   DEEPSEEK_PASSWORD=your_password
   ```

## 🎮 Usage

### Interactive Chat Mode
Run the main script to start a chat session:
```bash
python main.py
```

**Commands inside the chat:**
| Command | Description |
|---------|-------------|
| `/think` | Toggle **Deep Thinking** mode (R1/Chain of Thought). |
| `/search`| Toggle **Web Search** functionality. |
| `/exit` | Exit the application. |

### Single Prompt Mode
You can also run a quick, single query directly from the command line:
```bash
python main.py "Explain quantum entanglement in simple terms"
```

## 📂 Project Structure

```
reverse/
├── data/                    # Storage for session data & config
│   ├── .env                 # Your credentials (create this!)
│   ├── auth_token.txt       # Auto-saved auth token
│   ├── deepseek_cookies.json# Auto-saved browser cookies
│   └── sha3_wasm_bg.wasm    # PoW solver module
├── src/                     # Core logic
│   ├── auth.py              # Browser automation & login (Brave/Chrome)
│   ├── client.py            # API client & SSE stream parsing
│   ├── config.py            # Global settings (Headless mode, paths)
│   └── display.py           # Rich UI & Panel rendering
├── main.py                  # Entry point
└── requirements.txt         # Dependencies
```

## 🔧 Troubleshooting

- **Browser Not Found**: 
  - If you don't use Brave, you may need to edit the browser path in `src/auth.py`.
  - Ensure the browser is properly installed in the default location.
- **Login Issues**:
  - Delete `data/deepseek_cookies.json` and `data/auth_token.txt` to force a fresh login.
  - Verify your credentials in `data/.env`.
  - The browser window will open briefly to handle the login (headless mode defaults to `False` for better stability).
- **Missing "Thinking" Panel**:
  - Ensure you have toggled `/think` to ON.
  - Note that only "DeepSeek-R1" or reasoning models produce thinking content.

## 🤝 Contributing

Contributions are welcome! Feel free to submit Pull Requests for:
- New features (File upload, History management).
- Bug fixes.
- Documentation improvements.

## 📄 License

This project is open-source for educational use.
