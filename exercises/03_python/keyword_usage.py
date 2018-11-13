def keyword_usage(sentence, list_of_words):
  my_tuple = ()
  for word in sentence.split(' '):
    if word in list_of_words:
      my_tuple = my_tuple + (true,)
    else:
      my_tuple = my_tuple + (false,)
  return my_tuple
