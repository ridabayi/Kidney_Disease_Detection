
# Kidney Disease Detection 

A CNN..


## 📊 Project Context

Kidney diseases are a significant global health problem, often leading to serious complications if not detected early. This project leverages **Convolutional Neural Networks (CNN)** to automatically classify kidney-related conditions from **CT scan images**, assisting healthcare professionals in early diagnosis.

### Why Kidney Disease Classification?
- Kidney diseases affect **over 10% of the world's population**.
- Early detection is critical to avoid **kidney failure** and improve patient outcomes.
- Automated classification systems reduce the workload of radiologists and improve diagnosis speed.

### Example of Kidney CT Scan Image:

![Kidney CT Scan](https://www.researchgate.net/profile/Sina-Bagheri-2/publication/351048862/figure/fig2/AS:1019366702325760@1619523801212/Example-of-a-kidney-CT-scan-image.png)
*Example of a kidney CT scan image used for classification.*

### Deep Learning Pipeline Overview:

![Deep Learning Pipeline](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JgE7txbM9BY-xXcdhOTAxA.png)
*General workflow of a CNN-based classification system.*

---

## 🚀 Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ridabayi/AI-Powered-Pipeline-for-Kidney-Disease-Diagnosis-MLflow-DVC
```

### 2️⃣ Create and activate a conda environment
```bash
conda create -n env python=3.8 -y
conda activate env
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
.
├── .dvc/                     # DVC metadata
├── .github/                  # Actions & workflows
├── artifacts/                # Saved data and models
├── config/                   # YAML configurations
├── logs/                     # Training/inference logs
├── model/                    # Trained models
├── research/                 # Experimental notebooks
├── src/
│   └── CnnClassifier/
│       ├── components/       # Core components
│       ├── config/           # Configuration helpers
│       ├── constants/        # Global constants
│       ├── entity/           # Data schemas
│       ├── pipeline/         # Pipeline orchestration
│       └── utils/            # Utility functions
├── templates/                # Frontend templates
├── app.py                    # API server
├── main.py                   # CLI interface
├── dvc.yaml                  # DVC pipelines
├── params.yaml               # Hyperparameters
├── requirements.txt          # Dependencies
├── dockerfile                # Docker container
├── setup.py                  # Installable package setup
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
