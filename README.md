# SecretSanta
This is a Secret Santa matchmaker that I whipped up for my family. It randomly assigns Secret Santa matches without letting the organizer (me) know who is assigned to whom, maintaining the element of surprise.

I just used my gmail account and an [app password](https://support.google.com/mail/answer/185833?hl=en) to send the emails. Note that this is not a recommended path, but I could not be arsed to set up OIDC for this.

This is not good code. I mostly just wanted to play around with python because it had been a while. You may end up sending an email to your family at 3am and then going "oops not that one."

## Usage
In inputs/participants, enter in a list all the participants, csv style.
name,email

In illegal_pairs, enter in csv style the names that you don't want paired together (e.g. themselves or their spouses, as assumedly spouses will be giving each other gifts anyway).
name1,name1
name2,name2
name1,name2

In emailer, replace the cringely hardcoded user account/pw information (where it says INSERT...HERE).

Enjoy and don't contact me about this