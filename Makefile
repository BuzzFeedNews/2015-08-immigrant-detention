IMM_DATA_PARTS = $(wildcard compressed-data/immigration-data.tar.gz-*)

.PHONY: \
	data \
	notebooks/detention-by-nationality-analysis.ipynb
	
data:
	cat $(IMM_DATA_PARTS) | tar -xzvf -

notebooks/detention-by-nationality-analysis.ipynb:
	jupyter nbconvert $@ \
        --ExecutePreprocessor.enabled=True \
		--ExecutePreprocessor.timeout=600 \
		--to notebook \
		--output $@
