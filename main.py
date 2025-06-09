import os
os.environ.setdefault("PLAIN_SETTINGS_MODULE", "app.settings")

import plain

if __name__ == "__main__":
    plain.run()