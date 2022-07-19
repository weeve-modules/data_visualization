echo "Started the script"
while sleep $INTERVAL
do
  echo "Saving an image"

  cur_time=`date +'%r'`
  /opt/vc/bin/raspistill -o /home/pi/images/graph.png
  echo "Saved image at $cur_time"xd
  curl -X POST -F 'image=@/home/pi/images/graph.png' $EGRESS_API_HOST
done