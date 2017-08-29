from __future__ import division
import random
from datetime import datetime

def generate_shakes(strlen):

  alphabet = "abcdefghijklmnopqrstuvwxyz "
  reserve = ""

  for i in range(strlen):
      reserve = reserve + alphabet[random.randrange(27)]

  return reserve

def score(goal, teststring):

    match = 0

    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            match = match + 1

    return match/len(goal)

def main():

    start_time = datetime.now()

    print "String Matching started at %s" % (start_time)

    #goalstring = "methinks it is like a weasel"
    goalstring = "viable"
    newstring = generate_shakes(len(goalstring))
    total_executions = 0
    top_score = 0
    newscore = score(goalstring, newstring)

    while newscore < 1:
        total_executions = total_executions + 1

        if total_executions % 1000000 == 0:
            print "Duration %s; %s string match tests" % (datetime.now()-start_time, total_executions)

        if newscore > top_score:
            timestamp = datetime.now()-start_time
            top_score = newscore

            print "Duration %s; Total Executions %s with score of %s for string %s" % (timestamp, total_executions, top_score, newstring)

        newstring = generate_shakes(len(goalstring))
        newscore = score(goalstring, newstring)


    total_executions = total_executions + 1
    timestamp = datetime.now()-start_time
    top_score = newscore

    print "Duration %s; Total Executions %s with score of %s for string %s" % (timestamp, total_executions, top_score, newstring)

main()
