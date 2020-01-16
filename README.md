# Hackathon
This is a project for the 2019 TriCo CIL Hackathon made by myself (William
Ball), Zoey Biulala, Derrick Zhen, and Alex Xuan. I wrote the documentation and
most of the python code, Zoey wrote the HTML and CSS (some of which was
unfortunately lost), Derrick found, cleaned, and organized all the data we used,
and Alex battled with Google to get us access to their API and helped clean
data with Derrick.

# Expungenation
## What is this?
As a part of the Hackathon, we interacted with the Philadelphia Lawyers for
Social Equity (PLSE), who said they really needed a website that could explain
the intricacies of expungement law, which varies wildly from state to state, as
well as direct potential clients to legal clinics near them, since they can only
do so much. We sought to implement this in Expungenation.

## What is left to do
We obviously couldn't complete the entire project in a weekend, so the project
is still incomplete. We would like to clean the data on expungement law and make
that more readable, but that would take a lot of time and research we simply
didn't have. On top of this, we would definitely like to clean it up and
generally make everything prettier and easier to use. We also tried to get in
touch with PLSE to actually deploy it, but they have not responded to us.

## How to view on your machine
We haven't deployed it, so it could be quite tricky to view for yourself. You
will need python 3 and a few libraries. I'm assuming you have python 3
installed. Attempt to run `python app.py` on Windows or `python3 app.py` on Mac
or Linux. This will probably not work since you don't have Flask installed. It
will complain saying you don't have one or more libraries installed, so you
should then run `pip install *library*` or `pip3 install *library*` or `python
-m pip install *library*` or some other variant with 3's in different places
until it works. Then run `python app.py`, open a browser, and type
`http://127.0.0.1:5000/` into the search bar of a browser and it should work.
