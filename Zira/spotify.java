// Authorization token that must have been created previously. See: https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQBRfSrAWTNOtOkAxEF1tBFFVjc0DgK2vbK-GYq2T2hP5IQ7zR7WLJG_VQCfCGqRQuBkDUO-DlwFKSVKXhiUHgMnHBawbfxo5bVyJ7NS6dS87RECh8ku_cnHnDpk5XhQyJSeoogW7NQvxSBUjkIZ69X2OSST6I5OyXdudxf5SRwF0fS8mDjbI9C8DgbJkNJsSqj3yjhJNE4x5ArdAcd16rMQnRRiK6R2jT1EP2tfP-Jc2AGGsqpAmZvAxcYZ-xi_0ZqqcociKlsHh3EcM84f7mB_GPRybAtb';

async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body: JSON.stringify(body),
  });
  return await res.json();
}

async function getTopArtists() {
  // Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi('v1/me/top/artists?time_range=long_term&limit=5', 'GET')).items;
}

const topArtists = await getTopArtists();
console.log(
  topArtists?.map(({ name }) => `${name}`)
);
