kmer_filter: kmer_filter.cc
	g++ kmer_filter.cc \
		-I/home/user/duanran/software/jellyfish/2.3.0/include/jellyfish-2.3.0/ \
		-L/home/user/duanran/software/jellyfish/2.3.0/lib/ \
		-static -ljellyfish-2.0 -lpthread \
		-o kmer_filter 