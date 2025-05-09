# Personalized-LLM

---

## MacOS Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install backend dependencies
pip install -r requirements.txt

# 3. Navigate to llm folder and start llm 
cd llm_api
python llm_server.py

# 4. Open a new terminal for the backend
cd client/src/backend
python app.py

# 5. Open a new terminal for the frontend
cd client
npm install
npm start
```
---
## Windows Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install backend dependencies
pip install -r requirements.txt

# 3. Navigate to llm folder and start llm 
cd llm_api
python llm_server.py

# 4. Open a new terminal for the backend
cd client/src/backend
python app.py

# 5. Open a new terminal for the frontend
cd client
npm install
npm start
```
