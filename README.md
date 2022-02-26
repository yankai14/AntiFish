# AntiFish
AntiFish is an extension that prevents users from accessing phishing links sent online. In addition, it provides a Telegram service which checks whether a link might be harmful.

## Checks
There are three levels of check performed.
1. Checks whether the content (if it is a URL) of an ```<a>``` tag matches the ```href``` value.
2. Calls a backend API hosted of GCP. The API verifies that the domain that the user is trying to reach is not a known phishing domain. A CRON job is scheduled to be ran every hour to update the database of the new phishing links.
3. The same backend API verifies that the URL must be exactly the same as known good websites such as banks or it has no similiarity to known good websites. This prevents any sort of phishing by the attacker where the attacker mimics trusted domains maliciously. This is done by matching the URL string with our database where ```THRESHHOLD < URL < 1``` are URLs that are too similar to known domains and thus are considered untrustworthy.

## Reporting
The Telegram bot supports a URL reporting function which submits the phishing URL to the backend. The backend in turn flags the domain as a possible phishing domain after investigation from the team.

## Hosting and Infrastructure
- Telegram bot is hosted on Heroku
- All backend APIs are hosted on GCPs cloud functions
- Database is hosted on GCP's firestore