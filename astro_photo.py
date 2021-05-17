def astro():
    import os
    import json
    import requests
    from dotenv import load_dotenv
    ATOKEN = os.getenv('APOD_TOKEN')
    url = 'https://api.nasa.gov/planetary/apod?api_key={0}'
    url2 = url.format(ATOKEN)

    response = requests.get(url2)
    response.raise_for_status()

    astro = json.loads(response.text)
    main = astro['url']
    return(main)
