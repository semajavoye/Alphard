import requests

def get_latest_release():
    api_url = f"https://api.github.com/repos/semajavoye/Alphard/releases/latest"
    response = requests.get(api_url)

    if response.status_code == 200:
        release_info = response.json()
        tag_name = release_info.get('tag_name')
        return tag_name
    else:
        return None

def main():
    latest_version = get_latest_release()

    if latest_version:
        print(f"The latest version of Alphard is {latest_version}")
    else:
        print(f"Unable to fetch the latest version. Check if the repository exists or if you have the correct permissions.")
