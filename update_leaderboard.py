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
        'per_page': 100,  # Number of PRs per page (max is typically 100)
        'page': 1,  # Start with page 1
    }

    # Add your GitHub token to the request headers for authentication
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    all_prs = []
    while True:
        response = requests.get(api_url, params=params, headers=headers)
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            pull_requests = response.json()
            if len(pull_requests) == 0:
            # No more PRs to fetch, break out of the loop
                break
            else:
                # Extend the list of all PRs with the current page's PRs
                all_prs.extend(pull_requests)
                # Move to the next page
                params['page'] += 1
    # Send a GET request to the GitHub API
    return all_prs


def get_sorted_pr():

    response = initialize_api()
    
    # Create a dictionary to track the count of merged pull requests by each user
    merged_prs_count_by_user = defaultdict(int)
    avi = {}
    # Create a list of contributors to exempt
    exempt = ["Odion-Sonny", "Tutu6790", "Sammybams", "FelixFrankFelix", "Olamilekan002", "AjibolaMatthew1", "salimcodes"]

    # Iterate through the pull_requests list
    for pr in response:
        # Check if the pull request was merged and get the username of the user who merged it
        if pr['merged_at']:
            pr_by = pr['user']['login']
            
            # Check if the user is exempted
            if pr_by in exempt:
                continue
            else:
                # Increment the count of merged pull requests for this user
                merged_prs_count_by_user[pr_by] += 1
                avi[pr_by] = pr['user']['avatar_url']
    # Print the sorted list of users and their merged pull request counts
    sorted_users = sorted(merged_prs_count_by_user.items(), key=lambda x: x[1], reverse=True)

    # Sort the users by the number of merged pull requests in descending order
    return sorted_users, avi

def leaderboard_data():
    # Calculate the leaderboard data
    sorted_users, avi = get_sorted_pr()
    leaderboard_data = []
    rank = 1
    last_count = 0
    for user, count in sorted_users:
        if count == last_count:
            rank -= 1
            leaderboard_data.append({"rank":rank, "avi": f"<img src='{avi[user]}' alt='Avatar' width='30' height='30'>", "contributor": f"[{user}](https://github.com/{user})", "merged_prs": f"{count}"})
        else:
            last_count = count
            leaderboard_data.append({"rank":rank, "avi": f"<img src='{avi[user]}' alt='Avatar' width='30' height='30'>", "contributor": f"[{user}](https://github.com/{user})", "merged_prs": f"{count}"})
        rank += 1
    return leaderboard_data

leaderboard_data = leaderboard_data()

# filter only the top 10 contributors
max_rank = 10
filtered_data = [contributor for contributor in leaderboard_data if contributor['rank'] <= max_rank]

# Generate the Markdown content for the leaderboard
markdown_content = """
# GitHub Leaderboard

Welcome to the Official Leaderboard, showcasing our top contributors and their impressive contributions.

| Rank || Contributor | Merged PRs |
| ---- | -- |----------- | ---------- |
{}

Thank you to all our fantastic contributors for their hard work and dedication!

""".format("\n".join(
    f"| {entry['rank']} | {entry['avi']} | {entry['contributor']} | {entry['merged_prs']} |"
    for entry in filtered_data
))

# Write the Markdown content to LEADERBOARD.md
with open("LEADERBOARD.md", "w") as readme_file:
    readme_file.write(markdown_content)
    print("successfully updated LEADERBOARD.md")


