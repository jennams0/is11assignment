import pandas as pd

#import the data set
data_set = pd.read_csv("video_games_raw.csv")

#allows user to select and edit row status
again = "next"
while again == "next":
    select_row = int(input("Select a row number to inspect: "))
    print(data_set.iloc[select_row])
    status_update = input("\nEnter your new game status (Backlog, Playing, Completed, or Dropped): ")
    data_set.at[select_row, "Status"] = status_update
    again = input("\nType 'next' to inspect another row, or any other key to exit: ")

#create and sort recommended games
data_set["Recommended"] = ""
data_set.loc[:, "Recommended"] = "No"
for i in range(len(data_set)):
    if data_set.at[i,"Rating"] >= 8 and data_set.at[i,"Price"] <= 40:
        data_set.at[i,"Recommended"] = "Yes"
#display recommended games
print("\nHere is a list of your recommended games:")
print(data_set.query("Recommended == 'Yes'"))

#upload to file
data_set.to_csv("video_games_cleaned.csv", index=False)
print("\nYour updated data set has been saved to video_games_cleaned.csv")