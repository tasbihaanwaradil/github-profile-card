
# GitHub Profile Card Generator

A Python application that uses the **GitHub REST API** to fetch and display live GitHub profile information and repository statistics.

Enter any public GitHub username to generate a profile card showing developer information, followers, public repositories, most-used programming languages, and recently updated repositories.

## Features

- **GitHub Profile Information:** Displays name, username, bio, and location.
- **Profile Statistics:** Shows followers, following, and total public repositories.
- **Language Statistics:** Identifies the top 5 programming languages based on repository counts.
- **Latest Repositories:** Displays up to 5 recently updated repositories with descriptions, languages, stars, and links.
- **JSON Export:** Saves fetched profile and repository data as a JSON file.
- **Error Handling:** Handles invalid usernames, connection errors, HTTP errors, and request timeouts.

## Technologies Used

- Python
- Requests Library
- GitHub REST API
- JSON
- Git and GitHub

## Project Structure

```text
github-profile-card/
│
├── github_api.py       # GitHub API integration
├── profile_card.py     # Profile display and statistics
├── main.py             # Main application
├── requirements.txt    # Project dependencies
├── .gitignore          # Ignored files
├── README.md           # Project documentation
│
└── output/             # Generated JSON profile files
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tasbihaanwaradil/github-profile-card.git
```

### 2. Navigate to the project directory

```bash
cd github-profile-card
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

No GitHub token or API key is required for accessing public GitHub profile information.

## Sample Output

```text
========================================
       GITHUB PROFILE CARD GENERATOR
========================================

Enter GitHub username: tasbihaanwaradil

Fetching GitHub profile for @tasbihaanwaradil...

==================================================
             GITHUB PROFILE CARD
==================================================
Name:              Tasbiha Anwar Adil
Username:          @tasbihaanwaradil
Bio:               Full Stack Software Engineer
Location:          Pakistan
Followers:         4
Following:         16
Public Repos:      44

--------------------------------------------------
MOST USED LANGUAGES
--------------------------------------------------
HTML                 9 repositories
JavaScript           8 repositories
TypeScript           5 repositories
Python               3 repositories
C++                  2 repositories

--------------------------------------------------
LATEST REPOSITORIES
--------------------------------------------------

Repository: github-profile-card
Description: A Python application using GitHub REST API
Language: Python
Stars: 0
URL: https://github.com/tasbihaanwaradil/github-profile-card

Repository: com.aevion.mobile
Description: Final year project mobile Application
Language: TypeScript
Stars: 1
URL: https://github.com/tasbihaanwaradil/com.aevion.mobile

==================================================

Would you like to save this profile? (y/n): y

Profile data saved successfully:
output/tasbihaanwaradil_profile.json

Thank you for using GitHub Profile Card Generator!
```

*Sample output is illustrative and reflects profile data retrieved during development. Live information may change.*

## Generated Output

When you choose `y` to save the profile, the application generates a JSON file:

```text
output/
└── tasbihaanwaradil_profile.json
```

The JSON file contains:
- GitHub profile information
- Repository details
- Top programming language statistics

## API Information

This project uses the following public GitHub REST API endpoints:

| Endpoint | Purpose |
|---|---|
| `/users/{username}` | Fetch user profile |
| `/users/{username}/repos` | Fetch public repositories |

Repository language statistics are calculated using each repository's primary language field. The application retrieves up to 100 recently updated repositories per user.

## Error Handling

The application handles:
- Invalid GitHub usernames
- Network connection failures
- Request timeouts
- HTTP errors
- Empty username input

## Author

**Tasbiha Anwar Adil**

- GitHub: [@tasbihaanwaradil](https://github.com/tasbihaanwaradil)
- LinkedIn: [Tasbiha Anwar Adil](https://linkedin.com/in/tasbiha-anwar-adil/)

---

Developed as a Python project using the GitHub REST API.
