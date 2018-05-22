#!/usr/bin/env python3 -W ignore::DeprecationWarning

import argparse
import logging
import os
import sys
import datetime
import time

from config import *


# Remove tensorflow CPU instruction information.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def _setup_argparser():
    """Sets up the argument parser and returns the arguments.

    Returns:
        argparse.Namespace: The command line arguments.
    """
    parser = argparse.ArgumentParser(description="Control program to launch all actions related to this project.")

    parser.add_argument("-m", "--model", action="store",
                        choices=["cnn_ngrams", "put_your_model_name_here2", "put_your_model_name_here3"],
                        default="cnn_ngrams",
                        type=str,
                        help="the model to be used, defaults to cnn_ngrams")
    parser.add_argument("-t", "--train",
                        help="train the given model",
                        action="store_true")
    parser.add_argument("-p", "--predict",
                        help="predict on a test set given the model",
                        action="store_true")


    args, unknown = parser.parse_known_args()

    return args


def get_latest_model():
    """Returns the latest directory of the model specified in the arguments.

    Returns:
        (path) a path to the directory.
    """
    print("Retrieving trained model from {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), out_trained_models)))
    if not os.path.exists(os.path.join(out_trained_models, args.model)):
        print("No trained model {} exists.".format(args.model))
        sys.exit(1)
    #Path to the model
    res = os.path.join(os.path.abspath("run.py"), "../trained_models", args.model)
    all_runs = [os.path.join(res, o) for o in os.listdir(res) if os.path.isdir(os.path.join(res, o))]
    res = max(all_runs, key=os.path.getmtime)

    return res


def get_submission_filename():
    """
    Returns:
        (path to directory) + filename of the submission file.
    """
    ts = int(time.time())
    submission_filename = "submission_" + str(args.model) + "_" + str(ts) + ".csv"
    submission_path_filename = os.path.join(get_latest_model(), submission_filename)

    return submission_path_filename


"""********************************************** USER ACTIONS from parser ************************************************************"""

if __name__ == "__main__":

    __file__ = "run.py"
    file_path = os.path.dirname(os.path.abspath(__file__))

    args = _setup_argparser()
    """
    #Once we get ready we can decomment. This avoids creating files when things have still to be debugged
    if args.train:
        out_trained_models = os.path.normpath(os.path.join(properties["SRC_DIR"],
                                              "../trained_models/",
                                              args.model,
                                              datetime.datetime.now().strftime(r"%Y-%m-%d[%Hh%M]")))
        try:
            os.makedirs(out_trained_models)
        except OSError:
            pass
    else:
        out_trained_models = os.path.normpath("..")
    """

    import training_utils as train_utils
    import negative_endings as data_aug
    from models import cnn_ngrams
    import numpy as np
    import keras


    if args.train:
        """Create a field with your model (see the default one to be customized) and put the procedure to follow to train it"""
        if args.model == "cnn_ngrams":

            print("cnn grams training invoked")
            
            #The things below are just a trial !
            neg_end = data_aug.Negative_endings(thr_new_noun = 0.8, thr_new_pronoun = 0.8, 
                               thr_new_verb = 0.8, thr_new_adj = 0.8, 
                               thr_new_adv = 0.8)
            neg_end.load_vocabulary()
    
            print("Loading pos tagged corpus (context) from ",train_pos_begin)
            all_stories_context_pos_tagged = np.load(train_pos_begin)

            all_stories_context_pos_tagged = neg_end.delete_id_from_corpus(corpus = all_stories_context_pos_tagged, endings = False)
            all_stories_endings_pos_tagged = neg_end.delete_id_from_corpus(corpus = all_stories_context_pos_tagged, endings = True)
            neg_end.filter_corpus_tags()

            all_stories = len(all_stories_endings_pos_tagged)
            for i in range(0,80000):
                neg_end.words_substitution_approach(neg_end.all_stories_endings_pos_tagged[i], is_w2v = False,
                                                    out_tagged_story = True, #Output a pos_tagged story if True
                                                    batch_size = 2,
                                                    shuffle_batch = True,
                                                    merge_sentences = True)
                if i%10000 ==0:
                    print("Negative ending(s) created for :",i, "/",all_stories)
            

            #train_generator = train_utils() # TODO
            #validation_generator = train_utils() # TODO



        elif args.model == "put_your_model_name_here2":

            print("Please put your procedure in here before running & remember to add the name of the model into the options of the parser!")

        elif args.model == "put_your_model_name_here3":
            
            print("Please put your procedure in here before running & remember to add the name of the model into the options of the parser!")
        

    if args.predict:

        """
           Path to the model to restore for predictions
        """

        """Submission file"""
        submission_path_filename = get_submission_filename()

        if args.model == "cnn_ngrams":
            
            #path_model_to_restore = os.path.join(get_latest_model(), "weights.h5")
            #print("Loading the last checkpoint of the model ", args.model, " from: ", path_model_to_restore)
            print("cnn grams prediction invoked")


        elif args.model == "put_your_model_name_here2":

            print("Put your code here before calling predict")

        elif args.model == "put_your_model_name_here3":

            print("Put your code here before calling predict")