from os import makedirs, path
from easygui import fileopenbox
from zipfile import ZipFile
from pathlib import Path
import frontmatter
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import TextBlock

client = NotionClient(token_v2="f969bce40b512d89812546f29318b3575d25694bb16cfe9430f609c92dd595c91a8dfe48796d23601d626791143f5f89408d59b644e02d09cb55b703eeed519cc8a136bb50f5c9a37855eee110be")


NotionZip = Path(fileopenbox(filetypes = ['*.zip']))

zf = ZipFile(NotionZip, 'r')

rename = []

def check_block(page):
  if len(page.children) == 0:
    print(f"{page.title} doesnt has blocks!")
  else:
    print(f"{page.title} has {len(page.children)} blocks")
    print("   |")
    for child in page.children:
      print("   +-", child.title)

#my_block.move_to(video, "after")
#my_block.move_to(otherblock, "last-child")

def block_add(page, title_str="something to do first"):
  return page.children.add_new(TextBlock, title=title_str)


def find_line(page, line_title="Notes:"):

  is_exist = False
  idx = 0

  if len(page.children) == 0:
    block_add(page, title_str="")

  for idx in range(len(page.children)):
      if page.children[idx].title == line_title:
        is_exist = True
        break

  return [is_exist, idx]

def update_note(page, content):
  start = 0
  end = 0
  note_info = find_line(page, line_title="Notes:")
  thought_info = find_line(page, line_title="Thoughts:")

  if not note_info[0] and not thought_info[0]:
    note_info[1] = block_add(page, "Notes:")
    thought_info[1] = block_add(page, "Thoughts:")

  if note_info[0] and not thought_info[0]:
    thought_info[1] = block_add(page, "Thoughts:")

  if not note_info[0] and thought_info[0]:
    note_info[1] = block_add(page, "Notes:")
    note_info[1].move_to(thought_info[1], "before")

  note_info = find_line(page, line_title="Notes:")
  thought_info = find_line(page, line_title="Thoughts:")

  i =0 
  for note in content:
    need_add = True

    for b_id in range(note_info[1], thought_info[1]):
      if note == page.children[b_id].title:
        need_add = False

    if need_add:
      print(f"Update {note} in page {page.title}")
      child = block_add(page, note)
      child.move_to(page.children[thought_info[1]+i], "before")
      i += 1

def get_note_content_md(mdFile):
  note_content = []
  idx = 0
  first = 0
  end = 0
  for line in mdFile:
    idx += 1
    line_decode = line.decode("utf-8").rstrip()

    if line_decode == "## Notes:":
      first = idx

    if line_decode == "## Thoughts:":
      break

    if first != 0 and first != idx and line_decode != "":
      note_content.append(line_decode)

  return note_content


def scan_md_zip():
  for filename in zf.namelist():

    with zf.open(filename, "r") as mdFile:
      content = zf.read(filename)
      post = frontmatter.loads(content)
      new_title = post["title"]
      uid = post["Notion_UID"]

      page = client.get_block("https://www.notion.so/" + uid)
      if (page.title != new_title):
        rename.append("https://www.notion.so/" + uid + " : oldtitle = " + page.title)
      
      content = get_note_content_md(mdFile)
      update_note(page, content)

scan_md_zip()