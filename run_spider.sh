for i in `seq 1 $1`;
do
	scrapy crawl crawly
	sleep 5
done
