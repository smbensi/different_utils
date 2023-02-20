# FreeCodeCamp HTTP Networking
[link](https://www.freecodecamp.org/news/http-networking-protocol-course/)


# HTTP

protocol for communicating online \
Requests and responses: we make requests as a client to a server  \
URL is not specific to HTTP. the prefix specifies the protocol

## clients and servers

clients exist on the front-end of an app (what the user sees) , the server exists at the back-end of an app. the **server** handles the HTTP request

## fetch API
set of built in functions to make HTTP request \
takes 2 inputs : URL and settings \
use **await** before fetch because it can take a while \


## Web addresses

DNS: domain name system : map human readable --> ip adresses \
1. resolve DNS: domain --> IP
2. use IP to make the request across the Internet \

`cloudflare-dns` API  nice tool `jsonlint` [link](https://jsonlint.com/)

the organisation ICANN manages DNS for the entire internet. they manage the "phonebook"

TLD: Top-Level Domain  \
subdomain: for example `api.boot.dev` or `blog.boot.dev`it prefixes a domain name

## URL and URI

URI is a superset of URL. URL are on kind of URI

URL parts: *http://testuser:testpass@testdomain.com:8080/testpath?testsearch=testvalue#testhash*
* protocol: http (required)
* username: testuser
* password: testpass
* hostname: testdomain.com (required)
* port: 8080 (default is used if one is not provided)
* pathname: /testpatth (default / is used if one isn't provided)
* search: ?testsearch=testvalue
* hash: #testhash

## Ports

they are virtual hub  \
 the default port is defined by the protocol (80 for HTTP)

## Synchronous vs Asynchronous

`async` code runs in parallel