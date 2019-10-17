import os, glob
import re


def segment_screenplay(script_file, new_script_file):
    """
    Find the manual segmentation of the screenplay into scenes and re-write the
    script file with seperation markers. Each scene is separated with a sequence
    of 40 '=' from the previous and next one. Also, before the beginning of each
    scene the scene index (starting from 0) is written between the '=' boundaries.
    :param script_file: Original raw script file for a movie
    :param new_script_file: New segmented script file
    :return: -
    """
    scenes = []
    last_scene = ''
    flag = 0
    with open(script_file, 'r') as f1:
        for line in f1.readlines():
            line_new = re.sub(' +', ' ', line)
            tmp_line = line_new.split()
            tmp_line = [x for x in tmp_line if x != '']
            if ((('INT.' in tmp_line or 'EXT.' in tmp_line or 'INT/EXT.' in tmp_line or
                             'EXT./INT.' in tmp_line or 'INT./EXT.' in tmp_line))):
                flag = 1
                if last_scene != '':
                    scenes.append(last_scene)
                last_scene = line
            else:
                if flag == 1:
                    last_scene += ('\n' + line)

    for i, scene in enumerate(scenes):
        with open(new_script_file, 'a+') as f1:
            f1.write('='*20)
            f1.write(str(i))
            f1.write('='*20)
            f1.write('\n')
            f1.write(scene)
            f1.write('\n')
            f1.write('='*40)
            f1.write('\n')

    return


if __name__ == '__main__':
    screenplays_folder = './Screenplays_and_imdb_meta'
    new_segmented_screenplays = './Segmented_screenplays'

    if not os.path.exists(new_segmented_screenplays):
        os.makedirs(new_segmented_screenplays)

    movie_folder_list = [x[0] for x in os.walk(screenplays_folder)]
    movie_folder_list = glob.glob(screenplays_folder + "/*/")

    for movie in movie_folder_list:
        movie_name = movie.split('/')[-2]
        print(movie_name)
        script_file = os.path.join(movie, movie_name + '_script.txt')
        new_script_file = os.path.join(new_segmented_screenplays,
                                       movie_name + '_script_segmented.txt')
        segment_screenplay(script_file, new_script_file)
        break
