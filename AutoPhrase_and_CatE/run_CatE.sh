cd src
make cate
cd ..

./src/cate -train ./datasets/covid19/input_8k.txt -topic-name ./datasets/covid19/topics.txt \
	-load-emb word2vec_100.txt \
	-spec ./datasets/covid19/emb_topics_spec.txt \
	-word-emb ./datasets/covid19/emb_topics_w.txt \
	-topic-emb ./datasets/covid19/emb_topics_t.txt \
	-res ./datasets/covid19/res_topics.txt -k 50 -binary 0 \
	-size 100 -iter 6 -pretrain 2 -expand 1 -window 5 -negative 5 -sample 1e-3 -min-count 3 -threads 12
	 