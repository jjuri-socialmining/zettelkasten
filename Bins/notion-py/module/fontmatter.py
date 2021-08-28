import yaml

def get_yaml(file):
  pointer = file.tell()
  if file.readline() != '---\n':
    file.seek(pointer)
    return ''
  readline = iter(file.readline, '')
  readline = iter(readline.__next__, '---\n')

  return ''.join(readline)


def test_yaml():
  
  with open("./yaml.yaml", encoding="utf8") as file:
    config = yaml.load(get_yaml(file))
    text = file.read()
    print("TEXT from", "yaml.yaml")
    print(text)
    print("CONFIG from", "yaml.yaml")
    print(config)

if __name__ == "__main__":
    test_yaml()
