# women_in_science

## Project Overview
A project designed to promote **women in science**. A website that presents a user with a **log-in form** that allows the user to select certain **preferences**. A preference may include queries such as: **minority status**, **field of study**, **degree** and **availability** for speaking engagements.

Once a user sets up this profile, the site will select a random scientist to display.

## Functionality
A user will see a "register" screen that will allow them to build a profile with preferences. The site will use the preferences to query the [UIS Developer Portal](https://apiportal.uis.unesco.org/) API and display the results.

## Data Model
The user will have several ###fields: user name, password, e-mail address, preferences.

Preferences will have the following fields: minority status, geographical location, field of study, degree, availability for speaking engagements.

## Schedule
Week One:
  Set up Django App structure
  Use Axios, Ajax and JSon to query API
  Use HTML, CSS and Materialize to style and present the Data
  Create a Chrome extension to offer up a different scientist when user goes to a new tab.
