week=$1
(
    cd Scraper
    python3 scraper_script.py $week
)

cp ./Scraper/*.csv ./Submission/
for file in ./Submission/*.csv;
do
    # python3 ./Submission/organizeCodes.py Submissions $file
    (
        cd Submission
        # echo $file
        python3 organizeCodes.py Submissions $file
    )
    cp -r ./Submission/Submissions moss/
    rm -r ./Submission/Submissions
    (
        cd moss
        python3 run_moss.py $file
        rm -r hwX_join
        rm -r hwX_prune
        rm -r Submissions
        mkdir hwX_join
        mkdir hwX_prune
    )
done
mv ./moss/plagiarismReport.csv ./plagiarismReport_week$week.csv
