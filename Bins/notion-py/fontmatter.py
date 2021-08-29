from os import makedirs, path
from easygui import fileopenbox
from zipfile import ZipFile
from pathlib import Path
import frontmatter
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import TextBlock
from re import compile, search

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

regexfileUID = compile("(\.md)")

def scan_md_zip():
  title_erros = []
  for filename in zf.namelist():

    match = regexfileUID.search(filename)
    if not match:
      continue

    with zf.open(filename, "r") as mdFile:
      content = zf.read(filename)
      print(filename)
      try:
        post = frontmatter.loads(content)
        if 'title' not in post.keys():
          continue
        if 'notion_url' not in post.keys():
          continue
        new_title = post["title"]
        uid = post["notion_url"]
      except:
        print("ERROR")
        continue

      if new_title is None:
        title_erros.append(uid)

      page = client.get_block(uid)
      if page._type == "image" or page._type == "pdf":
        continue

      if (page.title != new_title):
        rename.append(uid + " : oldtitle = " + page.title)
        print("old: ", page.title)
        print("new: ", new_title)
        #page.title = new_title
  print("------------------------------")
  print("------------------------------")

  print(rename)

def sample():

  string = "%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F".split("%")
  print(string)
  string = ["0x"+string[i] for i in range(len(string))]
  print(string)
  bytes_unicode = bytes([int(string[i],0) for i in range(len(string))])
  print(bytes_unicode.decode('utf-8'))
  unicode_str = str(bytes_unicode, 'utf-8')
  print(unicode_str)

  b = ["â".encode('utf-8'), "b".encode('utf-8')]
  print(b)
  some = "something"
  print(some.encode('utf-8'))

def string_test(notion_mix_decoded_string):

  regexSpecialUtf8 = compile("%([A-F0-9][A-F0-9])")
  string = notion_mix_decoded_string
  encoded_str = []
  convert = ""
  while range(len(string)):
    special_utf8_match = regexSpecialUtf8.search(string[0:3])
    if (special_utf8_match):
      code = regexSpecialUtf8.sub("0x"+string[1:3], string[0:3])
      encoded_str.append(bytes([int(code, 0)]))
      string = string[3:]
    else:
      encoded_str.append(string[0].encode('utf-8'))
      string = string[1:]

  print(encoded_str)
  print(b''.join(encoded_str).decode('utf-8'))

scan_md_zip()