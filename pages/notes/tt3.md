{% include base.html %}

## Tech Talk 3: Accounts and Login

- Flask_Login is Python system, can protect certain routes w/login
- "app = flask(__name__)", "login_manager = LoginManager()", and " is requirement
- app and login_manager are both objects
- Relating login_manager to app
- Need to import UserMixin
- Database example: 
- Werkzeug is built into Flask, used to hash passwords if they are to be displayed in database 
- Model: Signup form creates entry, login is query to check database
- Control: Use driver function instead of calling function directly, display user's account details on profile and deliver error messages
- View: Sign up/Sign in forms and protected pages
