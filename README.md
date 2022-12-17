# It's like Uber, but for recipes

KEY ISSUE: Idk if we can do this if we are not a grocery store. Feels like api won’t let us spam other stores. Let me know if you see anything different. Otherwise basic idea below.

Pain point
It is irritating to populate an instacart order with the UI - have to click through too many screens

Basic idea
User types grocery list into one window, and it auto-populates an instacart order with best estimates for the specific sku (e.g., 2% milk is placed in cart as 2% horizon milk). 

What it might need:
A website with basic UI
Instacart fulfillment api
Instacart recommendation api
Link to user instacart account
Database (and maybe cookies)  for remembering past user orders and preferences

Key piece for implementation:

Instacart cleanly outlined a process for creating an order (link) - unsure how straight forward it will be though. The key piece will probably be this part:



We could make a database of generic UPC codes (they are standardized for all grocery products) and then spam the recommendation api to get the specific item (i.e., user puts in milk; we spam api for top milk recommendation; put recommendation in cart). Flow might be something like this:

User input: 2 % milk
Query database for 2% milk upc
Send milk upc to instacart recommendation api for specific product 

Another challenge, the instacart apis might be for grocery stores and not for standalone developers. We could contact instacart for a work around. If that doesn’t work, amazon fresh might have an api.

V2 Features
Remember past orders 
Allow users to set preferences for item choices - e.g., always choose cheapest option/organic option
