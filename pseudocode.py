"""

Production; Counting Daily // Or Production Wise:

# Add in the main page will have you get a daily add view
- Where you give all rope bundles sorted by size & sepprated manually by , 
- Where you give all fibre bundles from inventory used & sepprated manually by , 

# Add will be availaible for each individual fibre or rope bale
# Update will be availaible for each individual fibre or rope bale
# Delete will be availaible for each individual fibre or rope bale

So we can do something like this where you can create a production record which is date
And then according to date a page will be created where you can input fibre bales used & rope bundles created

Fibre bales from inventory will be labeled as used & rope bundles will be inputted to inventory

So now we need an inventory thngy which will be like expenses with association but with 2 sub domains for fibre bales & rope bundles

For fibre bale, just weight, creation/inputted date & maybe we can have an is_sold attribute or associated_sale attribute for instancing if it is sold or not
For rope bundle,just weight & size, creation/inputted date & maybe we can have an is_sold attribute or associated_sale attribute for instancing if it is sold or not


Production -> 

    Add -> 
        Select Fibre Bales Used
        Input Bundles By Size Produced
    
    
Inventory ->

    Fibre Bale -> 
        Association
        Weight
        Addition/Creation Date

    Rope Bundle -> 
        Association
        Size Weight
        Production/Creation Date

    Fibre Bale -> Standard CRUD
    Rope Bundle -> Standard CRUD

    Showing Bundles & Bales

"""