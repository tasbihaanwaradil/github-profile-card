
import requests

BASE_URL = "https://api.github.com"


def get_github_profile(username):
    """
    Fetch public GitHub profile information.
    """

    url = f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print("Error: GitHub username not found.")
            return None

        response.raise_for_status()

        profile = response.json()

        return profile

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to GitHub.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")

    return None


def get_github_repositories(username):
    """
    Fetch public repositories of a GitHub user.
    """

    url = f"{BASE_URL}/users/{username}/repos"

    params = {
        "per_page": 100,
        "sort": "updated",
        "direction": "desc"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        repositories = response.json()

        return repositories

    except requests.exceptions.Timeout:
        print("Error: Repository request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to GitHub.")

    except requests.exceptions.HTTPError as error:
        print(f"Repository HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Repository API Error: {error}")

    return None
