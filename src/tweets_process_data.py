import xlrd
import csv
from os import sys
import glob

#function to extract subset of the tweets
def extract_tweets_subset_from_csv(csv_file):
    csvf = glob.glob(csv_file)
    f = open('subset.csv', 'wt')# write into subset.csv
    for filename in csvf:
        try:
            reader = csv.reader(open(filename)) #CSV reader to open the file 'tweets.csv
            for row in reader:
                writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow((row[1],row[8], row[2]))
        except IndexError:
            pass
        finally:
            f.close()

# parsing the tweets.csv as argument to the main function e.g 'python tweet_data_subset.py tweets.csv'
if __name__ == "__main__":
    extract_tweets_subset_from_csv(sys.argv[1]) #argument parsing



