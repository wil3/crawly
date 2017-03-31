for i in `seq 1 $1`;
do
	SECONDS=0
	scrapy crawl crawly
	delta=$SECONDS
	printf "$delta\n" >> t.out
	sleep 5
done
