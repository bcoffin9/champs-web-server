import os
import urllib.parse
from champion_handler import *

def client_thread(connectionSocket, addr):
    try:
        request = connectionSocket.recv(1024).decode()
        print("Received Request from", addr)
        # print(request)

        # Extract the requested resource from the first line of the request
        lines = request.splitlines()
        if len(lines) > 0:
            first_line = lines[0]
            resource = first_line.split()[1]  # The format is typically "GET /path HTTP/1.1"

        # Path handlers
        path_handlers = {
            '/champions/nfl': find_nfl_winner,
            '/champions/nba': find_nba_winner,
            '/champions/mlb': find_mlb_winner,
            '/champions/nhl': find_nhl_winner,
            '/champions/ncaaf': find_ncaaf_winner,
            '/champions/premier-eng': find_premier_eng_winner,
            '/champions/uefa-champions': find_uefa_champs_winner,
            '/champions/bundesliga': find_bundesliga_winner,
            '/champions/mls': find_mls_winner
        }

        # Check if the request matches any champion path
        parsed_url = urllib.parse.urlparse(resource)
        handler_function = path_handlers.get(parsed_url.path)

        if handler_function:
            query = urllib.parse.parse_qs(parsed_url.query)
            year = query.get('year', [None])[0]
            if year:
                winner = handler_function(year)
                httpResponse = f'HTTP/1.1 200 OK\r\n\r\nWinner in {year}: {winner}'
            else:
                httpResponse = 'HTTP/1.1 400 Bad Request\r\n\r\nMissing year parameter'

            connectionSocket.send(httpResponse.encode())
            return
        
        # If the file does not exist, send the 404 HTML file
        httpHeader = b'HTTP/1.1 404 Not Found\r\n\r\n'  # Encode the header as bytes
        with open('resources/not_found.html', 'rb') as file:
            httpResponse = httpHeader + file.read()
        connectionSocket.send(httpResponse)            
            
    except Exception as e:
        print("Error:", e)

    finally:
        connectionSocket.close()
