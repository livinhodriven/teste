vogais = ["a", "e", "i", "o", "u"]

def vogal(str):
  if(len(str) > 1):
    return False
  
  return str.lower() in vogais