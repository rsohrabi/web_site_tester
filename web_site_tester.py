"""
a simple test of given web site URL for online
It is important to give web site url as: http://www.google.com
else a schema error is dumped.

"""
import sys
import requests
import time

# defults and globals
HORIZONTAL_DASH = 60
ALLOW_REDIRECTS = False
TIME_PLACES = 3

# input must have at least 2 inputs.
if len(sys.argv) < 2:
    print("Usage: {} site1 site2 site2...".format(sys.argv[0]))
    print("Verify input web sites are online.")
    sys.exit(0)

print("Checking web site status for:")
print("   ".join(sys.argv[1:]))

print("-" * HORIZONTAL_DASH)
try:
    for site in sys.argv[1:]:
        tc1 = time.clock()
        r = requests.head(site, allow_redirects=ALLOW_REDIRECTS)
        tc2 = time.clock()
        print("Site URL:", site)
        print("Returned results:")
        print("return.ok:", r.ok)
        print("return.status_code:", r.status_code)
        print("Web site response time:", round(tc2 - tc1, TIME_PLACES), "secs")
        print("-" * HORIZONTAL_DASH)
except requests.ConnectionError as ce:
    print("Error: ConnectionError: {}".format(ce))
    sys.exit(1)
except requests.exceptions.MissingSchema as ms:
    print("Error: MissingSchema: {}".format(ms))
    sys.exit(1)
except Exception as e:
    print("Error: Exception: {}".format(e))
    sys.exit(1)
