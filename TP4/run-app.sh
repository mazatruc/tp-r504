docker run -d \
	-it \
	-p 5000:5000 \
	--name tp4-app \
	--network net-tp4 \
	--mount type=bind, source="$app_1.py"/build, target=/srv \
	im-tp4