
# Kidney Disease Detection 

A CNN..


## 📊 Project Context

Kidney diseases are a significant global health problem, often leading to serious complications if not detected early. This project leverages **Convolutional Neural Networks (CNN)** to automatically classify kidney-related conditions from **CT scan images**, assisting healthcare professionals in early diagnosis.

### Why Kidney Disease Classification?
- Kidney diseases affect **over 10% of the world's population**.
- Early detection is critical to avoid **kidney failure** and improve patient outcomes.
- Automated classification systems reduce the workload of radiologists and improve diagnosis speed.

### Example of Kidney CT Scan Image:


---

## 🚀 Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
cd Kidney-Disease-Classification-Deep-Learning-Project
```

### 2️⃣ Create and activate a conda environment
```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### 3️⃣ Install project dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app locally
```bash
python app.py
```

📍 **Then open your browser and go to:**  
`http://localhost:5000` or your specified port.

---

## 🛠️ Workflows

Here is the recommended development workflow:

```
🔄 Update config.yaml
🛡️ Update secrets.yaml [Optional]
⚙️ Update params.yaml
🧩 Update the entity
🔧 Update the configuration manager in src/config
🧱 Update components
👵 Update pipeline
💻 Update main.py
📜 Update dvc.yaml
🚀 Launch app.py
```

---

## 📂 Project Structure

```
├── app.py
├── main.py
├── dvc.yaml
├── config.yaml
├── params.yaml
├── secrets.yaml [Optional]
├── src/
│   ├── config/
│   ├── components/
│   └── pipeline/
├── artifacts/
├── requirements.txt
└── README.md
```

---

## 💡 Notes
- **DVC** is used for data & model versioning.
- **src/** folder contains modularized code (configuration, components, pipelines).
- You can modify `params.yaml` and `config.yaml` based on your dataset or training settings.

---

## ✅ How to Contribute?
1. Fork the project 🍵
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add: Your feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request 🔄
