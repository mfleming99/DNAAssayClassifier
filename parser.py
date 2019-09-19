#method to take in a string of sam data and output read length, read frequency, and lopsidedness
import numpy as np
def parseString(txt):
    spliter = re.compile('\n+')
    readnumber = re.compile('[r]+\d+')
    line_spliter = re.compile('\t+')
    colon_spliter = re.compile(':')
    forward_reads = 0
    reverse_reads = 0
    unmatched_reads = 0
    read_positions = []
    position_differences = []
    read_lengths_count = 0;;
    read_lengths_total = 0;;
    # tlen = []
    # read_quality_unpaired = [[]]
    # read_quality_first = [[]]
    # read_quality_second = [[]]
    # match_scores = []
    # mapq_scores = []

    lines = spliter.split(txt)
    #Itterating though everyline
    for i in range(len(lines) - 1):
        get_match_score = True
        subline = line_spliter.split(lines[i])
        if (int(subline[1]) & 4 == 4):
            unmatched_reads += 1
            get_match_score = False
        elif (int(subline[1]) & 16 == 16):
            reverse_reads += 1
        else:
            forward_reads += 1
        read = subline[9]
        read_lengths_count++
        read_lengths_total += len(read)
        read_positions.append(subline[3])
        # if(int(subline[1]) & 2 == 2): #read is paired
        #     tlen.append(abs(int(subline[8])))
        #     if(int(subline[1]) & 64 == 64):
        #       for j in range(len(subline[10]) - 1):
        #           while(len(read_quality_first) < len(subline[10])):
        #               read_quality_first.append([])
        #           read_quality_first[j].append(subline[10][j])
        #     elif(int(subline[1]) & 128 == 128):
        #       for j in range(len(subline[10]) - 1):
        #           while(len(read_quality_second) < len(subline[10])):
        #               read_quality_second.append([])
        #           read_quality_second[j].append(subline[10][j])
        # else: #read is unpaired
        #   for j in range(len(subline[10]) - 1):
        #       while(len(read_quality_unpaired) < len(subline[10])):
        #           read_quality_unpaired.append([])
        #       read_quality_unpaired[j].append(subline[10][j])
        #
        # if (get_match_score):
        #     match_scores.append(int(colon_spliter.split(subline[11])[2]))
        #     mapq_scores.append(int(subline[4]))
    # except:
    # #     print("Invalid Line")
    # read_quality_unpaired = read_quality_converter(read_quality_unpaired)
    # read_quality_first = read_quality_converter(read_quality_first)
    # read_quality_second = read_quality_converter(read_quality_second)
    # return (forward_reads, reverse_reads, unmatched_reads, read_quality_unpaired, read_quality_first, read_quality_second, match_scores, tlen, mapq_scores)
    read_frequency = (forward_reads + reverse_reads) / (forward_reads + reverse_reads + unmatched_reads)
    read_lengths_average = read_lengths_total / read_lengths_count
    read_positions.sort()
    for i in range(len(read_positions) - 1):
        position_differences.append(read_positions[i + 1] - read_positions[i])
    std_dev_of_position_difference = np.std(position_differences)
    return (read_frequency, read_lengths_average, std_dev_of_position_difference)
