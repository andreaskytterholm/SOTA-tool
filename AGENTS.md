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

## 2025-12-08: Migration from Sphinx to MkDocs
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

## 2025-12-08: Fix Markdown conversion artifacts
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

## 2025-12-08: Fix additional Markdown bugs
**Agent**: GitHub Copilot CLI
**Task**: Fix escaped apostrophes, broken links in guidelines, and formatting of filtering tags.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_bugs_v2.py` to scan all markdown files in `docs/content/`.
    *   Replaced escaped apostrophes `\'` with `'`.
    *   Reformatted `[Filtering tags: ...]{.silver}` to `**Filtering tags**: ...`.
    *   Fixed broken relative links to `mdr` and `ivdr` in `ansm_2019.md`.

## 2025-12-08: Fix Admonitions and Dropdowns
**Agent**: GitHub Copilot CLI
**Task**: Convert Sphinx-style admonitions and dropdowns to MkDocs Material syntax.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_admonitions.py` to scan all markdown files in `docs/content/`.
    *   Converted `::: admonition` blocks to `!!! info` or `!!! note` blocks.
    *   Converted `::: dropdown` and `::: {#id .dropdown}` blocks to `??? note` (collapsible details) blocks.
    *   Ensured proper indentation for content within these blocks.

## 2025-12-08: Fix Tabs and Tab Sets
**Agent**: GitHub Copilot CLI
**Task**: Convert Sphinx-style tabs and tab-sets to MkDocs Material syntax.

**Changes**:
1.  **Automated Fixes**:
    *   Created and ran `fix_tabs_v2.py` to scan all markdown files in `docs/content/`.
    *   Converted `::: tabs` / `:::: tab` blocks to `=== "Title"` blocks.
    *   Converted `::: tab-set` / `::: tab-item` blocks to `=== "Title"` blocks.
    *   Handled nested colon blocks correctly to preserve content structure.

