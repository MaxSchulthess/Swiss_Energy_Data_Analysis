# Swiss_Energy_Data_Analysis

This is a personal project that serves the purpose of applying, developing, and displaying my data analysis and python skills.

Data contained in this project is taken from the following source(s):  
  - Opendata.Swiss: https://opendata.swiss/en/dataset

The aim is to do an analysis of datasets related to energy (production, consumption, ...) in Switzerland,  
noting any observed trends or remarkable observations made.


### 🚀 Initial Setup (First-Time Only)

#### 1️⃣ Install the Virtual Environment
```bash
python3 -m venv sklearn-env
```

#### 2️⃣ Activate the Virtual Environment

- **Linux/macOS (Bash/Zsh):**
  ```bash
  source sklearn-env/bin/activate
  ```

- **Windows (Command Prompt):**
  ```cmd
  sklearn-env\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .\sklearn-env\Scripts\Activate
  ```

#### 3️⃣ Install Required Packages
```bash
pip install -r requirements.txt
pip install ipykernel
python -m ipykernel install --user --name=sklearn-env --display-name "Python (sklearn-env)"
```

---

### 🔁 Standard Startup (Every Time You Work on the Project)

#### 1️⃣ Activate the Virtual Environment
```bash
source sklearn-env/bin/activate  # Linux/macOS
# OR
sklearn-env\Scripts\activate     # Windows
```

#### 2️⃣ Start Your Work (Jupyter, Scripts, etc.)

#### 3️⃣ Deactivate When Done
```bash
deactivate
```
