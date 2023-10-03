cnvkit_source = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"
cnvrobot_source = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/sample_SAMPLE001_F_SEGMENTS_C-2_PoN-F_SEGM-smart-0.65_segmentation.tsv"
snp_source = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"

def extract_data_from_snp_source(snp_source):
    # Read data from source and extract CNV calls 
    # Return data in the format [("chr1", (start, end call)),....]
    # Store list in list in source list "call_data", [("chr1", (start, end call)),....]

    # Return data in the format [("chr1", (start, end call)),....]
    # Store list in list in source list "call_data", [("chr1", (start, end call)),....]

def extract_data_from_cnvkit_source():
    # Read data from source and extract CNV calls 
    # Return data in the format [("chr1", (start, end call)),....]
    # Store list in list in source list "call_data", [("chr1", (start, end call)),....]
    
def extract_data_from_cnvrobot_source():
    # Read data from source and extract CNV calls 
    # Return data in the format [("chr1", (start, end call)),....]
    # Store list in list in source list "call_data", [("chr1", (start, end call)),....]
    
#  extract data from each source 
snp_data = extract_data_from_snp_source()
cnvkit_source = extract_data_from_cnvkit_source()
cnvrobot_source = extract_data_from_cnvrobot_source()

# Organise data into the desired format
data_sources = [
    (
        "call_data",
        [
            ("chr1", (200000, 149000000, -0.2)),
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvkit_data",
        [
            ("chr1", (1, 249250621, 0.1)),
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvrobot_data",
        [
            # ("chr1", (1, 249250621, 0.05)),
            # Add data for other chromosomes if needed
        ],
    ),
]