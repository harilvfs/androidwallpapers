import os

WALLPAPER_DIR = "."
README_FILE = "README.md"

def generate_markdown(images):
    """Generates Markdown for images displayed side by side."""
    rows = []
    for i, img in enumerate(images, start=1):
        rows.append(f"<img src='{img}' alt='img' width='150px' style='margin: 5px;'>")
        if i % 3 == 0:  
            rows.append("<br>")  
    return "\n".join(rows)

def main():
    images = [
        file for file in sorted(os.listdir(WALLPAPER_DIR))
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    if not images:
        print("No wallpapers found.")
        return

    markdown = generate_markdown(images)
    readme_content = (
        "# Wallpaper Previews\n\n"
        "Here is a preview of all wallpapers in this repository:\n\n"
        + markdown
    )

    with open(README_FILE, "w") as readme:
        readme.write(readme_content)

if __name__ == "__main__":
    main()
