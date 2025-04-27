# Kidney Disease Detection 🩺 | CT Scan Image Classification

![build](https://img.shields.io/badge/build-passing-brightgreen)
![python](https://img.shields.io/badge/python-3.8%2B-blue)
![license](https://img.shields.io/badge/license-MIT-yellow)

> **State‑of‑the‑art Convolutional Neural Networks (CNNs) that classify kidney CT slices into _Normal_, _Cyst_, _Stone_ or _Tumor_ — packaged for reproducible research and real‑world deployment.**

---

## 📚 Table of Contents
1. [Project Context](#project-context)
2. [Deep‑Learning Pipeline](#deep-learning-pipeline)
3. [Quick Start](#-quick-start)
4. [Project Structure](#-project-structure)
5. [Tech Stack](#-tech-stack)
6. [Workflows](#️-workflows)
7. [Contribution Guide](#-how-to-contribute)
8. [License](#license)

---

## 📊 Project Context

Kidney diseases affect **> 10 % of the global population**. Early detection dramatically reduces the risk of kidney failure, yet manual CT‑scan interpretation is time‑consuming and error‑prone. This repository delivers an **automated classifier** that supports radiologists with rapid, consistent predictions.

| Why it matters | Impact |
|---------------|--------|
| ⏱️  Radiologist shortage | Automation speeds up workflow |
| 🏥  Early intervention | Better patient outcomes |
| 💸  Cost reduction | Fewer invasive procedures |

### Example Kidney CT Image

![Kidney CT Scan](https://www.researchgate.net/profile/Sina-Bagheri-2/publication/351048862/figure/fig2/AS:1019366702325760@1619523801212/Example-of-a-kidney-CT-scan-image.png)

### End‑to‑End Pipeline Overview

![DL Pipeline](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JgE7txbM9BY-xXcdhOTAxA.png)

---

## 🚀 Quick Start

<details>
<summary><strong>Local (Conda)</strong></summary>

```bash
# 1️⃣ Clone
 git clone https://github.com/<your‑user>/Kidney_Disease_Detection.git
 cd Kidney_Disease_Detection

# 2️⃣ Env
 conda create -n kidneycnn python=3.8 -y && conda activate kidneycnn

# 3️⃣ Install
 pip install -r requirements.txt

# 4️⃣ Launch the demo API
 python app.py  # default http://localhost:5000
```

</details>

<details>
<summary><strong>Docker</strong></summary>

```bash
docker build -t kidneycnn .
docker run --rm -p 5000:5000 --gpus all kidneycnn
```

</details>

---

## 🏗️ Project Structure

```text
.
├── app.py                    # FastAPI / Flask demo server
├── configs/                  # YAML configs for every pipeline step
├── src/
│   ├── config/               # configuration manager helpers
│   ├── components/           # data, model, evaluation building blocks
│   └── pipeline/             # orchestrated ML pipelines (DVC)
├── artifacts/                # auto‑generated data & model artefacts
├── dvc.yaml                  # pipeline stages & dependencies
├── params.yaml               # hyper‑parameters
├── requirements.txt          # Python dependencies
└── README.md                 # ← you are here
```

---

## ⚙️ Tech Stack

| Category | Tool |
|----------|------|
| Core DL | PyTorch, TorchVision |
| Training Loop | PyTorch Lightning |
| Orchestration | Hydra, DVC |
| Experiment Tracking | TensorBoard, Weights & Biases (optional) |
| Serving | FastAPI / Flask & Docker |

---

## 🛠️ Workflows

```text
📝 Edit config.yaml / params.yaml →
📦 DVC pipeline rebuilds →
🧪 Unit tests (pytest) & pre‑commit hooks →
📊 Tracked experiments →
🚀 Deploy with Docker
```

---

## ✅ How to Contribute

1. **Fork** the repo
2. `git checkout -b feature/<YourFeature>`
3. Commit following Conventional Commits
4. `git push origin feature/<YourFeature>`
5. Open a **Pull Request** – we’ll review ASAP

---

## 📜 License

This project is released under the **MIT License**.

---

> *“Where there is data smoke, there is business fire.”* — Thomas Redman

