import os
from PIL import Image

def convert_image_to_html(image_file, html_file):
    try:
        img = Image.open(image_file)
        img_width, img_height = img.size
        img_pixels = img.load()

        shadow_pixels = []

        for row in range(img_height):
            for col in range(img_width):
                r, g, b, *alpha = img_pixels[col, row]
                hex_color = f'#{r:02x}{g:02x}{b:02x}'
                shadow_pixels.append(f'{col}px {row}px 0 0 {hex_color}')

        shadow_css = ','.join(shadow_pixels)

        with open(html_file, 'w') as file:
            file.write('<html>\n<head>\n<style>\n')
            file.write('body{margin:0;overflow:hidden;background:#000;}\n')
            file.write('.art{position:absolute;top:50%;left:50%;width:1px;height:1px;')
            file.write(f'box-shadow:{shadow_css};')
            file.write('transform:translate(-50%,-50%) scale(var(--scale));}\n')
            file.write('</style>\n</head>\n<body>\n')
            file.write('<div class="art"></div>\n')
            file.write('<script>\n')
            file.write('function resizeArt(){\n')
            file.write(f'const w={img_width},h={img_height};\n')
            file.write('const sw=window.innerWidth,sh=window.innerHeight;\n')
            file.write('const s=Math.min(sw/w,sh/h);\n')
            file.write('document.documentElement.style.setProperty("--scale",s);\n')
            file.write('}\n')
            file.write('window.addEventListener("resize",resizeArt);\n')
            file.write('resizeArt();\n')
            file.write('</script>\n</body>\n</html>')

        print(f"HTML generated successfully: {html_file}")

    except Exception as error:
        print("Conversion failed:", error)


if __name__ == "__main__":
    image_input = input("Image path: ").strip('"')
    output_html = "output.html"
    convert_image_to_html(image_input, output_html)
