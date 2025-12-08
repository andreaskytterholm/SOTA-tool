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
    *   Created `.readthedocs.yaml` for hosting compatibility (configured to use `uv`).
    *   Updated `.gitignore` to exclude `site/` and `.venv/`.
5.  **Fixes**:
    *   Manually fixed `index.md` to replace Sphinx `toctree` directive with a standard Markdown list.
