#!/usr/bin/env python3
import argparse
import os
import sys
import shutil
import datetime
import re
import yaml

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(REPO_ROOT, "_template_post.md")
POSTS_DIR = os.path.join(REPO_ROOT, "_posts")
IMAGES_BASE_DIR = os.path.join(REPO_ROOT, "assets", "images", "posts")
LOGO_PATH = os.path.join(REPO_ROOT, "assets", "images", "logo.png")


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


def extract_frontmatter(content: str):
    """Extract YAML frontmatter from a markdown file."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None


def get_all_categories() -> list:
    """Scan all posts and collect unique categories."""
    categories = set()
    if not os.path.isdir(POSTS_DIR):
        return []
    
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    frontmatter = extract_frontmatter(content)
                    if frontmatter and 'categories' in frontmatter:
                        cats = frontmatter['categories']
                        if isinstance(cats, list):
                            categories.update(cats)
                        elif isinstance(cats, str):
                            categories.add(cats)
            except Exception as e:
                # Skip files that can't be read
                continue
    
    return sorted(list(categories))


def main():
    parser = argparse.ArgumentParser(description='Create a new blog post from template')
    parser.add_argument('-t', '--title', type=str, help='Title of the new post')
    args = parser.parse_args()

    ensure_paths()
    
    if args.title:
        title = args.title.strip()
    else:
        try:
            title = input("Post title: ").strip()
        except KeyboardInterrupt:
            print("\nCancelled.")
            return
    
    if not title:
        print("Title cannot be empty.")
        sys.exit(1)

    slug = slugify(title)
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S %z")
    if not timestamp_str.endswith(" +0000") and not timestamp_str.endswith(" -0000"):
        # If timezone is not set, default to UTC
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S") + " +0000"

    new_post_filename = f"{date_str}-{slug}.md"
    new_post_path = os.path.join(POSTS_DIR, new_post_filename)

    if os.path.exists(new_post_path):
        print(f"Post already exists: {new_post_path}")
        sys.exit(1)

    # Create images directory for this post
    images_dir = os.path.join(IMAGES_BASE_DIR, slug)
    os.makedirs(images_dir, exist_ok=True)

    # Copy logo as default featured image
    featured_image_path = os.path.join(images_dir, "featured.jpg")
    if os.path.isfile(LOGO_PATH):
        shutil.copy2(LOGO_PATH, featured_image_path)

    # Load template and substitute title and date
    tpl = read_template()

    # Get all existing categories
    all_categories = get_all_categories()
    
    # Replace title in frontmatter: assumes a line like 'title: ...'
    tpl = re.sub(r"^title:\s*.*$", f"title: {title}", tpl, flags=re.MULTILINE)

    # Replace date in frontmatter - match either literal YYYY-MM-DD or actual date
    tpl = re.sub(r"^date:.*$", f"date: {timestamp_str}", tpl, flags=re.MULTILINE)

    # Replace categories with all existing unique categories
    if all_categories:
        # Format as inline YAML array: [item1, item2, item3]
        categories_str = "[" + ", ".join(repr(cat) for cat in all_categories) + "]"
        tpl = re.sub(
            r"^categories:\s*\[.*?\]\s*$",
            f"categories: {categories_str}",
            tpl,
            flags=re.MULTILINE,
        )

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
    print(f" - Featured image: {featured_image_path} (copied from logo)")
    if all_categories:
        print(f" - Populated with {len(all_categories)} existing categories")
    print("\nNext: Replace featured.jpg with your actual image if desired.")


if __name__ == "__main__":
    main()
