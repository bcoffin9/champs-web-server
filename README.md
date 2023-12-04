# Web Server Lab

## Completed from Computer Networking: A Top-Down Approach 8th Edition

### How to use

- Run the `server.py` locally
- Open a browser and navigate to your localhost:12000
- You can then test the server using the following format:
  `localhost:12000/champions/<league name>?&year=<year name>`
  - The following leagues are available:
    - Bundesliga
    - MLB, MLS, NBA, NCAAF, NFL, NHL
    - Premier League (English top-flight soccer/football)
    - UEFA Champions League

---

## Passing Criteria

1. Create a connection socket when contacted by a client (browser)
2. Receive the HTTP request from this connection
3. Parse the request to determine the specific file being requested
4. Get the requested file from the server's file system
5. Create an HTTP response message consisting of the requested file preceded by header lines
6. Send the response over the TCP connection to the requesting browser

---

## Handling an unknown request

- If the client requests a file the server doesn't have, the server will return a 404 response to the client.

---

## Future Dev Ideas

- Include a testing package for creating the request and receiving the response
- Include more querying capability on searches
