
def keyword_usage(sentence, list_of_words):
  my_tuple = ()
  splitted_sentence = sentence.split()
  for word in list_of_words:
    if word in splitted_sentence: 
      my_tuple = my_tuple + (True,)
    else:
      my_tuple = my_tuple + (False,)
  return my_tuple

  
def main():
	sentence = input("")
	list_of_words = ['Python','python','scala']
	print(keyword_usage(sentence, list_of_words))
