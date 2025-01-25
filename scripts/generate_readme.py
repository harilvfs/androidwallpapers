import os

WALLPAPER_DIR = "."
README_FILE = "README.md"

def generate_markdown(images):
    """Generates Markdown for images displayed side by side."""
    rows = []
    row = []
    for i, img in enumerate(images, start=1):
        row.append(f"<img src='{img}' alt='img' width='150px' style='margin: 5px;'>")
        if i % 5 == 0:  # Add a new row after 5 images
            rows.append("".join(row))  # Join images in the row without line breaks
            row = []
    if row:  # Add any remaining images
        rows.append("".join(row))
    return "<div style='display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;'>\n" + "\n<div style='display: flex; gap: 10px; justify-content: center;'>\n".join(rows) + "\n</div>"

def main():
    # Collect all images in the root directory
    images = [
        file for file in sorted(os.listdir(WALLPAPER_DIR))
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    if not images:
        print("No wallpapers found.")
        return

    # Generate Markdown content
    markdown = generate_markdown(images)
    readme_content = (
        "# Wallpaper Previews\n\n"
        "Here is a preview of all wallpapers in this repository:\n\n"
        + markdown
    )

    # Write to README.md
    with open(README_FILE, "w") as readme:
        readme.write(readme_content)

if __name__ == "__main__":
    main()

