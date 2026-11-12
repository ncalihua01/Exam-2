def filter_grades(dict,num):
  """
  dictionary of student names with respective grades -> filter out names of students above grade threshold
  filter_grades takes in a dictionary  of students' names as keys and their grades as values and a threshold
  number to filter out and print names of students who have grades above the specified threshold.

  >>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 95)
  'Abe'
  'Debbie'
  >>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 62)
  'Abe'
  'Cameron'
  'Debbie'
  """
  for name in dict:
    grade = dict[name]
    if grade > num:
      print(name)
