# static_site_demo

## Project Overview

This is a static site repository used to publish HTML and static resources (CSS, JS, images, etc.) to the internet via GitHub.

- **Remote**: git@github.com:offline2online/static_site_demo.git
- **Branch**: `main` (default publishing branch)
- **Purpose**: Upload static files and push to GitHub for hosting

## Repository Structure

- `index.html` — Main entry point
- Static assets (CSS, JS, images) go directly in the repo root or organized subdirectories

## Common Workflows

### Publish changes
Use the `/publish` skill to stage all changes, commit with a message, and push to `main`:
```
/publish
```

### Manual git flow
```bash
git add .
git commit -m "your message"
git push origin main
```

## Guidelines

- Always push to `main` branch
- Commit messages should be short and descriptive (e.g., "Add contact page", "Update hero image")
- No build step required — files are served as-is
- Keep assets organized (e.g., `css/`, `js/`, `images/` subdirectories)
