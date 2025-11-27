# Craft Journal

A Jekyll-based blog for documenting crafting projects, hosted on GitHub Pages.

## Creating a New Post

### File Naming
Posts must be named with the format: `YYYY-MM-DD-title-with-hyphens.md`

Example: `2025-11-27-my-craft-project.md`

### Post Template

Create a new file in `_posts/` with this frontmatter:

```yaml
---
layout: post
title: "Your Post Title Here"
date: YYYY-MM-DD HH:MM:SS -0000
categories: [Category 1, Category 2, Category 3]
author: Your Name
featured_image: /assets/images/posts/your-post-name/featured.jpg
project_details:
  Difficulty: Beginner/Intermediate/Advanced
  Time Required: X hours/days
  Equipment:
    - Equipment item 1
    - Equipment item 2
    - Equipment item 3
  Resources:
    - Resource item 1
    - Resource item 2
    - Resource item 3
excerpt: "A brief summary of your post (1-2 sentences). This appears in RSS feeds, post previews, and search results."
---

Your post content goes here...
```

### Frontmatter Fields

**Required:**
- `layout: post` - Must be "post"
- `title:` - The post title
- `date:` - Format: `YYYY-MM-DD HH:MM:SS -ZZZZ` (or omit to use filename date)

**Optional:**
- `categories:` - Array of categories (used for navigation)
- `author:` - Author name
- `featured_image:` - Path to featured image (recommended: 1200-1600px wide)
- `excerpt:` - Brief summary for RSS feeds and previews
- `project_details:` - Custom table of any project information you want to display

### Featured Images

- Recommended size: 1200-1600px wide
- Formats: JPG or PNG
- Location: `/assets/images/posts/post-name/featured.jpg`
- Keep file size under 500KB for performance

