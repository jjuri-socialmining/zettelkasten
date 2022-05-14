from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="f969bce40b512d89812546f29318b3575d25694bb16cfe9430f609c92dd595c91a8dfe48796d23601d626791143f5f89408d59b644e02d09cb55b703eeed519cc8a136bb50f5c9a37855eee110be")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/560f8008018a4e9cb86ffee45ebb2d23")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"