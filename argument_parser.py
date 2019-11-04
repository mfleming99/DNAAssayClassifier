import argparse as ap

def get_args():
    p = ap.ArgumentParser()

    p.add_argument("--index", type=str, required=True,
        help="Where is the bowtie2 index")
    p.add_argument("--wgs", type=str, required=True,
        help="Where is the wgs csv")
    p.add_argument("--mrna", type=str, required=True,
        help="Where is the mrna csv")
    p.add_argument("--srna", type=str, required=True,
        help="Where is the srna")
    p.add_argument("--gtf", type=str, required=True,
        help="Where is the gtf")
    return p.parse_args()
