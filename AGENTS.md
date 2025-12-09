# Howto for Agents

This project is a documentation site for the Cyber Compass tool, built with **MkDocs** and the **Material for MkDocs** theme.

## Key Information
*   **Package Manager**: `uv` is used for Python package management. Do not use `pip` directly.
*   **Documentation Source**: All markdown source files are located in the `docs/` directory.
*   **Configuration**: The main configuration file is `mkdocs.yml`.
*   **Legacy Docs**: The old Sphinx/RST documentation is preserved in `docs_legacy/` for reference.

## Common Tasks

### Building the Documentation
To build the static site (output to `site/`):
```bash
uv run mkdocs build
```

### Serving Locally
To preview changes locally with hot-reloading:
```bash
uv run mkdocs serve
```

### Adding Dependencies
To add new python dependencies:
```bash
uv add <package_name>
```

---

# Worklog

## 2025-12-08 13:37: Migration from Sphinx to MkDocs
**Agent**: GitHub Copilot CLI
**Task**: Convert Sphinx documentation project to Markdown/MkDocs.

**Changes**:
1.  **Branching**: Created and switched to `mkdocs-test` branch.
2.  **Dependencies**:
    *   Switched to `uv` for package management.
    *   Replaced `sphinx` dependencies with `mkdocs` and `mkdocs-material` in `pyproject.toml`.
3.  **Conversion**:
    *   Wrote a Python script to convert all `.rst` files to `.md` using `pandoc`.
    *   Preserved directory structure and image assets.
    *   Renamed original `docs/` to `docs_legacy/`.
    *   Moved converted files to new `docs/` directory.
4.  **Configuration**:
    *   Created `mkdocs.yml` with Material theme, navigation tabs, and TOC integration.
    *   Updated `.readthedocs.yaml` for hosting compatibility (configured to use `uv` and `mkdocs`).
    *   Updated `.gitignore` to exclude `site/` and `.venv/`.
5.  **Fixes**:
    *   Manually fixed `index.md` to replace Sphinx `toctree` directive with a standard Markdown list.

## 2025-12-08 13:37: Fix Markdown conversion artifacts
**Agent**: GitHub Copilot CLI
**Task**: Fix broken links and formatting issues resulting from Pandoc conversion.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_markdown.py` to scan all markdown files in `docs/content/`.
    *   Converted Sphinx `::: {.toctree ...}` blocks into standard Markdown lists.
    *   Converted RST-style `` `path`{.interpreted-text role="doc"} `` links to standard Markdown links.
2.  **Manual Fixes**:
    *   Fixed `docs/content/operators/invitro.md` (toctree).
    *   Fixed `docs/content/operators/guidelines/operator_guidelines.md` (broken links).
    *   Fixed `docs/content/manufacturers/regulations/manufacturer_regulations.md` (nested toctree blocks).

## 2025-12-08 13:37: Fix additional Markdown bugs
**Agent**: GitHub Copilot CLI
**Task**: Fix escaped apostrophes, broken links in guidelines, and formatting of filtering tags.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_bugs_v2.py` to scan all markdown files in `docs/content/`.
    *   Replaced escaped apostrophes `\'` with `'`.
    *   Reformatted `[Filtering tags: ...]{.silver}` to `**Filtering tags**: ...`.
    *   Fixed broken relative links to `mdr` and `ivdr` in `ansm_2019.md`.

