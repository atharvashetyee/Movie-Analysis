
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import tempfile
import os

df = pd.DataFrame();

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "imbd_updated.csv")

def introduction():
    msg = '''
           Movies are integral part of our life. We love to watch movies but it is very hard to find out good 
          movies from the world cinema. 

           TMDB.org is a crowd-sourced movie information database used by many film-related consoles, 
           sites and apps, such as XBMC, MythTV and Plex. Dozens of media managers, mobile apps and 
           social sites make use of its API.
           
           TMDb lists some 80,000 films at time of writing, which is considerably fewer than IMDb. 
           While not as complete as IMDb, it holds extensive information for most popular/Hollywood films.
           
           This is dataset of the 10,000 most popular movies across the world has been fetched through the 
           read API. TMDB's free API provides for developers and their team to programmatically fetch and
           use TMDb's data. Their API is to use as long as you attribute TMDb as the source of the data
           and/or images. Also, they update their API from time to time.

          This data set is fetched using exception handling process so the data set contains some null 
          values as there are missing fields in the tmdb database. Thought it's good for a young analyst
          to deal with messing value.

          In this project we are going to analyse the same dataset using Python Pandas on windows machine but the 
          project can be run on any machine support Python and Pandas. Besides pandas we also used matplotlib python
          module for visualization of this dataset. 

          The whole project is divided into four major parts ie reading, analysis, visualization and export. all these
          part are further divided into menus for easy navigation

        
           \n\n\n\n'''
 
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')



    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()

def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nData Analysis MENU ')
            print('_'*100)
            print('1.  Show Whole DataFrame')
            print('2.  Show Columns')
            print('3.  Show Top Rows')
            print('4.  Row Bottom Rows')
            print('5.  Show Specific Column\n')
            print('6.  Add a New Record\n')
            print('7.  Add a New Column\n')
            print('8.  Delete a Column\n')
            print('9.  Delete a Record\n')
            print('10.  Update a Record\n')
            print('11.  Rating Wise Report \n')
            print('12.  Language wise Report \n')
            print('13.  Data Summary\n')
            print('14.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                print(df.columns)
                wait = input()
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input()
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input()
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==6:
                a = input('Enter Index Number :')
                b = input('Enter New Movie Name :')
                c = input(' Enter Movie Overview :')
                d= input('Enter Movie Language :')
                e = int(input('Enter Vote Count :'))
                f = float(input('Enter Vote Average :'))
                data={'index':a,'title':b,'overview':c,'language':d,'vote_count':e,'vote_average':f}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            if ch==7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name]=col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==8:
                col_name =input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==9:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()
            #update a record - this is to be cover
            if ch == 10:
                index_no = int(
                    input('Enter the Index Number that You want to update :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()
            
            if ch==11:
                g = df.sort_values(by=['vote_average','vote_count'],ascending=False)
                clear()
                print('Top 20 Movies Based on Rating')
                print('-'*120)
                print(g.head(20))

                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==12:
                df1=df.language.unique()
                print('Available Languages :',df1)
                print('\n\n')
                lang1 =input('Enter Language Type :')
                df1=df[df.language==lang1]
                clear()
                print('Top 20 Movies Based on Rating | Language :',lang1)
                print('-'*120)
                print(df1.sort_values(by='vote_average', ascending=False).head(20))
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch==13:
                print(df.describe())
                print("\n\n\nPress any key to continue....")
                wait=input()
            if ch == 14:
                break

# name of function      : graph
# purpose               : To generate a Graph menu


def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  Whole Data LINE Graph\n')
        print('2.  Whole Data Bar Graph\n')
        print('3.  Whole Data Bar Graph- Horizontal\n')
        print('4.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('Language')
            plt.ylabel('Total Movies')
            plt.title('Language wise movies count')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        if ch == 2:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Language')
            plt.ylabel('Total Movies')
            plt.title('Language wise movies count')
            plt.bar(x, y)
            plt.grid(True)
            plt.show()
        
        if ch == 3:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Language')
            plt.ylabel('Total Movies')
            plt.title('Language wise movies count')
            plt.barh(x, y)
        
            plt.grid(True)
            plt.show()

        
        
        if ch == 4:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  Text File\n')
        print('2.  Excel File\n')
        print('4.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch == 1:
            df.to_csv('C:/Users/hp/Project Export/data.txt')
            print('\n\nCheck your new file "newMovies.csv"  on C: Drive.....')
            wait = input()

        if ch == 2:
            df.to_csv('C:/Users/hp/Project Export/data.csv')
            print('\n\nCheck your new file "newMovies.xlsx"  on C: Drive.....')
            wait = input()

        

        if ch == 3:
            break


def main_menu():
    

           clear()
           introduction()
           
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice == 1:
                                
                                 read_csv_file()
                                 wait = input()

                      if choice == 2:
                                
                                 data_analysis_menu()
                                 wait = input()

                      if choice == 3:
                                 graph()
                                 wait = input()

                      if choice == 4:
                                 export_menu()
                                 wait = input()

                      if choice == 5:
                                 break
           clear()
        



# call your main menu
main_menu()
