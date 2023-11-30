docker run -d \
	--name nginx1 \
	--mount type=bind,source=/home/user/tp-r504/TP-LB/tp-A/shared1,target=/usr/share/nginx/html \
	nginx:latest \


docker run -d \
	--name nginx2 \
	--mount type=bind,source=/home/user/tp-r504/TP-LB/tp-A/shared2,target=/usr/share/nginx/html \
	nginx:latest