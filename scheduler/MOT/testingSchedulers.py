"""
Created on 31 March 2017
@author: Charlotte Alexandra Wilson

Last revision: 05 April 2017
---------------------------------------------------------------
Testing various constants and variables for scheduler output
"""

import datetime
import time
import csv
from itertools import groupby
from scheduler.models import Mission, NextPass
from scheduler.MOT import GA as ga


def test(passes, run_time):
    csv_name = "scheduler_compare.csv"
    resultFile = csv.writer(open(csv_name, 'a', newline=''))

    first_pass = passes.first().riseTime
    print("FIRST PASS: " + str(first_pass))
    end_pass = passes.last().setTime
    print("END PASS: " + str(end_pass))

    duration = end_pass - first_pass

    mission = Mission.objects.all()
    num_missions = len(mission)

    next_pass_test = ga.nextPassChromosome(passes)
    fitness_score = ga.nextPass_fitness_3(next_pass_test)

    total_contact_time_seconds = 0
    for item in passes:
        if item.duration is not None:
            total_contact_time_seconds += item.duration.seconds

    """convert total contact time to date time object """
    total_contact_time_int = datetime.timedelta(
        seconds=total_contact_time_seconds)
    total_non_contact_time = duration - total_contact_time_int

    contact_time_percentage = str(round(
        ((total_contact_time_int / duration) * 100), 2)) + "%"

    resultFile.writerow(
        [num_missions, duration, total_contact_time_int,
         total_non_contact_time, contact_time_percentage,
         fitness_score, str(run_time)])

    print("TOTAL DURAITON: " + str(duration) +
          "=======================================")
    print("TOTAL CONTACT TIME: " + str(total_contact_time_int) +
          "=======================================")
    print("TOTAL NON CONTACT TIME: " + str(total_non_contact_time) +
          "=======================================")
    print("CONTACT TIME PERCENTAGE: " + str(contact_time_percentage) +
          "=======================================")


def stats_each_sat(passes, run_number="unspecified"):
    """
    the first item with that name, create a new variable named
    after it? then start a count?

    """

    csv_name = "scheduler_compare_stats.csv"
    resultFile = csv.writer(open(csv_name, 'a', newline=''))
    resultFile.writerow(['run number ' + str(run_number)])
    resultFile.writerow(['Satellite Name', 'Num Passes',
                         'Total Contact Time', 'Avg Time per Pass',
                         'priority'])

    pass_dict = {}

    for item in passes:
        if item.tle.name not in pass_dict:
            pass_dict[item.tle.name] = []
            pass_dict[item.tle.name].append(item)
        else:
            pass_dict[item.tle.name].append(item)

    print("Dictionary")
    for keys, values in pass_dict.items():
        pass_name = ""
        number = 0
        avg = 0
        total_contact_time = 0
        for item in values:
            pass_name += item.tle.name + " "
            priority = item.mission.priority
            if item.duration is not None:
                total_contact_time += item.duration.seconds
            number += 1
        # Average time per pass
        if item.duration is not None:
            avg = item.duration.seconds / number
            average = datetime.timedelta(
                seconds=avg)
        else:
            average = "Data Problem"
        # convert total contact time to datetime...
        total_contact_time = datetime.timedelta(
            seconds=total_contact_time)
        print(number, total_contact_time, keys)
        resultFile.writerow(
            [keys, number, total_contact_time, average, priority])
        print('\n')
