# Shopping List
SEI Project 2

This shopping list app is a full-stack application developed using multiple technologies listed below. The app can be used to organize and check off everything you need before and after you go shopping. It will feature different categories*, quantities* and multiple list features.
(* *COMING SOON*)

## [Click Here](https://shopping-list-ily8.onrender.com/lists) to see my live project!

## How to use
1. Sign Up/Log In or Use guest account
2. Click the ➕ to create a new list
3. Create a name for your list
4. Click on the list to open it
5. Type into the add item input and hit enter
6. Click the 🗑️ to remove the item
7. Click on the item to cross it off
7. Click the hamburger menu to return to all your lists or to log out
8. Click the ⭐ to favourite a list
8. Click the 🗑️ to remove the list
9. Sign Out


## Technologies Used
- HTML
- CSS
- Python
- SQL/PSQL
- Flask
- Psycopg2
- Bcrypt
- Render Cloud Hosting


## Initial Plan
1. Get log in/log out working :white_check_mark:
2. Lists can be added :white_check_mark:
3. Lists can be deleted :white_check_mark:
4. When in a list you can add items to it :white_check_mark:
5. Items can be deleted :white_check_mark:
6. Items can be checked off and crossed out :white_check_mark:

![Wireframe (User settings/all lists)](./images/All%20Lists.png)
![Wireframe (Coles list)](./images/Coles%20List.png)
![Wireframe (Woolworths lists)](./images/Woolworths%20List.png)

## Extra Plan
1. Items can then be split up into categories
2. Different users have different lists and items :white_check_mark:
3. User can remove their profile :white_check_mark:
4. Move items between lists :white_check_mark:
5. Send lists to other users
6. Export SQL data

## Struggles
Starting out instead of trying to just get each feature to work one by one, I tried to get it all working together at once making me waste a lot of my time trouble shooting bugs.

Deploying the website and getting Flask-session to work was a big issue for me and a few other students.

Coming up with ideas and features was probably the biggest trouble for me.

## Bugs to Fix
- If nothing is entered in the input field for adding a list or item it will still add data to the database.
- If you've crossed off an item then reload the page, the item doesn't stay crossed off.

## Future Features
- Items are automatically added into categories and displayed by their categories.
- SQL data from user can be exported to an excel spread sheet

## Sources Used
https://coolors.co/
https://stackoverflow.com/questions/59054548/js-get-the-clicked-element-with-event-target
https://stackoverflow.com/questions/59054548/js-get-the-clicked-element-with-event-target
https://stackoverflow.com/questions/35077658/css-selector-for-no-children-but-not-empty
https://developer.mozilla.org/en-US/docs/Web/CSS/:has#browser_compatibility
https://stackoverflow.com/questions/7298057/how-can-i-select-the-last-element-with-a-specific-class-not-last-child-inside-o
https://www.markdownguide.org/cheat-sheet/
https://www.databasestar.com/sql-boolean-data-type/