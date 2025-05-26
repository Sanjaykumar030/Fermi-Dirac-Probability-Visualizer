# ⚛️ Fermi-Dirac Distribution Visualizer – Interactive GUI

A full-screen interactive Python GUI application that visualizes the **Fermi-Dirac distribution** and **energy band behavior** in semiconductors.  
Built with `matplotlib`, `numpy`, and `matplotlib.widgets`, this educational tool provides real-time visual feedback on how **temperature**, **semiconductor type**, and **energy levels** affect electron occupation probabilities.

## ✨ Features

🎨 Visualizes:
- **Valence Band**, **Conduction Band**, and **Fermi Level**
- **Energy state markers** with color-coded occupation probability
- **Temperature-dependent bandgap shifts**
- **Dynamic physical descriptions** (based on selected temperature, energy level, and semiconductor type)

🧩 Interactive Controls:
- **Temperature Slider**: 0 K to 1000 K
- **Semiconductor Type**: Intrinsic, n-type, p-type (via radio buttons)
- **Energy Level**: Below, equal to, or above Fermi level (via selector)

📊 Educational & User-Friendly Plot:
- Clean UI with labeled energy levels and bands
- Real-time updates on user input
- Designed for use in **Jupyter Notebook** with `%matplotlib widget` for full interactivity

---

## 📚 Technologies & Concepts Used

- **Python 3**
- [`matplotlib`](https://matplotlib.org/) – for plotting and widgets
- [`numpy`](https://numpy.org/) – for computation
- [`matplotlib.widgets`](https://matplotlib.org/stable/users/interactive.html) – for GUI elements

📘 Physics Concepts:
- Fermi-Dirac distribution
- Band theory
- Intrinsic and doped semiconductors (n-type & p-type)

---

## 📷 Screenshot

> Sample GUI Output  
(*Include an image here: You can add `![Screenshot](path/to/image.png)` if you're uploading to GitHub*)

---

## ▶️ How to Run

1. **Install Python 3**  
   Download from: [https://www.python.org](https://www.python.org)

2. **Install Required Libraries**

```bash
pip install matplotlib numpy

