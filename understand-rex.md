Think of rex as 3 things
| rex "PATTERN (?<FIELD_NAME>WHAT_TO_EXTRACT)"

For example:

| rex "to (?<destination_ip>\d+\.\d+\.\d+\.\d+)"

Break it down:

to → look for the word to
(?<destination_ip>...) → create a field called destination_ip
\d+ → one or more digits
\. → literal dot
repeated four times → IPv4 address

So if the log says:

Blocked connection from 203.0.113.10 to 10.0.0.156 port 443

Splunk extracts:

destination_ip = 10.0.0.156
What if the interviewer changes the question?

Suppose they ask:

"Write a Rex query to extract the source IP."

You don't memorize it. Look at the log:

Blocked connection from 203.0.113.10 to 10.0.0.156 port 443

You identify:

from 203.0.113.10

Then construct:

| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"

That's the skill they're testing.

Another example

Log:

Failed password for invalid user service from 203.0.113.10 port 54334

Interviewer:

Extract the IP.

You see:

from 203.0.113.10

So:

| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
The one pattern I want you to remember

For an IPv4 address:

\d+\.\d+\.\d+\.\d+

For creating a field:

(?<field_name>...)

Put them together:

| rex "WORD (?<field_name>\d+\.\d+\.\d+\.\d+)"

That's enough to start.

And this is exactly why we're doing the queries manually rather than just giving you a README of commands. You're learning how to build them from the log structure.