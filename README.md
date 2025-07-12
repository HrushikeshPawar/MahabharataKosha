# Mahabharata Kosha (महाभारत कोश)

[![Project Status: WIP](https://img.shields.io/badge/status-work_in_progress-yellow.svg)](https://github.com/your-username/mahabharata-kosha)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

An interactive, web-based learning environment for the Mahabharata in its original Sanskrit.

## The Vision

Reading a monumental epic like the Mahabharata in its original Sanskrit is a deeply enriching experience, yet it remains inaccessible to most learners who are not yet proficient in the language. Existing digital resources are often fragmented—providing either the raw text, a translation, or linguistic tools, but rarely all three in a single, cohesive, and user-friendly platform.

**Mahabharata Kosha** (The Mahabharata Treasury) aims to bridge this gap. This project is dedicated to building an open-source platform that weaves together the authoritative Sanskrit text, a trusted English translation, and powerful, interactive linguistic tools. Our goal is to transform passive reading into an active learning journey, allowing users to dissect every verse, understand its grammatical structure, and explore the profound depths of the epic word by word.

## ✨ Core Features (Planned)

*   **Verse-by-Verse Parallel Text:** Read the BORI Critical Edition Sanskrit text alongside the Kisari Mohan Ganguli English translation in a clean, synchronized view.
*   **Interactive Word Dissection:** Click on any Sanskrit word to instantly see its root (`dhatu`), grammatical form (case, number, gender, tense, etc.), and meaning.
*   **Transliteration Support:** Toggle between Devanagari and IAST transliteration on the fly.
*   **Advanced Search:** Search the entire epic in either Sanskrit or English, with future plans to search by grammatical roots or concepts.
*   **Personalization:** User accounts to support bookmarking, personal notes on verses, and a custom vocabulary builder.

## 🛠 Tech Stack

This project is a monorepo built with a modern, performant, and type-safe technology stack.

| Area      | Technology                                                                                                   |
| :-------- | :----------------------------------------------------------------------------------------------------------- |
| **Backend**   | [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Alembic](https://alembic.sqlalchemy.org/), [uv](https://github.com/astral-sh/uv) |
| **Frontend**  | [TypeScript](https://www.typescriptlang.org/), [React](https://reactjs.org/), [Vite](https://vitejs.dev/), [pnpm](https://pnpm.io/)                                       |
| **Database**  | [PostgreSQL](https://www.postgresql.org/)                                                                    |
| **DevOps**    | [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) for local development |

## 🚀 Getting Started

A complete local development environment is orchestrated with Docker Compose. With one command, you can launch the PostgreSQL database, the FastAPI backend, and the Vite frontend dev server.

### Prerequisites

1.  **Git:** [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2.  **Docker & Docker Compose:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
3.  **Node.js (v20+) & pnpm:** We recommend using a version manager like [nvm](https://github.com/nvm-sh/nvm).
4.  **uv (Python):** Follow the [official installation instructions](https://github.com/astral-sh/uv#installation).

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/mahabharata-kosha.git
    cd mahabharata-kosha
    ```

2.  **Create the environment file:**
    Create a `.env` file in the root of the project by copying the example. This file holds your database credentials and other secrets.
    ```bash
    cp .env.example .env
    ```
    *(You can modify the default password in `.env` if you wish)*

3.  **Launch the services:**
    This command will build the Docker images and start all the services.
    ```bash
    docker-compose up --build
    ```

4.  **You're ready to code!**
    *   The FastAPI backend is available at `http://localhost:8000`.
    *   The React frontend is available at `http://localhost:5173`.
    *   Any changes you make to the `backend/` or `frontend/` directories will trigger live-reloading.

## 📁 Project Structure

This project is a monorepo containing both the backend and frontend applications.

```
.
├── backend/          # FastAPI application (Python)
├── data/             # Raw and processed data sources
├── frontend/         # React application (TypeScript)
├── notebooks/        # Jupyter notebooks for exploration
├── .github/          # GitHub templates for issues and PRs
├── docker-compose.yml # Orchestrator for all services
└── README.md
```

## 🗺️ Development Roadmap

This project will be developed in phases. The primary goal is to reach a feature-rich MVP as efficiently as possible.

*   **Phase 1: MVP Foundation (In Progress)**
    *   [x] Set up project scaffolding and Docker environment.
    *   [ ] Define database schema and set up migrations.
    *   [ ] Ingest and align raw Sanskrit and English texts.
    *   [ ] Build core API for serving verse data.
    *   [ ] Build basic frontend reader UI.
    *   [ ] Integrate NLP tools and pre-compute linguistic analysis.
    *   [ ] Implement interactive word-dissection popover.

*   **Phase 2: Beta Features**
    *   [ ] User authentication.
    *   [ ] Bookmarking and annotation features.
    *   [ ] Basic search functionality.

*   **Phase 3: V1.0 and Beyond**
    *   [ ] Advanced search capabilities.
    *   [ ] Audio recitation integration.
    *   [ ] Exploring additional commentaries and translations.

## 🙏 Contributing

This is a personal learning project, but contributions and suggestions are welcome. Please read our `CONTRIBUTING.md` to learn about our development process, commit conventions, and more.

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0**. The full license text will be available in the `LICENSE` file. This choice was made to ensure that the project and all of its derivatives—*especially those run as network services*—will always remain free and open-source for the benefit of the entire community.
