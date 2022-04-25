{% include base.html %}

## Tech Talk 3: Accounts and Login

- Flask_Login is Python system, can protect certain routes w/login
- "app = flask(__name__)", "login_manager = LoginManager()", and "login_manager.init_app(app)" is requirement
- app and login_manager are both objects
- Relating login_manager to app
- Need to import UserMixin
- Database example: 
- Werkzeug is built into Flask, used to hash passwords if they are to be displayed in database 
- Model: Signup form creates entry, login is query to check database
- Control: Use driver function instead of calling function directly, display user's account details on profile and deliver error messages
- View: Sign up/Sign in forms and protected pages

Analysis: One of the flaws I see in the current CSP website is the lack of verification. To avoid spamming it would be best to have an email verification system and/or a 2-hour cooldown for making accounts. There should also be different levels of security assigned to certain accounts, so that only teachers have admin privileges (editing other people's table entries). And of course, although the website is meant to educate, allowing logged-in users to view all account details would not be practical in a real-world scenario.
