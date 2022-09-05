import wikipedia
import requests

page = wikipedia.page(
    "beach",
    auto_suggest=False                                  # solve DisambiguationError
                                                        # ref: https://stackoverflow.com/a/70409134
)
W = 20
print(f'{"page.url":<{W}.{W}}: {page.url}')
print(
    f'{"len(page.images)":<{W}.{W}}: '
    f'{len(page.images)}'
)
print(
    f'{"page.images[0]":<{W}.{W}}: '
    f'{page.images[0]}'                                 # get the first image URL
)

link = page.images[0]                                   # save the first image URL

response = requests.get(
    link,
    headers={                                           # solve error 403: https://stackoverflow.com/a/38489588
        "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.141 Safari/537.36"
    }
)                                                       # dowload the image
print(
    f'{"response.status_code":<{W}.{W}}: '
    f'{response.status_code}'
)

if response.status_code == 200:
    # print(response.content)
    filename = (                                        # get wikipedia image name from URL
        link                                            # URL
        .split("?")[-1]                                 # split to ? and return second-last or just the first
        .split("/")[-1]                                 # split to / and return second-last or just the first
    )
    print(f'{"filename":<{W}.{W}}: {filename}')

    with open(f'files/{filename}', 'wb') as file:       # save the file
        file.write(response.content)

