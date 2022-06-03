#!/bin/bash

# Basic syntax

today=$(date)
echo $today # Format: Tue, May 31, 2022 09:22:34 PM

# Special formats
# date +'FORMAT'

# Examples

# weekday abbreviation
weekday=$(date +'%a') 
echo $weekday # Tue

# weekday
weekday=$(date +'%A') 
echo $weekday # Tuesday

# month  abbreviation
month=$(date +'%b') 
echo $month # Jan

# month 
month=$(date +'%B') 
echo $month # January

# local date and time
local=$(date +'%c') 
echo $local # Tue, May 31, 2022 09:22:34 PM

# century 
century=$(date +'%C') 
echo $century # 20

# day 
day=$(date +'%d') 
echo $day # 31

# date in %m/%d/%y
date=$(date +'%D') 
echo $date # 05/31/22

# day 
day=$(date +'%e') 
echo $day # 31

# day %Y-%m-%d
date=$(date +'%F') 
echo $date # 2022-05-31

# last two digits of year 
year=$(date +'%g') 
echo $year # 22

# year  
year=$(date +'%G') 
echo $year # 2022

# month abbreviation 
month=$(date +'%h') 
echo $month # May

# hour in military format (00..23)  
hour=$(date +'%H') 
echo $hour # 23

# hour (01..12)  
hour=$(date +'%I') 
echo $hour # 11

# day of year  
day=$(date +'%j') 
echo $day # 151

# hour in military format, space padded  
hour=$(date +'%k') 
echo $hour # 23

# hour, space padded  
hour=$(date +'%l') 
echo $hour # 11

# month  
month=$(date +'%m') 
echo $month # 05

# minute 
minute=$(date +'%M') 
echo $minute # 46

# newline 
newline=$(date +'%n') 
echo $newline # 

# nanoseconds   
nanoseconds=$(date +'%N') 
echo $nanoseconds # 683594800

# AM or PM  
ampm=$(date +'%p') 
echo $ampm # PM

# am or pm 
ampm=$(date +'%P') 
echo $ampm # pm

# quarter  
quarter=$(date +'%q') 
echo $quarter # 2

# time 
time=$(date +'%r') 
echo $time # 10:49:30 PM

# time in military format  
time=$(date +'%R') 
echo $time # 22:49

# seconds since 1970-01-01 00:00:00 UTC 
timestamp=$(date +'%s') 
echo $timestamp # 1654066170

# second   
second=$(date +'%S') 
echo $second # 17

# tab 
tab=$(date +'%t') 
echo $tab # 

# time; same as %H:%M:%S 
time=$(date +'%T') 
echo $time # 23:52:17

# day of week (1-7); 1 is Monday
day=$(date +'%u') 
echo $day # 2

# week number of year, with Sunday as first day of week   
week=$(date +'%U') 
echo $week # 22

# ISO week number 
week=$(date +'%V') 
echo $week # 22

# day of week (0-6); 0 is Sunday 
day=$(date +'%w') 
echo $day # 2

# week number of year, with Monday as first day of week
week=$(date +'%W') 
echo $week # 22

# local date 
date=$(date +'%x') 
echo $date # 06/ 1/2022

# locale’s time 
time=$(date +'%X') 
echo $time # 12:04:42 PM

# last two digits of year
year=$(date +'%y') 
echo $year # 22

# year
year=$(date +'%Y') 
echo $year # 2022

# +hhmm numeric time zone 
zone=$(date +'%z') 
echo $zone # -0700

# +hh:mm numeric time zone
zone=$(date +'%:z') 
echo $zone # -07:00

# +hh:mm:ss numeric time zone
zone=$(date +'%::z') 
echo $zone # -07:00:00

# numeric time zone with : to necessary precision
zone=$(date +'%:::z') 
echo $zone # -07

# alphabetic time zone abbreviation (e.g., EDT)
zone=$(date +'%Z') 
echo $zone # PDT