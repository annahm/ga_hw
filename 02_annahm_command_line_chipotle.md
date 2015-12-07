## Class 2 Homework: Command Line Chipotle

#### Submitting Your Homework

* Create a file that includes your answers **and** the code you used to arrive at those answers. (feel free to use Markdown if you want)
* Add this file to your homework repo that you will use for all of your coursework. Push your changes up to GitHub.
* Submit a link to your repo using the [homework submission form] (http://goo.gl/forms/EamVci00DO).

#### Command Line Tasks

1. Look at the head and the tail of **chipotle.tsv** in the **data** subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you are unsure, look at more of the file contents.)
    * order_id: Represents the orders that were made at Chipotle. Within each order are multiple food items from the Chipotle menu. 
    * quantity: Quantity of a food item for a given order.
2. How many orders do there appear to be?
    * cut -f1 chipotle.tsv | tail -5
    * 1833
    * 1833
    * 1834
    * 1834
    * 1834
    * there are 1834 orders in this file.
3. How many lines are in this file?
    * wc -l chipotle.tsv 
    * 4623 lines in file
4. Which burrito is more popular, steak or chicken?
    * Chicken Burrito is more popular ("grep "Chicken Burrito" chipotle.tsv | wc -l" yields 553 lines and doing the same for Steak Burrito yields 368).
5. Do chicken burritos more often have black beans or pinto beans?
    * grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | wc -l
    *  282
    * grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | wc -l
    *  105
    * grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | grep "Pinto Beans" | wc -l
    *  20
    * Black beans. There are 282 lines which show black beans, 105 with pinto, and 20 lines with both.
6. Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.
    * $ ls -l *.csv *.tsv
    * -rwxrwxr-x. 1 anna anna    2266 Dec  2 20:30 airlines.csv
    * -rwxrwxr-x. 1 anna anna  579778 Dec  2 20:30 bank-additional.csv
    * -rwxrwxr-x. 1 anna anna  648353 Dec  2 20:30 bikeshare.csv
    * -rwxrwxr-x. 1 anna anna  364975 Dec  2 20:30 chipotle.tsv
    * -rwxrwxr-x. 1 anna anna    4973 Dec  2 20:30 drinks.csv
    * -rwxrwxr-x. 1 anna anna   22555 Dec  2 20:30 hitters.csv
    * -rwxrwxr-x. 1 anna anna   91499 Dec  2 20:30 imdb_1000.csv
    * -rwxrwxr-x. 1 anna anna  477907 Dec  2 20:30 sms.tsv
    * -rwxrwxr-x. 1 anna anna   60302 Dec  2 20:30 titanic.csv
    * -rwxrwxr-x. 1 anna anna 3004097 Dec  2 20:30 ufo.csv
    * -rwxrwxr-x. 1 anna anna      99 Dec  2 20:30 vehicles_test.csv
    * -rwxrwxr-x. 1 anna anna     354 Dec  2 20:30 vehicles_train.csv
    * -rwxrwxr-x. 1 anna anna 8091185 Dec  2 20:30 yelp.csv

7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT8 repo.
    * $ find . | xargs grep 'ictionary' > dict.out
    * $ grep ictionary dict.out > dict.out2
    * $ wc -l dict.out2
    * 123 dict.out2

8. **Optional:** Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!

    * $ cut -f3 chipotle.tsv > out
    * $ sort out > out.sort
    * $ uniq out.sort > out.sort.uniq
    * $ wc -l out.sort.uniq
    * 50 out.sort.uniq
    * Note: out of 1834 orders or a total of 4623 individual servings of food items, Chipotle only has 50 unique menu items including drinks.  This is an example of a good restaurant that focuses on a smaller number of menu items and does it well.  

<!---
-->
