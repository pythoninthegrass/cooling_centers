# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python web application that aggregates and visualizes public cooling centers across the United States. The project extracts data from PDF documents and web sources, geocodes addresses, and generates interactive maps.

## Development Commands

```bash
# Setup and dependencies
task install             # Install via devbox
task uv:install          # Install with uv package manager
task uv:sync             # Sync with lockfile

# Code quality
task lint                # Run ruff linting
task format              # Run ruff formatting
task test                # Run pytest tests
task pre-commit          # Run pre-commit hooks

# Docker development
task docker:build        # Build Docker image
task docker:up           # Start with docker-compose
task docker:down         # Stop containers
task docker:exec         # Shell into container

# Data processing
./bin/make_map.py        # Generate interactive map from CSV
./bin/geocode.py         # Add coordinates to data
./bin/pdf_to_csv.py      # Extract data from PDFs
```

## Architecture

**Data Flow**: PDF/HTML sources → CSV files → Geocoding → Map generation → Web display

**Key Components**:

- `bin/` - Data processing scripts (PDF extraction, geocoding, map generation)
- `csv/` - Structured cooling center data per state (standardized schema)
- `docs/` - Generated HTML maps for web display
- Folium library generates interactive Leaflet.js maps
- Google Geocoding API for address-to-coordinate conversion

**State Data**: Each state maintains separate CSV files in `csv/` directory with columns for name, address, phone, hours, notes, and coordinates.

## Environment Setup

Requires `.env` file with:

```bash
GOOGLE_API_KEY=your_api_key_here
```

## Python Configuration

- **Version**: Python 3.11+ required
- **Package Manager**: uv (modern, faster alternative to pip)
- **Framework**: Plain (Python web framework)
- **Dependencies**: Plain, Folium, requests, pandas
- **Dev Tools**: ruff (linting/formatting), pytest, mypy
- **Container**: Multi-stage Dockerfile with Python 3.12 slim base

## Future Architecture Plans

The project is evolving toward:

- Database backend (SQLite → Neon migration planned)
- Plain web framework backend
- Iframe embedding for external sites
- Multi-state data aggregation

## Plain Framework Documentation

**Main Documentation**: https://plainframework.com/docs/plain/plain/README.md
**Additional Docs**: https://plainframework.com/docs/
**Starter Apps**:

- Full starter: <https://github.com/dropseed/plain-starter-app>
- Bare starter: <https://github.com/dropseed/plain-starter-bare>
