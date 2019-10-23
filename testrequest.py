import requests
import io, json


def main():
    files = {
        'metadata': (None,
            io.BytesIO(json.dumps({"userid":"nolink"}).encode('ascii')),
            'application/json'),
        'media_file': ('binary', open('test.pdf', 'rb'), 'application/pdf')
    }

    r = requests.post("https://postman-echo.com/post",
            files=files)

    print("Return body:", r.text)
    print("Status code:", r.status_code)
    print("Request time:", r.elapsed.total_seconds())


#############################################
# RON: Troubleshoot
#  thefile = open('requestfile.txt', 'w')
#  thefile.write( str( r.request.body ) )
#############################################


class Person:
    username_enabled = "johnwick"
    username_suspended = "mopheus"
    username_deleted = "knock_knock"

class Files:
    file_small = "small.pdf"
    file_large_upper_boundary = "larger.pdf"
    file_too_large = "past_max_size.pdf"


x = vars(Person)
x.get('username_enabled')


