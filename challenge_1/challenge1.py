

def rot13(plaintext: str) -> str:
  plaintext.replace(".", "")
  # print(plaintext)
  letters = ["a","b","c","d","e","f","g","h","i","j",
          "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  size = len(plaintext)
  encripted =  ''
  index = 0
  index_of_space = plaintext.find(" ")
  if any(char.isdigit() for char in plaintext) or any(char!=" " and not char.isalnum() for char in plaintext):
    raise WrongInputException("Sorry, please enter only alphabets")
  while True:
    if size==0:break
    if index==index_of_space:
      encripted+= " "
    else:
      add_13 = (letters.index(plaintext[index].lower())+13)
      if add_13>26:
        encripted += letters[(add_13)%13]
      else:
        encripted += letters[(add_13)]
    index +=1
    size -=1
  return encripted


class WrongInputException(Exception):
    pass