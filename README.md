## TRIPOD

### TuRnIng POint Dataset 

This repository contains the screenplays and plot synopses with turning point (TP) annotations for 99 movies. Each movie contains:

1. The [Wikipedia] plot synopsis (extended summary of 35 sentences on average) with sentence-level TP annotations.
2. The screenplay (all dialogue and description parts of the movie) segmented into scenes (selected from the [Scriptbase dataset]).
4. The cast information (according to [IMDb]).

We split the dataset into training and test. For the movies of the test set, we also provide scene-level TP annotations for the corresponding screenplays.

#### Screenplays_and_imdb_meta folder

This folder contains the screenplays (./moviename/moviename\_script.txt) and the imdb meta-data (./moviename/moviename\_imdb\_meta.txt) for all movies in TRIPOD.

#### Synopses_and_annotations folder

This folder contains:

1. TRIPOD\_synopes\_train.csv: all synopses and respective TP annotations for the movies of the training set. 

It contains the movie name, the raw synopsis, the synopsis segmented into sentences and the sentence index (starting from 0) that corresponds to each TP.

*Note: As part of annotations, we also provide multiple annotations for a given movie when available and reliable. For this reason, the movie name is the actual movie name with an underscore and the index of the annotation (e.g., Reservoir Dogs\_0, Reservoir Dogs\_1, Reservoir Dogs\_2...). For the movies with only one set of available annotations there is only the moviename\_0 version.* 

2. TRIPOD\_synopses\_test.csv: all synopses and respective TP annotations for the movies of the test set.

3. TRIPOD\_screenplays\_test.csv: the goldstandard annotations for the screenplays of the test set.

It contains the movie name and a list of screenplay scene indices (starting from 0) that corresponds to each TP.

#### screenplays_scene_segmentation.py file

Python script for segmenting the screenplays into scenes following tha manual segmentation of the screenwriters. This segmentation also agrees with the scene indices that are provided for the goldstandard annotations of the screenplays in the test set. 

[Wikipedia]: https://www.wikipedia.org/
[Scriptbase dataset]: https://github.com/EdinburghNLP/scriptbase
[IMDb]: https://www.imdb.com/
