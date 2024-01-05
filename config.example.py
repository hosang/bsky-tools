import dataclasses


@dataclasses.dataclass
class Feed:
    record_name: str
    display_name: str
    description: str
    emoji: list[str]
    hashtags: list[str]


# Service
HOSTNAME = 'bsky.komagomama.com'
SERVICE_DID = f'did:web:{HOSTNAME}'

# Account
HANDLE = 'user.bsky.social'
PASSWORD = 'xxxx-xxxx-xxxx-xxxx'

# Feeds
FEED_URI = 'at://did:plc:..../app.bsky.feed.generator/'
FEEDS = []
