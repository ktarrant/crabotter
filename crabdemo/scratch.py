from polls.models import Question, Choice
from django.utils import timezone

# >>> q = Question(question_text="What's new?", pub_date=timezone.now())

# # Save the object into the database. You have to call save() explicitly.
# >>> q.save()

# # Now it has an ID. Note that this might say "1L" instead of "1", depending
# # on which database you're using. That's no biggie; it just means your
# # database backend prefers to return integers as Python long integer
# # objects.
# >>> q.id
# 1

# # Access model field values via Python attributes.
# >>> q.question_text
# "What's new?"
# >>> q.pub_date
# datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# # Change values by changing the attributes, then calling save().
# >>> q.question_text = "What's up?"
# >>> q.save()

# # objects.all() displays all the questions in the database.
# >>> Question.objects.all()
# [<Question: Question object>]