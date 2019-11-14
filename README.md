# Women In Science

## Project Overview
A project designed to promote **women in science**. A website that presents a user with a **log-in form** that allows the user to select certain **preferences**. A preference may include queries such as: **minority status**, **field of study**, **degree** and **availability** for speaking engagements.

Once a user sets up this profile, the site will select a random scientist to display.

## Functionality
A user will see a **register** screen that will allow them to build a **profile** with preferences. The site will use the preferences to query the [UIS Developer Portal](https://apiportal.uis.unesco.org/) API and display the **results**.

## Data Model
The user will have several **fields**:
- user name
- password
- e-mail address
- preferences.

### Preferences
Will have the following **fields**:
- minority status
- geographical location
- field of study
- degree
- availability for speaking engagements.

## Schedule
  1. [] Explore and study the API structure
  2. [] Get and save the key
  3. [] Set up Django App structure
  4. [] Create user CRUD
  5. [] Employ Axios, Ajax and JSon to query API
  6. [] Use Python to randomize the selected data
  7. [] Use HTML, CSS and Materialize to style and present the data
  8. [] Create a Chrome extension to offer up a different scientist when user goes to a new tab.
