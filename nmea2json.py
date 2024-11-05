from const import Const
import fileinput
import json

def main():
  result = []
  bean = []
  for line in fileinput.input():
    lst = line.strip().split("*")[0].split(",")
    sentence_type = lst[0]
    if sentence_type == "$GPGGA":
      result.append(bean)
      bean = []
    if sentence_type in Const().label_dict.keys():
      dct = {}
      for index in range(len(lst)):
        label = Const().label_dict[sentence_type][index]
        dct[label] = lst[index]
      bean.append(dct)
      
  print(json.dumps(result, indent=4))

main()
