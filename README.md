## Problem

Write a program that will subtract one list of time ranges from another. Formally: for two lists of time ranges A and B, a time is in (A-B) if and only if it is part of A and not part of B.

A time range has a start time and an end time. You can define timeas and time ranges however you want (Unix timestamps, date/time objects in your preferred language, the actual string "start-end", etc.).

Your solution shouldn't rely on the granularity of the timestamps (so don't, for example, iterate over all the times in all the ranges and check to see if that time is "in").

## Assumptions

 - All time ranges are on the same day and don't for example, wrap to the next day.
 - No time ranges overlap within the list itself.
 - Times are NOT sorted ascending (even though all examples are)

 ## Running Tests

 `python -m unittest tests`