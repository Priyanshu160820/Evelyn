import requests

# Define the token as a constant
TOKEN = "BQBRfSrAWTNOtOkAxEF1tBFFVjc0DgK2vbK-GYq2T2hP5IQ7zR7WLJG_VQCfCGqRQuBkDUO-DlwFKSVKXhiUHgMnHBawbfxo5bVyJ7NS6dS87RECh8ku_cnHnDpk5XhQyJSeoogW7NQvxSBUjkIZ69X2OSST6I5OyXdudxf5SRwF0fS8mDjbI9C8DgbJkNJsSqj3yjhJNE4x5ArdAcd16rMQnRRiK6R2jT1EP2tfP-Jc2AGGsqpAmZvAxcYZ-xi_0ZqqcociKlsHh3EcM84f7mB_GPRybAtb"

# Function to fetch top artists from Spotify
def get_top_artists():
    # Spotify API endpoint for top artists
    url = "https://api.spotify.com/v1/me/top/artists?time_range=long_term&limit=20"

    # Request headers with the authorization token
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        top_artists = response.json()['items']
        # Print out the top artists' names
        print("Top 5 Artists:")
        for artist in top_artists:
            print(artist['name'])
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.text)

# Main function to run the script
def main():
    print("Spotify Authorization Token:")
    print(TOKEN)
    print("\nFetching top artists...\n")
    get_top_artists()

# Call the main function to run the program
if __name__ == "__main__":
    main()
