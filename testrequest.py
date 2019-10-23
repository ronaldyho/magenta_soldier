import requests
import io, json

# Declare dict "files" 
files = {
    'metadata': (None,
        io.BytesIO(json.dumps({"userid":"nolink"}).encode('ascii')),
        'application/json'),
    'media_file': ('binary', open('test.pdf', 'rb'), 'application/pdf')
}

# Ron: Troubleshoot
print ( str(files) )

r = requests.post("https://postman-echo.com/post",
        files=files)

print("Return body:", r.text)
print("Status code:", r.status_code)
print("Request time:", r.elapsed.total_seconds())


thefile = open('requestfile.txt', 'w')
thefile.write( str( r.request.body ) )


