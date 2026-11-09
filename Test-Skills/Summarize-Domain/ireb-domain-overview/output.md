# Introduction: GOV.UK Notify

No documents were provided, and no law or formal standard defines GOV.UK Notify, so the primary source used is the government's binding policy mandate on central services; Notify's data processing and financial agreement (a PDF) could not be read.

## Core purpose

GOV.UK Notify is a shared platform that the Government Digital Service (GDS, the UK government's central digital team) builds and runs. Public sector teams use it to send emails, text messages (SMS, short message service) and printed letters to the people who use their services [SRC 2, SRC 3, SRC 4]. Teams can send messages by hand through a web interface, for example by uploading a spreadsheet of recipients. They can also send them automatically from their own web applications or back-office systems through an API (application programming interface, a defined way for software systems to talk to each other) [SRC 3, SRC 9]. Only public sector organisations can use Notify, such as central government departments, local authorities, the NHS, emergency services and state-funded schools. It is not for personal use [SRC 5]. Government services that send notifications by email, post or SMS must use Notify for this unless technical reasons prevent it, and those reasons must be explained in the spend request [SRC 1].

## Key benefits

- **BEN 1: Low cost and no procurement** - Public sector organisations pay no monthly charge or setup fee and do not have to go through a procurement process. Emails are free and unlimited, and they get a free yearly allowance of text messages. After that they pay per text message and per letter [SRC 3, SRC 7].
- **BEN 2: Service teams can send messages without developers** - Content designers, caseworkers and contact centre staff can create templates and send one-off or bulk messages without technical knowledge. Developers are needed only to automate sending [SRC 3, SRC 4, SRC 8].
- **BEN 3: Faster and cheaper service delivery for government** - Because Notify is a common platform, teams do not have to build and run their own messaging solution. This helps them deliver services that meet user needs faster and at lower cost [SRC 2].
- **BEN 4: Citizens get information quickly** - Notify aims to send 95% of emails and text messages within 10 seconds, and to print and post letters by 3pm on the next working day [SRC 4].
- **BEN 5: Teams can see what reached people** - Teams can track how many messages they have sent and which ones were not delivered, so they can follow up [SRC 3, SRC 9].

## Common use cases

- **UC 1: Prepare message templates** - A content designer in a service team writes email, text message or letter templates and adds personalisation placeholders, for example for a name or a reference number. The placeholders are filled in for each person when the message is sent [SRC 4, SRC 8, SRC 9].
- **UC 2: Send one-off or bulk messages by hand** - A caseworker or contact centre agent sends a single message, or uploads a spreadsheet of email addresses or phone numbers to send a batch of messages, through the web interface [SRC 3, SRC 8].
- **UC 3: Send automatic notifications from a service** - A developer connects the service's own system to the Notify API. The system then automatically sends status updates, requests for action, acknowledgements of applications and reminders, and can check whether each message was delivered [SRC 8, SRC 9].
- **UC 4: Send printed letters** - A service team sends letters from a template, or uploads a ready-made PDF letter. Notify prints and posts the letter with the postage class the team chooses [SRC 4, SRC 9].
- **UC 5: Receive text message replies** - A service team turns on two-way text messaging, so that members of the public can reply by text and the service can read their replies [SRC 4, SRC 7, SRC 9].

## Sources

| ID | Title | URL | Edition or date | Reading status |
|---|---|---|---|---|
| SRC 1 | Use mandated central services (GDS and Central Digital and Data Office) | https://www.gov.uk/guidance/use-mandated-central-services | Published 23 February 2024 | full |
| SRC 2 | Service Manual: Using common platforms | https://www.gov.uk/service-manual/technology/using-common-components | Last updated 3 September 2024 | full |
| SRC 3 | GOV.UK Notify: Send emails, text messages and letters to your users (home page) | https://www.notifications.service.gov.uk/ | not stated | full |
| SRC 4 | GOV.UK Notify: Features | https://www.notifications.service.gov.uk/features | not stated | full |
| SRC 5 | GOV.UK Notify: Who can use Notify | https://www.notifications.service.gov.uk/features/who-can-use-notify | not stated | full |
| SRC 6 | GOV.UK Notify: Terms of use | https://www.notifications.service.gov.uk/terms | Last updated 3 June 2024 | full |
| SRC 7 | GOV.UK Notify: Pricing – text messages | https://www.notifications.service.gov.uk/pricing/text-messages | Last updated 1 April 2026 | full |
| SRC 8 | GOV.UK Notify live assessment report | https://www.gov.uk/service-standard-reports/gov-dot-uk-notify-live-assessment-report | Assessed 10 November 2020, published 16 February 2021 | full |
| SRC 9 | GOV.UK Notify: REST API documentation | https://docs.notifications.service.gov.uk/rest-api.html | not stated | full |

SRC 6 was read as background on the obligations that service teams accept, for example that recipients must have consented to their data being used and that unsolicited messages are not allowed. No element above cites it directly. No element is based on model knowledge alone.
