
def keyword_usage(sentence, list_of_words):
  my_tuple = ()
  for word in sentence.split():
    if word in list_of_words:
      my_tuple = my_tuple + (True,)
    else:
      my_tuple = my_tuple + (False,)
  return my_tuple

  
def main():
	sentence = input("")
	list_of_words = ['Python','python','scala']
	print(keyword_usage(sentence, list_of_words))

