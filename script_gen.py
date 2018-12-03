programs = ["/bin/echo", "/bin/grep", "./benchmarks/coremark/coremark.exe"]
prefetchers = ["bestoffset", "queued", "stride"]
cpus = ["TimingSimpleCPU","MinorCPU","DerivO3CPU"]
l2sizes = ["8MB","2MB","128kB"]
for pref in prefetchers:
	for prog in programs:
		for cpu in cpus:
			for l2size in l2sizes:
				print("./build/X86/gem5.opt --outdir ./results/",prog,pref,cpu,l2size, " configs/example/se.py -c ",prog," --caches --l2cache --l2_size ",l2size, " --mem-size 2048MB --cpu-type ",cpu," --prefetcher ", pref, sep='')
 
