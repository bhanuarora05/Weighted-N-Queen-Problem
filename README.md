# Weighted-N-Queen-Problem

# Description
You are helping the LA Dept of Transportation (LADOT) to develop apilot scooter program for LA. There are a limited number of police officers available to monitor and address issues that may arise from scooters, ranging from traffic and safety violations to accidents with cars, bikes, other scooters and pedestrians. The scooter companies have given LADOT access to scooterroutes over the course of one day. In order to maximize the scooter activity monitored by the officers, you will take as input theroute information,the monitored city area dimensions, and the number of officers available to then generate the best placement of the officers.The officers can only be in one place for one day, and there can only be one officer on each street. When an officer and scooter are at the same location at the same time, the officer is able to address a safety issue, and one “Activity point”is gained.The  goal  is  to  place  the  officers  in  locations  that  do  not conflict with each other, while maximizing the total “Activity points” for the day(12 time steps in a day).  The problem follows these rules:-
•Officers cannot be in same square,same row, same column, or along the same diagonal. (Think of queens on a chess board)
•Officers cannot move.
•Activity points are collected at each time step t when officers are in same square as scooters. One point per each scooter. 
•The grid coordinate system will be indexed starting from the top-left corner.

Input: The file input.txt in the current directory of your program will be formatted as follows: First line: strictly positive 32-bit integer n, the width and height of the nx ncity area, n<= 15.Second line: strictly positive 32-bit integer p, the number of police officersThird line: strictly positive 32-bit integer s, the number of scootersNext s*12lines: the list of scooter x,y coordinatesover time, separated with the End-of-line character LF.  With sscooters and 12 timestepsin a day, this results in 12 coordinatesper scooter.
Output: Max activity points:strictly positive 32-bit integer m
