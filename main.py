
from github_api import get_github_profile, get_github_repositories
from profile_card import display_profile_card, save_profile_data


def main():
    print("\n========================================")
    print("       GITHUB PROFILE CARD GENERATOR")
    print("========================================")

    username = input("\nEnter GitHub username: ").strip()

    if not username:
        print("Error: GitHub username cannot be empty.")
        return

    print(f"\nFetching GitHub profile for @{username}...")

    profile = get_github_profile(username)

    if profile is None:
        print("Unable to retrieve GitHub profile.")
        return

    repositories = get_github_repositories(username)

    if repositories is None:
        print("Unable to retrieve repositories.")
        return

    display_profile_card(profile, repositories)

    choice = input("\nWould you like to save this profile? (y/n): ").strip().lower()

    if choice == "y":
        save_profile_data(profile, repositories)
    else:
        print("Profile data was not saved.")

    print("\nThank you for using GitHub Profile Card Generator!")


if __name__ == "__main__":
    main()
