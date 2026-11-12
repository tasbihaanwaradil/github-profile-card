
import json
import os
from collections import Counter


def get_language_statistics(repositories):
    """
    Count repositories by their primary programming language.
    """

    languages = Counter()

    for repo in repositories:
        language = repo.get("language")

        if language:
            languages[language] += 1

    return languages.most_common(5)


def display_profile_card(profile, repositories):
    """
    Display GitHub profile information and repository statistics.
    """

    print("\n" + "=" * 50)
    print("             GITHUB PROFILE CARD")
    print("=" * 50)

    print(f"Name:              {profile.get('name') or 'Not provided'}")
    print(f"Username:          @{profile.get('login')}")
    print(f"Bio:               {profile.get('bio') or 'Not provided'}")
    print(f"Location:          {profile.get('location') or 'Not provided'}")
    print(f"Followers:         {profile.get('followers', 0)}")
    print(f"Following:         {profile.get('following', 0)}")
    print(f"Public Repos:      {profile.get('public_repos', 0)}")

    print("\n" + "-" * 50)
    print("MOST USED LANGUAGES")
    print("-" * 50)

    languages = get_language_statistics(repositories)

    if languages:
        for language, count in languages:
            print(f"{language:<20} {count} repositories")
    else:
        print("No language information available.")

    print("\n" + "-" * 50)
    print("LATEST REPOSITORIES")
    print("-" * 50)

    for repo in repositories[:5]:
        print(f"\nRepository: {repo.get('name')}")
        print(f"Description: {repo.get('description') or 'No description'}")
        print(f"Language: {repo.get('language') or 'Not specified'}")
        print(f"Stars: {repo.get('stargazers_count', 0)}")
        print(f"URL: {repo.get('html_url')}")

    print("\n" + "=" * 50)


def save_profile_data(profile, repositories):
    """
    Save GitHub profile and repository information as JSON.
    """

    os.makedirs("output", exist_ok=True)

    filename = f"output/{profile['login']}_profile.json"

    data = {
        "profile": profile,
        "repositories": repositories,
        "top_languages": get_language_statistics(repositories)
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\nProfile data saved successfully: {filename}")
