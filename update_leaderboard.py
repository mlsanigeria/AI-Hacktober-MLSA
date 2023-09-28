# update_leaderboard.py
# This script updates the GitHub Leaderboard in the README.md file
import requests
from collections import defaultdict
import os

def initialize_api():
    # Define your GitHub repository and authentication token
    repository_owner = "mlsanigeria"
    repository_name = "AI-Hacktober-MLSA"
    api_token = os.environ.get("API_TOKEN")

    # Define the GitHub API endpoint for pull requests
    api_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/pulls"

    # Define query parameters to filter pull requests (only closed ones)
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc",
    }

    # Add your GitHub token to the request headers for authentication
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    # Send a GET request to the GitHub API
    return requests.get(api_url, params=params, headers=headers)

def get_sorted_pr():

    response = initialize_api()
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        pull_requests = response.json()

        # Create a dictionary to track the count of merged pull requests by each user
        merged_prs_count_by_user = defaultdict(int)

        # Iterate through the pull_requests list
        for pr in pull_requests:
            # Check if the pull request was merged and get the username of the user who merged it
            if pr['merged_at']:
                pr_by = pr['user']['login']
                # Increment the count of merged pull requests for this user
                merged_prs_count_by_user[pr_by] += 1
        
        # Print the sorted list of users and their merged pull request counts
        sorted_users = sorted(merged_prs_count_by_user.items(), key=lambda x: x[1], reverse=True)
        for user, count in sorted_users:
            print(f"{user}: {count} merged pull requests")

        # Sort the users by the number of merged pull requests in descending order
        return sorted_users

    else:
        # Handle API request failure
        print(f"API request failed with status code: {response.status_code}")

def leaderboard_data():
    # Calculate the leaderboard data
    sorted_users = get_sorted_pr()
    leaderboard_data = []
    rank = 1
    for user, count in sorted_users:
        leaderboard_data.append({"rank":rank, "contributor": f"{user}", "merged_prs": f"{count}"})
        rank += 1
    return leaderboard_data

leaderboard_data = leaderboard_data()
# Generate the Markdown content for the leaderboard
markdown_content = """
# GitHub Leaderboard

| Rank | Contributor | Merged PRs |
| ---- | ----------- | ---------- |
{}
""".format("\n".join(
    f"| {entry['rank']} | @{entry['contributor']} | {entry['merged_prs']} |"
    for entry in leaderboard_data
))

# Write the Markdown content to README.md
with open("LEADERBOARD.md", "w") as readme_file:
    readme_file.write(markdown_content)
    print("successfully updated README.md")


