from flask_talisman import Talisman

# Create the Flask app
app = Flask(__name)

# Initialize Flask-Talisman with your Flask app
talisman = Talisman(
    app,
    content_security_policy={
        # ... other CSP directives ...
        'frame-ancestors': "'self'",
    },
)
