### This tool leverages the SIEGE tool 
###   https://github.com/JoeDog/siege

def main():

    inUser_ID  = defaultInitUser
    inTeam_ID  = VALID_TEAM_JID

    url = []
    url.append( "https://amazing.com/api/{better}".format(better=inGroup_ID) )

    reps = 1
    concurrency = 1

    for urlX in url:
        COMMAND = 'siege --benchmark --rc="siege_qa.conf" --reps={reps} --concurrent={concurrent} "{url}" --header "Authorization: Bearer {headerJWT}"'.format(reps=str(reps),
            concurrent=str(concurrency), 
            headerJWT=JWT_TOKEN.decode('utf-8'),
            url=urlX)
        print( COMMAND )
        subprocess.call( COMMAND, shell = True )
