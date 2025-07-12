---
applyTo: '**'
---
# Contributing Guide & Commit Convention

We use a structured commit message format to ensure our Git history is clean, readable, and easy to navigate. This is based on Conventional Commits, with added emojis for visual clarity.

### Commit Message Format
Each commit message consists of a **header**, a **body**, and a **footer**.

```
<emoji> <type>(<scope>): <subject>
│       │      │         │
│       │      │         └─> Short summary in present tense. Not capitalized. No period.
│       │      │
│       │      └─> Optional scope of the change (e.g., backend, frontend, db, docs, repo).
│       │
│       └─> Type of change (see list below).
│
└─> Emoji representing the type of change.

[optional body: more detailed explanation, formatted in markdown]


[optional footer: e.g., "Fixes #123", "BREAKING CHANGE: ..."]
```

## Commit Types

Use the following types for your commits.

| Emoji | Type       | Description & Example                                                                              |
| :---- | :--------- | :------------------------------------------------------------------------------------------------- |
| ✨    |  `feat`     | A new feature or enhancement. <br/>_E.g., `feat(backend): add user authentication endpoint`_          |
| 🐛    | `fix`      | A bug fix. <br/>_E.g., `fix(frontend): correct case conversion for user input`_                     |
| 📚    | `docs`     | Documentation-only changes. <br/>_E.g., `docs(repo): update README with setup instructions`_         |
| 📦    | `refactor` | A code change that neither fixes a bug nor adds a feature. <br/>_E.g., `refactor(backend): simplify database query logic`_ |
| 🚀    | `perf`     | A code change that improves performance. <br/>_E.g., `perf(frontend): optimize image loading`_       |
| ⛑     | `test`     | Adding missing tests or correcting existing tests. <br/>_E.g., `test(backend): add tests for new user model`_ |
| 🎨    | `style`    | Changes that do not affect the meaning of the code (white-space, formatting, etc). <br/>_E.g., `style: format all python files with black`_ |
| 🛠     | `build`    | Changes that affect the build system or external dependencies. <br/>_E.g., `build(frontend): upgrade react to v18`_ |
| 💢    | `ci`       | Changes to our CI configuration files and scripts. <br/>_E.g., `ci: add linting step to docker build workflow`_ |
| ♻️    | `chore`    | Other changes that don't modify `src` or `test` files. <br/>_E.g., `chore: add .dockerignore file`_ |
| ⏪️    | `revert`   | Reverts a previous commit. <br/>_E.g., `revert: feat(backend): add user authentication endpoint`_   |
| 🔥    | `delete`   | Deleting files or directories. <br/>_E.g., `delete: remove unused assets from frontend`_           |

The commit message should always be enclosed in a code block for clarity.
