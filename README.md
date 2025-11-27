# Craft Journal

A Jekyll-based blog for documenting crafting projects, hosted on GitHub Pages.

## Features

✨ **Key Features:**
- Clean, responsive design
- Category-based organization with dynamic category generation
- Searchable categories page
- Custom favicon support
- Configurable number of posts on homepage (default: 5)
- SEO-friendly with jekyll-seo-tag
- Archive page with yearly organization
- Mobile-responsive layout

## Setup Instructions

### 1. Local Development

**Prerequisites:**
- Ruby (version 2.7 or higher)
- RubyGems
- GCC and Make

**Installation:**

```bash
# Install dependencies
bundle install

# Run the site locally
bundle exec jekyll serve

# View at http://localhost:4000
```

### 2. GitHub Pages Deployment

1. **Create a GitHub repository** named `craft_journal` (or your preferred name)

2. **Update `_config.yml`** with your information:
   ```yaml
   title: Your Journal Name
   description: Your journal description
   url: "https://yourusername.github.io"
   baseurl: "/craft_journal"
   ```

3. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/craft_journal.git
   git push -u origin main
   ```

4. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: / (root)
   - Save

5. **Your site will be live at:** `https://yourusername.github.io/craft_journal/`

## Customization

### Change Number of Posts on Homepage

Edit `_config.yml`:
```yaml
posts_per_page: 5  # Change to your desired number
```

### Add Custom Favicon

1. Generate favicons using [Favicon.io](https://favicon.io/) or [RealFaviconGenerator](https://realfavicongenerator.net/)
2. Replace files in `assets/images/`:
   - `favicon.ico`
   - `favicon-16x16.png`
   - `favicon-32x32.png`
   - `apple-touch-icon.png`

### Create New Posts

Create a new file in `_posts/` with the format: `YYYY-MM-DD-title.md`

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS -0000
categories: [Category 1, Category 2, Category 3]
tags: [tag1, tag2, tag3]
author: Your Name
---

Your content here...
```

### Customize Colors

Edit `assets/css/style.css` and modify the color variables:
- Primary color: `#007bff`
- Background: `#f8f9fa`
- Text: `#333`

## Project Structure

```
craft_journal/
├── _config.yml           # Site configuration
├── _layouts/             # Layout templates
│   ├── default.html     # Main layout with header/footer
│   └── post.html        # Post layout
├── _posts/              # Blog posts (markdown)
├── assets/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── images/          # Images and favicons
├── index.html           # Homepage (latest posts)
├── categories.html      # Categories page with search
├── archive.html         # All posts by year
├── about.html          # About page
├── Gemfile             # Ruby dependencies
└── .gitignore          # Git ignore rules
```

## Writing Posts

Each post should have YAML frontmatter with:
- `layout: post` (required)
- `title:` (required)
- `date:` (required)
- `categories:` (array, supports multiple)
- `tags:` (optional array)
- `author:` (optional)

**Example:**
```markdown
---
layout: post
title: "My Awesome Craft Project"
date: 2025-11-27 14:00:00 -0000
categories: [Knitting, Beginner Projects, Winter Crafts]
tags: [yarn, needles, cozy]
author: Jane Doe
---

Content goes here...
```

## Categories

Categories are automatically generated from post frontmatter. The categories page includes:
- Quick jump navigation
- Post count per category
- Real-time search functionality
- Posts grouped by category

## Support

For Jekyll documentation: [https://jekyllrb.com/docs/](https://jekyllrb.com/docs/)
For GitHub Pages: [https://docs.github.com/en/pages](https://docs.github.com/en/pages)

## License

Feel free to use this template for your own projects!

---

Happy crafting! 🎨✨
