import os
import sys

ranks = {}

def rankquery(title):
    print "querying.."
    strip = title.replace("_", " ")
    # print strip
    print ranks.get(strip)
    
def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    scores = open(os.path.join(__location__, "pagetitlerank.txt"), "r")

    # for line in scores:
    # ranks = {}
    
    while True:
        name = scores.readline().strip("\n")
        score = scores.readline().strip("\n")
        # name.strip("\\n")
        # score.strip("\\n")
        ranks[name] = score
        if not name:
            break
    print "done"
    # print ranks
    if sys.argv[1]:
        cmd = sys.argv[1]
        print cmd
        return rankquery(cmd)


if __name__ == '__main__':
    main()