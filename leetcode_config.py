# TODO: Currently session cookie and csrf token are a bit hard to get; One should get them from browser and store them 
# in external_services/leetcode_config.py; then they can be fetched from there
# guide on how to fetch them from browser: https://github.com/joshcai/leetcode-sync/blob/master/README.md - point 1.

# Better one: 
# Log in leetcode.com in chrome.
# Open chrome developer tools (F12)
# Click application.
# Expand storage->cookies.
# Copy and paste csrftoken and LEETCODE_SESSION.

LEETCODE_SESSION = ""
CSRF_TOKEN = ""


