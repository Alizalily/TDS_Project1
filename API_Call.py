import requests

# Your GitHub token
token = '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'  # Replace with your token

# API URL to search users in Mumbai with more than 50 followers
url = 'https://api.github.com/search/users?q=location:Mumbai+followers:>50'

headers = {
    'Authorization': f'token {token}',
}

response = requests.get(url, headers=headers)
users_data = response.json()

# Print user login and name
for user in users_data['items']:
    print(f"Login: {user['login']}, Name: {user.get('name', 'N/A')}")


repositories = []

for user in users_data['items']:
    user_login = user['login']
    repos_url = f'https://api.github.com/users/{user_login}/repos?per_page=100'
    repos_response = requests.get(repos_url, headers=headers)
    
    repos_data = repos_response.json()
    
    for repo in repos_data:
        repositories.append({
            'login': user_login,
            'full_name': repo['full_name'],
            'created_at': repo['created_at'],
            'stargazers_count': repo['stargazers_count'],
            'watchers_count': repo['watchers_count'],
            'language': repo['language'],
            'has_projects': repo['has_projects'],
            'has_wiki': repo['has_wiki'],
            'license_name': repo['license']['name'] if repo['license'] else ''
        })

# Print the repositories data
for repo in repositories:
    print(repo)


import pandas as pd

# Create DataFrames
users_df = pd.DataFrame(users_data['items'])
repos_df = pd.DataFrame(repositories)

# Save to CSV
users_df.to_csv('users.csv', index=False)
repos_df.to_csv('repositories.csv', index=False)

import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())


