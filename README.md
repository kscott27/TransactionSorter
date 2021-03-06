# TransactionSorter

## Instructions for setting up the development environment

From the root of this repository, run the following script to install PyQt5 and a few other module dependencies (python3 and pip3 must already be installed on your system for this script to work):

`$ bash ./env/install-pyqt5.sh`

Once the dependencies are installed, the program can be run with the following command:

`$ python3 BootGUI.py`

The GUI window should appear and the program should be running.


## Program design insight

The TransactionSorter is a personal financial management application. It offers several 
analytical tools for a comprehensive overview of the user’s financial standing- past, present,
and future. The application takes several user-defined benchmarks that will then itemize
transactions and project balances based on the user’s financial goals. Though the application
has bugs and is still in early stages, it offers useful data for spending analysis right now. There are
several other features that can be implemented in the future: these include a more flexible
projection plot based on priority of planned transactions(which the back-end is already prepared
to do), adjusting transactions for venmo reimbursements, and tracking other assets like stocks,
bonds, and commodities. The interface consists of four tabs: Setup, Planning, Categorize, and
Analysis. Each tab offers tools to create a comprehensive analysis of the user’s financial 
standing.


The application opens up in the Setup tab. There, the user has the option to enter their 
current checking account balance, their income, the frequency of their income (ex: $2500 
bi-weekly). In addition, they specify the date of their next pay day and when they pay 
off their next credit card bill. This information is used to run the cash projection 
analysis. The rest of the application is available for use without entering this 
information. However, if the user wants to see their projection, they will need to enter
their current standing in order to provide an accurate prediction. The other button in 
the Setup tab will open a file manager to select a CSV of their credit card statement.
Banks offer downloadable CSV files that can be accessed easily on their website. Once
it's downloaded, the application can read the CSV and parse all transactions into 
items within the app that can be categorized and recorded. 

  
After the CSV file is imported and parsed by the application, the user can create additional
“planned transactions” in the Planning tab. The interface allows the user to specify what 
category the transaction belongs in, the amount, recurrence (if any), and if the 
transaction will be paid out of the user’s checking account or credit card. Once a Planned 
Transaction is created, it will be visible in the window- arranged by category. Planned 
Transactions are saved in the application as supplemental data for analysis of the user’s 
financial standing. 

  
After the Planned Transactions are created, the user can manually sort their completed 
transactions imported from the CSV file. This window has buttons to create, edit, and delete 
categories that reflect the user’s spending (ex: Groceries, Hobby, Restaurants, 
Transportation). All completed transactions will appear in a “Unhandled” window, waiting 
to be sorted. The user can drag and drop transactions into the appropriate category. If 
there are several transactions at the same location (ex: a particular gas station), all 
identical transactions will be automatically sorted into the same category. 
Additionally, the name of that location will be linked to the category; any later 
transaction will be automatically sorted when data is pulled from a different CSV. 

  
After the planned transactions are created and completed transactions are sorted, the 
application has enough information to create a comprehensive analysis of the user’s spending 
and future projection. The Analysis tab has a window that tracks the essential figures for 
each category: allotment, planning, spent, and balance. Below that table, there are figures 
that tell the user how much of their budget they have spent. The figures will be checked to 
see if they are close to overspending. If there is a chance of overspending, the application
will flag the category and represent it in a different color. Within the Analysis tab, there 
are two buttons that will open pop-up windows with plotting capabilities. The first button 
is the Credit Card Analysis button. That will review all completed transactions and offer a 
bar graph, pie chart, and time series visualization of the user’s spending. The bar graph 
compares the amount spent versus the amount allotted for each category. The pie chart 
represents the amount spent for each category proportional to the total budget. The time 
series shows what the balance of the user’s credit card was throughout the time period the 
CSV held. The other tool offer is the projection analysis; the application will plot out the
user’s projected checking account balance over 1 year. It makes this prediction based on 
their Setup tab data, and the Planned Transactions. Any Planned Transactions that will be 
paid out of the checking account will occur in the time series projection, as well as 
recurring credit card payments based on sum of the allotted amount for each category. 
Overall, the application will create a time series plot based on the user’s income, their 
credit card payment, and their planned transactions. 

  
The application in its current state can offer useful information for anyone interested in 
understanding their spending habits and budgeting. Though in its early stages, it has all of 
the basic tools. The more information that the user can specify in regards to their budget 
and planned transactions in the future, the better feedback the application can offer. It 
has much more potential; additional ideas include adjustments for a Venmo balance, a savings
tool, and accounting for other assets (savings and trading accounts). For now, the 
application offers a fast, seamless comprehensive overview of the user’s financial 
standpoint.

Please refer to AppOverview.pdf in the repository for more information.