## 2025-12-08 13:37: Fix Admonitions and Dropdowns
**Agent**: GitHub Copilot CLI
**Task**: Convert Sphinx-style admonitions and dropdowns to MkDocs Material syntax.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_admonitions.py` to scan all markdown files in `docs/content/`.
    *   Converted `::: admonition` blocks to `!!! info` or `!!! note` blocks.
    *   Converted `::: dropdown` and `::: {#id .dropdown}` blocks to `??? note` (collapsible details) blocks.
    *   Ensured proper indentation for content within these blocks.

## 2025-12-08 13:37: Fix Tabs and Tab Sets
**Agent**: GitHub Copilot CLI
**Task**: Convert Sphinx-style tabs and tab-sets to MkDocs Material syntax.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_tabs_v2.py` to scan all markdown files in `docs/content/`.
    *   Converted `::: tabs` / `:::: tab` blocks to `=== "Title"` blocks.
    *   Converted `::: tab-set` / `::: tab-item` blocks to `=== "Title"` blocks.
    *   Handled nested colon blocks correctly to preserve content structure.

## 2025-12-08 13:37: Move Filtering Tags to Front Matter
**Agent**: GitHub Copilot CLI
**Task**: Move "Filtering tags" from content body to YAML front matter for MkDocs Material compatibility.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_tags_v2.py` to scan all markdown files in `docs/content/`.
    *   Extracted tags from lines starting with `Filtering tags:` or `**Filtering tags**:`.
    *   Added `tags` list to the YAML front matter of each file.
    *   Removed the original "Filtering tags" lines from the content.
2.  **Manual Fixes**:
    *   Manually fixed `ansm_2019.md` to include missing tags and remove leftover text.

## 2025-12-08 13:37: Implement Tags Display at Bottom
**Agent**: GitHub Copilot CLI
**Task**: Configure MkDocs to display tags at the bottom of each page as links to a tags index.

**Changes**:
1.  **Configuration**:
    *   Enabled `tags` plugin in `mkdocs.yml`.
    *   Configured `tags_file: tags.md`.
    *   Added `hooks/tags_hook.py` to `hooks` configuration.
2.  **Implementation**:
    *   Created `docs/tags.md` with `[TAGS]` marker.
    *   Created `hooks/tags_hook.py` to append a "Tags" section with links to the bottom of each page content.

## 2025-12-08 13:37: Fix Tag Link Warnings
**Agent**: GitHub Copilot CLI
**Task**: Fix MkDocs build warnings related to tag links and missing anchors.

**Changes**:
1.  **Hook Update**:
    *   Modified `hooks/tags_hook.py` to prepend `tag:` to anchor links (e.g., `#tag:cybersecurity`) to match the format generated by `mkdocs-plugin-tags`.
2.  **Tags Page Update**:
    *   Added hidden anchor elements (e.g., `<div id="tag:cybersecurity"></div>`) to `docs/tags.md` for all used tags.
    *   This resolves MkDocs validation warnings about missing anchors in the source file, while preserving the plugin's dynamic tag generation.

## 2025-12-08 13:37: Fix Broken Image in About Page and Index Page
**Agent**: GitHub Copilot CLI
**Task**: Fix broken image reference in `docs/content/about.md` and `docs/index.md`, and remove embedded HTML.

**Changes**:
1.  **Image Reference in About Page**:
    *   Replaced HTML `<img>` tag with Markdown image syntax `![...](...){...}` in `docs/content/about.md`.
    *   This allows MkDocs to correctly resolve the relative path to `nemecys_logo.png`.
2.  **Image Reference in Index Page**:
    *   Replaced HTML `<figure>` and `<img>` tags with Markdown image syntax `![...](...){...}` in `docs/index.md`.
    *   Removed unnecessary HTML tags to ensure cleaner Markdown.

## 2025-12-08 13:37: Design Updates
**Agent**: GitHub Copilot CLI
**Task**: Replicate design elements from the original site (logo and clean navigation).

**Changes**:
1.  **Logo**:
    *   Added `logo: logo.png` to `mkdocs.yml` to display the Cyber Compass logo in the header.
2.  **Navigation Cleanup**:
    *   Removed `docs/special.md` and `docs/_static/test_page.md` to eliminate empty/test links from the top-level navigation.
    *   This results in a cleaner first page with fewer links, matching the user's request.

## 2025-12-08 13:37: Replicate Original Site Navigation
**Agent**: GitHub Copilot CLI
**Task**: Recreate the cleaner navigation structure of the original ReadTheDocs site.

**Changes**:
1.  **Navigation Generation**:
    *   Created a Python script `generate_nav.py` to parse the original Sphinx `toctree` structure from `docs_legacy/`.
    *   Generated a hierarchical `nav` configuration for `mkdocs.yml` that mirrors the original site's organization.
2.  **Configuration Update**:
    *   Appended the generated `nav` section to `mkdocs.yml`.
    *   This explicitly defines the top-level tabs (Home, About, Manufacturers, Operators) and their sub-sections, eliminating clutter from unlisted files (like `tags.md` and `general/`) in the navigation menu.

## 2025-12-08 13:37: Make Logo Prominent
**Agent**: GitHub Copilot CLI
**Task**: Increase the size of the logo in the header to match the prominence of the original site.

**Changes**:
1.  **CSS Customization**:
    *   Created `docs/stylesheets/extra.css`.
    *   Added CSS to increase the height of the logo (`.md-header__button.md-logo img`) to `64px`.
    *   Increased the header height (`--md-header-height`) to `80px` to accommodate the larger logo.
2.  **Configuration**:
    *   Added `extra_css` to `mkdocs.yml` to include the custom stylesheet.

## 2025-12-09 10:00: Add Tags Page to Navigation
**Agent**: GitHub Copilot CLI
**Task**: Add a dedicated Tags page to the top-level navigation.

**Changes**:
1.  **Navigation**:
    *   Added `Tags: tags.md` to the `nav` section in `mkdocs.yml`.
    *   Placed it after "About" to make it easily accessible.


