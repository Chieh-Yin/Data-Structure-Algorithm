import textwrap

def feedbackReview(feedback, size):
    return [] if feedback == "" else textwrap.fill(feedback, width=size).split('\n')
