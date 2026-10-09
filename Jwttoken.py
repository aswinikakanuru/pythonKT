#What is Authentication
'''Authentication = verifying who you are.
For example, when you log in to Gmail:

Username/Email: aswini@gmail.com
Password: ********

The server checks:
"Are these credentials correct?"
If yes:
Login successful
If no:
Invalid username or password
'''

'''
Authentication vs Authorization
These two are different:
Concept                   Meaning	                              Example
Authentication	        Who are you?	                   Login with username/password
Authorization	       What can you access?	               Admin can delete users

Simple example:
Authentication:
Are you Aswini?

Authorization:
Is Aswini allowed to delete this user?'''


#Why do APIs need Authentication
'''
Suppose we have an API:
GET /users
Without authentication, anybody might be able to call it.
For example:

Browser
   ↓
GET /users
   ↓
Server
   ↓
All user data

That's dangerous.'''




'''
Common Authentication Methods

Some common methods are:

1. Basic Authentication
2. Session Authentication
3. Token Authentication
4. JWT Authentication
5. OAuth 2.0
6. API Keys
You asked specifically about Basic Authentication / JWT / Token, so we'll focus on those.'''

#Basic Authentication : Basic Authentication is one of the simplest HTTP authentication methods.
#What is a Token : A token is a piece of information that represents an authenticated user.
'''
Why use Tokens?
Imagine you have:
100 API requests
You don't want to repeatedly send:
username
password
username
password
username
password
...

Instead:

Login
 ↓
Get token
 ↓
Use token for API requests

So:
Username + Password
        ↓
      Login
        ↓
      Token
        ↓
API Request 1 → Token
API Request 2 → Token
API Request 3 → Token
API Request 4 → Token
'''

#What is JWT?
'''JWT stands for:JSON Web Token
JWT is a popular format for securely representing information between parties.
A JWT commonly looks like:
xxxxx.yyyyy.zzzzz
It has three parts:
HEADER.PAYLOAD.SIGNATURE
For example:
eyJhbGciOiJIUzI1NiJ9
.
eyJzdWIiOiJhc3dpbmkiLCJleHAiOjE3...
.
abcXYZ123...'''

#JWT Structure
'''Part 1 — Header
The header contains information about the token.
Example:
{
    "alg": "HS256",
    "typ": "JWT"
}
Meaning:
alg → signing algorithm
typ → token type
For example:
HS256
is a common JWT signing algorithm.'''

#Part 2 — Payload

'''The payload contains claims.

Example:

{
    "sub": "aswini",
    "role": "user",
    "exp": 1791187200
}

Possible claims:

sub → subject/user identifier
role → user's role
exp → expiration time
iat → issued-at time

For example:

{
    "sub": "123",
    "username": "aswini",
    "role": "admin"
}


#Important security point
The JWT payload is generally encoded, not encrypted.
Therefore, don't put sensitive information such as:

password
credit card number
OTP

inside a JWT payload.'''

#Part 3 — Signature : The signature helps the server determine whether the token has been modified.
'''
Conceptually:
Signature =
Sign(
    encoded header +
    "." +
    encoded payload,
    secret key
)

Suppose the server's secret key is:MY_SECRET_KEY
The server creates a signature.
If someone modifies the payload:
{
    "role": "admin"
}

the signature won't match.

The server can therefore reject the token.
'''


#Stateless Authentication
'''
What is Stateless Authentication?
JWT authentication is commonly stateless.
That means the server doesn't necessarily need to maintain a login session for every user.
For example:
Request
   ↓
JWT
   ↓
Server verifies JWT
   ↓
User identified

The authentication information needed to validate the request is carried in the token.
Compare that with session authentication:
Client → Session ID
              ↓
           Server
              ↓
       Session Database
'''

#JWT Expiration

'''JWTs commonly have an expiration time.
Example:

{
    "sub": "123",
    "exp": 1791187200
}

After expiration:

JWT
 ↓
Expired
 ↓
401 Unauthorized

The user/application can then obtain a new token through the appropriate authentication flow.'''


#Access Token and Refresh Token
#Access Token : Used for API requests.
#Refresh Token : Used to obtain a new access token.
'''
Login
 ↓
Access Token + Refresh Token
 ↓
Access token expires
 ↓
Refresh token
 ↓
New access token

This reduces the need to make the user log in again frequently.
The exact lifetimes and storage strategy depend on the application.
'''

'''
JWT Security
JWT doesn't automatically make an application secure.
You need to follow good practices.
'''


#FastAPI JWT Example
'''Since you're learning FastAPI, let's see the basic structure.

A simplified flow might look like:

POST /login
       ↓
username + password
       ↓
Verify user
       ↓
Create JWT
       ↓
Return access_token

Then:

GET /users
Authorization: Bearer <JWT>
       ↓
Verify JWT
       ↓
Get current user
       ↓
Return users

A simplified FastAPI example:'''

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.get("/users")
def get_users(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Token received",
        "token": token
    }
