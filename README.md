# 🖼️ ImageToHtml (Python · Box-Shadow Method)

**ImageToHtml** is a Python-based project that converts an image into a **single HTML `<div>` rendered entirely with pure CSS using `box-shadow`**.
Each pixel of the image is recreated as a CSS shadow, producing pixel-perfect visual output without using canvas, SVG, or external CSS frameworks.

This approach demonstrates a creative and unconventional way of rendering images using **only HTML & CSS**, generated automatically via Python.

---

## ✨ Key Features

* Built with **Python**
* Generates **HTML + Pure CSS**
* Uses **single `<div>` with `box-shadow`**
* No JavaScript libraries or CSS frameworks
* Automatic scaling to fit screen size
* Clean, minimal HTML output
* Works directly in the browser

---

## 🧠 How It Works

1. Python reads the image using **Pillow**
2. Each pixel’s color is converted into a CSS `box-shadow`
3. All pixels are applied to a **1×1 div**
4. JavaScript dynamically scales the artwork to fit the viewport

This method is especially useful for:

* Pixel art experiments
* CSS rendering demos
* Creative frontend challenges

---

## 🛠️ Technologies Used

* **Python 3**
* **Pillow (PIL)**
* **HTML5**
* **CSS3**
* **Vanilla JavaScript** (for responsive scaling)

---

## 📂 Project Structure

```bash
ImageToHtml/
│
├── main.py              # Python image-to-HTML converter
├── output.html          # Generated HTML file
├── requirements.txt     # Pillow dependency
└── README.md
```

---

## ▶️ Installation

Install the required dependency:

```bash
pip install pillow
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Enter the image path when prompted:

```text
Image path: example.png
```

The generated file will be saved as:

```text
output.html
```

Open it in any modern browser to view the result.

---

## ⚠️ Performance Notes

* This method generates **one CSS shadow per pixel**
* Large images may cause:

  * High memory usage
  * Browser lag
* Best suited for:

  * Small images
  * Pixel art
  * Experiments & demos

---

## 🚀 Future Improvements

* Transparency (alpha channel) support
* CLI arguments instead of input prompt
* Image resizing before conversion
* Color grouping optimization
* Optional background control
* Export minified HTML

---

## 📜 License

This project is open-source and available under the **MIT License**.
