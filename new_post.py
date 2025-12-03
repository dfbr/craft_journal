#!/usr/bin/env python3
import os
import sys
import shutil
import datetime
import re

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(REPO_ROOT, "_template_post.md")
POSTS_DIR = os.path.join(REPO_ROOT, "_posts")
IMAGES_BASE_DIR = os.path.join(REPO_ROOT, "assets", "images", "posts")


def slugify(title: str) -> str:
    # Lowercase, replace non-word with hyphens, collapse repeats, strip hyphens
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def ensure_paths():
    if not os.path.isfile(TEMPLATE_PATH):
        print(f"Template not found: {TEMPLATE_PATH}")
        sys.exit(1)
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_BASE_DIR, exist_ok=True)


def read_template() -> str:
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def write_post(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    ensure_paths()
    try:
        title = input("Post title: ").strip()
    except KeyboardInterrupt:
        print("\nCancelled.")
        return
    if not title:
        print("Title cannot be empty.")
        sys.exit(1)

    slug = slugify(title)
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")

    new_post_filename = f"{date_str}-{slug}.md"
    new_post_path = os.path.join(POSTS_DIR, new_post_filename)

    if os.path.exists(new_post_path):
        print(f"Post already exists: {new_post_path}")
        sys.exit(1)

    # Create images directory for this post
    images_dir = os.path.join(IMAGES_BASE_DIR, slug)
    os.makedirs(images_dir, exist_ok=True)

    # Load template and substitute title and date
    tpl = read_template()

    # Replace title in frontmatter: assumes a line like 'title: ...'
    tpl = re.sub(r"^(title:\s*).*$", rf"\1{title}", tpl, flags=re.MULTILINE)

    # Replace date in frontmatter: assumes a line like 'date: ...'
    tpl = re.sub(r"^(date:\s*).*$", rf"\1{date_str}", tpl, flags=re.MULTILINE)

    # Optionally set featured_image directory if present and empty
    tpl = re.sub(
        r"^(featured_image:\s*)(.*)$",
        rf"\1/assets/images/posts/{slug}/featured.jpg",
        tpl,
        flags=re.MULTILINE,
    )

    write_post(new_post_path, tpl)

    print("Created:")
    print(f" - Post: {new_post_path}")
    print(f" - Images directory: {images_dir}")
    print("Next: add images (e.g., featured.jpg) to the images directory.")


if __name__ == "__main__":
    main()
